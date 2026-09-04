"""Разность двух прогонов по манифестам. Сравнение по двум окнам — сравнение
по памяти, а это не ответ.

Сравниваются прогоны ОДНОГО объекта: разные объекты расходятся по всем
показателям сразу, и такая разность не говорит о правке ничего.

Запуск:  uv run python lab/tools/diff_runs.py <прогон_ДО> <прогон_ПОСЛЕ>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

KEYS = ("thresholds", "counters", "metrics")


def load(p: Path) -> dict:
    f = p if p.is_file() else p / "run_manifest.json"
    return json.loads(f.read_text(encoding="utf-8"))


def main(a: str, b: str) -> int:
    before, after = load(Path(a)), load(Path(b))
    if before.get("object") != after.get("object"):
        print(f"РАЗНЫЕ ОБЪЕКТЫ: {before.get('object')} и {after.get('object')} "
              "— такая разность ничего не говорит о правке")
        return 1
    changed = 0
    for block in KEYS:
        lhs, rhs = before.get(block, {}), after.get(block, {})
        for k in sorted(set(lhs) | set(rhs)):
            x, y = lhs.get(k), rhs.get(k)
            if x != y:
                changed += 1
                print(f"{block}.{k}: {x} -> {y}")
    empt = set(after.get("artifacts_empty", [])) - set(before.get("artifacts_empty", []))
    for name in sorted(empt):
        print(f"витрина стала пустой: {name}")
    print(f"\nизменилось значений: {changed}")
    if changed == 0:
        print("ВНИМАНИЕ: содержательная правка, не сдвинувшая ни одного числа, "
              "означает, что правка никуда не подключена")
    else:
        print("объяснить КАЖДОЕ изменившееся число")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    raise SystemExit(main(*sys.argv[1:]))
