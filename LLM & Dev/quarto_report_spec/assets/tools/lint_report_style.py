"""Молчаливые дефекты подачи: разметка без `md()` и число мимо форматтера.

Оба дефекта не роняют сборку. Таблица рисуется, отчёт собирается, тесты
зелёные — неверна только вёрстка, и заметить её можно единственным способом:
глазами на собранном HTML. Ровно поэтому разметка без `md()` живёт долго
и тиражируется копированием соседней шапки.

Правило, за которым нет механического исполнителя, — намерение. Здесь
исполнитель.

Что ловится:

  §md    разметка в аргументе шапки `great_tables` без `md()` / `html()`.
         Обычная строка уходит через `html.escape`, который НЕ трогает
         обратную кавычку, — на странице видна сама кавычка, а не разбор.

  §num   число печатается мимо общего форматтера: разрядная запятая в
         форматной спецификации (`{x:,.0f}`) вместо `nfmt()`. Формат,
         собранный на месте, расходится от таблицы к таблице, а замена
         запятых по всей строке съедает запятые прозы.

Запуск:  uv run python lab/tools/lint_report_style.py [файл ...]
         без аргументов — все `.qmd` и `lib/*.py` лаборатории.

Срабатывание имеет ровно три исхода, и молчаливого среди них нет: правка,
строка `# обосновано: <почему>` рядом, либо принятие базой после разбора.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]

#: Методы great_tables, чей текст печатается читателю и допускает `md()`.
#: Перечень закрытый: именно эти пять документированы как принимающие разметку.
MD_METHODS = {"tab_header", "tab_source_note", "tab_spanner",
              "tab_stubhead", "cols_label"}

#: Образцы разметки. Одиночные `*` и `_` НЕ входят намеренно: в русской прозе
#: они встречаются знаками, а не выделением, и ловить их значило бы топить
#: находки в шуме.
MARKUP = re.compile(r"`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\)")

#: Разрядный разделитель в форматной спецификации: `{x:,.0f}`, `{x:_d}`.
FMT_SPEC = re.compile(r"[,_][^}]*[fd]")

CHUNK = re.compile(r"^```\{python\}\n(.*?)^```", re.S | re.M)
EXCUSE = re.compile(r"#\s*обосновано:")


def _sources(path: Path) -> list[tuple[int, str]]:
    """(смещение строк, исходник) — для .py один кусок, для .qmd каждый чанк."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        return [(0, text)]
    out = []
    for m in CHUNK.finditer(text):
        out.append((text[:m.start(1)].count("\n"), m.group(1)))
    return out


def _md_hits(tree: ast.AST) -> list[tuple[int, str]]:
    hits = []
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr in MD_METHODS):
            continue
        for arg in [*n.args, *(k.value for k in n.keywords)]:
            if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) \
               and arg.func.id in {"md", "html"}:
                continue
            src = ast.unparse(arg)          # склейка строк и f-строка уже развёрнуты
            if MARKUP.search(src):
                # `n.lineno` у звена цепочки указывает на НАЧАЛО цепочки, а не
                # на сам метод: у `GT(df).tab_header(…).tab_spanner(…)` обе
                # находки уехали бы на строку с `GT(`. Имя метода стоит в
                # `func`, и его конец — та строка, которую надо править.
                hits.append((n.func.end_lineno or n.lineno,
                             f"{n.func.attr}(…{src[:48]}…) без md()"))
    return hits


def _num_hits(tree: ast.AST) -> list[tuple[int, str]]:
    hits = []
    for n in ast.walk(tree):
        if isinstance(n, ast.FormattedValue) and n.format_spec is not None:
            spec = ast.unparse(n.format_spec)
            if FMT_SPEC.search(spec):
                hits.append((n.lineno, f"{spec} — разряды мимо nfmt()"))
    return hits


def lint(path: Path) -> list[str]:
    out: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for offset, src in _sources(path):
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue                        # синтаксис ловит дымовой прогон
        for code, hits in (("§md", _md_hits(tree)), ("§num", _num_hits(tree))):
            for lineno, what in hits:
                real = offset + lineno
                near = "\n".join(lines[max(0, real - 3):real])
                if EXCUSE.search(near):     # обоснование рядом снимает срабатывание
                    continue
                out.append(f"{path.name}:{real}  {code}  {what}")
    return out


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv] if argv else [
        *sorted(LAB.glob("*.qmd")), *sorted((LAB / "lib").glob("*.py"))]
    if hasattr(sys.stdout, "reconfigure"):  # см. references/tooling.md
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    found = [msg for t in targets if t.exists() for msg in lint(t)]
    for msg in found:
        print(msg)
    print(f"\nсрабатываний: {len(found)}")
    return 1 if found else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
