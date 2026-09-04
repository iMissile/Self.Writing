"""Корни на машине. ЕДИНСТВЕННОЕ, что правится при переносе проекта.

Ни один другой модуль не знает путей к машине. Проверка:
    grep -rn "[A-Z]:[\\/]" lab/ | grep -v paths.py
должен давать пусто.
"""
from __future__ import annotations

import os
from pathlib import Path

_ENV = "REPORT_PROJECT_DATA"          # переопределение без правки файла

_CANDIDATES = [
    Path(r"S:/_data/<project>"),      # рабочая машина
    Path.home() / "data" / "<project>",
    Path("/mnt/data/<project>"),
]

LAB = Path(__file__).resolve().parent
ROOT = LAB.parent
ARTIFACTS = LAB / "_artifacts"
CACHE = LAB / "_cache"
SANDBOX = LAB / "_ai_temp_scripts"    # черновики разведки — только сюда
MODEL = LAB / "model"


def data_root() -> Path:
    """Корень исходных данных. Ошибка называет, где искали, — молчаливое
    умолчание превратило бы отсутствие данных в пустой прогон."""
    if env := os.environ.get(_ENV):
        p = Path(env)
        if p.exists():
            return p
        raise FileNotFoundError(f"{_ENV}={env} — каталога нет")
    for p in _CANDIDATES:
        if p.exists():
            return p
    raise FileNotFoundError(
        "корень данных не найден; проверены: "
        + ", ".join(str(p) for p in _CANDIDATES)
        + f"; либо задайте {_ENV}"
    )


for _d in (ARTIFACTS, CACHE, SANDBOX):
    _d.mkdir(parents=True, exist_ok=True)
