"""Дымовой рендер: чанки отчёта исполняются за секунды вместо минут.

Ловит то, что чаще всего и ломается: несуществующую колонку, пустую витрину
без объявленной схемы, расчёт ширины на нетиповом типе. Поэтому он ОБЯЗАН
трогать данные по-настоящему, а не подменять отрисовку заглушкой.

Дополнительно ловит нарушение однородности: два `inject_css(engine=…)`
с разными движками в одном файле — правило «один отчёт — один движок».

Запуск:  uv run python lab/tools/render_smoke.py [отчёт.qmd ...]
"""
from __future__ import annotations

import re
import sys
import traceback
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
CHUNK = re.compile(r"^```\{python\}\n(.*?)^```", re.S | re.M)
ENGINE = re.compile(r"inject_css\(\s*engine\s*=\s*[\"'](\w+)[\"']")


def smoke(qmd: Path) -> list[str]:
    src = qmd.read_text(encoding="utf-8")
    errors: list[str] = []

    engines = set(ENGINE.findall(src))
    if len(engines) > 1:
        errors.append(f"два графических движка в одном отчёте: {sorted(engines)}")

    ns: dict = {"__name__": "__smoke__"}
    if str(LAB) not in sys.path:
        sys.path.insert(0, str(LAB))
    for i, chunk in enumerate(CHUNK.findall(src), 1):
        try:
            exec(compile(chunk, f"{qmd.name}#{i}", "exec"), ns)
        except Exception:
            errors.append(f"чанк {i}:\n{traceback.format_exc(limit=3)}")
            break                      # дальше всё равно посыплется
    return errors


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv] or sorted(LAB.glob("*.qmd"))
    if not targets:
        print("отчётов не найдено")
        return 1
    bad = 0
    for qmd in targets:
        errs = smoke(qmd)
        print(f"{'FAIL' if errs else ' ok '}  {qmd.name}")
        for e in errs:
            print("   ", e.replace("\n", "\n    "))
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
