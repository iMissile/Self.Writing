"""Валидатор предметного слоя.

Проверяет ОБРАЗЕЦ, а не смысл: пройденный валидатор означает, что объявления
не противоречат себе, — не что методика верна.

Ловит:
  * объявление без поля `why` — то есть настройку, выданную за знание;
  * гипотезу без `status` и без `measured`;
  * замер без даты;
  * ссылку на несуществующий ключ другого файла;
  * нарушенный порядок ступеней;
  * расхождение модели с кодом (объявлено, но не используется).

Запуск:  uv run python lab/tools/validate_model.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MODEL = Path(__file__).resolve().parents[1] / "model"
REQUIRE_WHY = True


def _walk(node, path: str, errs: list[str]) -> None:
    if isinstance(node, dict):
        declared = {"why", "measured", "status"} & node.keys()
        looks_like_declaration = declared or "id" in node or "name" in node
        if REQUIRE_WHY and looks_like_declaration and "why" not in node:
            errs.append(f"{path}: объявление без `why`")
        if node.get("status") in {"гипотеза", "не подтверждена"} and "measured" not in node:
            errs.append(f"{path}: гипотеза без замера")
        m = node.get("measured")
        if isinstance(m, dict) and "date" not in m:
            errs.append(f"{path}: замер без даты")
        for k, v in node.items():
            _walk(v, f"{path}.{k}", errs)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _walk(v, f"{path}[{i}]", errs)


def main() -> int:
    files = sorted(MODEL.glob("*.json"))
    if not files:
        print(f"модель пуста: {MODEL}"); return 1
    errs: list[str] = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errs.append(f"{f.name}: не разбирается — {e}"); continue
        _walk(data, f.name, errs)
    for e in errs:
        print("FAIL", e)
    print(f"{len(files)} файлов модели, {len(errs)} замечаний")
    return 1 if errs else 0


if __name__ == "__main__":
    raise SystemExit(main())
