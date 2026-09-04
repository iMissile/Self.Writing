"""Прогоны и манифест.

Отчёт читает ДАТИРОВАННЫЙ прогон, а не «последнее, что лежало в памяти».
Прогоны не перезаписываются: без истории вопрос «что изменилось после правки»
отвечается по памяти, а это не ответ.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import polars as pl

MANIFEST = "run_manifest.json"


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


@dataclass
class Run:
    """Каталог прогона. Одно имя витрины — один файл в прогоне."""
    path: Path
    manifest: dict = field(default_factory=dict)

    # ---- чтение ----------------------------------------------------------
    def table(self, name: str) -> pl.DataFrame:
        f = self.path / f"{name}.parquet"
        if not f.exists():
            # Отсутствие файла неотличимо от «эту витрину не считали»,
            # поэтому это ошибка, а не пустой фрейм.
            raise FileNotFoundError(
                f"витрина {name!r} отсутствует в прогоне {self.path.name}; "
                f"пустые витрины прогона: {self.manifest.get('artifacts_empty', [])}"
            )
        return pl.read_parquet(f)

    def thresholds_frame(self) -> pl.DataFrame:
        th = self.manifest.get("thresholds", {})
        return pl.DataFrame({"key": list(th), "value": [str(v) for v in th.values()]})

    # ---- запись ----------------------------------------------------------
    def save(self, name: str, df: pl.DataFrame) -> None:
        """Пустая витрина пишется файлом с объявленной схемой, а её имя
        попадает в artifacts_empty: иначе пустой раздел читается как
        отсутствие нарушений."""
        f = self.path / f"{name}.parquet"
        if f.exists():
            raise FileExistsError(
                f"витрина {name!r} уже есть в прогоне: второй отчёт затёр бы "
                "первый молча"
            )
        df.write_parquet(f)
        key = "artifacts_empty" if df.height == 0 else "artifacts"
        self.manifest.setdefault(key, []).append(name)

    def update(self, **blocks) -> None:
        """Второй отчёт ДОПИСЫВАЕТ манифест, не затирая чужое; пустое
        значение не затирает заполненное."""
        for block, values in blocks.items():
            cur = self.manifest.setdefault(block, {})
            for k, v in (values or {}).items():
                if v is None or (isinstance(v, (list, dict, str)) and not v):
                    continue
                cur[k] = v

    def flush(self) -> None:
        (self.path / MANIFEST).write_text(
            json.dumps(self.manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def new_run(root: Path, obj: str, *, model_dir: Path | None = None,
            thresholds: dict | None = None, code_version: str = "") -> Run:
    """Имя каталога — момент расчёта И объект: сравниваются прогоны одного
    объекта, разные расходятся по всем показателям сразу."""
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    path = root / f"{stamp}__{obj}"
    path.mkdir(parents=True, exist_ok=False)
    manifest = {
        "run_id": path.name,
        "object": obj,
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "code_version": code_version,
        # Хэши модели: иначе прогон воспроизводим только вместе с рабочей копией.
        "model_files": {f.name: _sha(f) for f in sorted((model_dir or path).glob("*.json"))},
        "thresholds": thresholds or {},     # вопрос «при каких порогах» — по файлу
        "counters": {}, "metrics": {},
        "artifacts": [], "artifacts_empty": [], "warnings": [],
    }
    run = Run(path, manifest)
    run.flush()
    return run


def load_run(root: Path, run_id: str | None = None) -> Run:
    """Без `run_id` берётся последний по имени — имя лексикографически
    совпадает с хронологией. Отчёт, публикуемый наружу, задаёт `run_id`
    явно: «последний» завтра будет другим."""
    if run_id:
        path = root / run_id
    else:
        runs = sorted(p for p in root.iterdir() if (p / MANIFEST).exists())
        if not runs:
            raise FileNotFoundError(f"прогонов нет в {root}")
        path = runs[-1]
    return Run(path, json.loads((path / MANIFEST).read_text(encoding="utf-8")))


def balance(before: pl.DataFrame, after: pl.DataFrame, step: str,
            *, expect: str = "equal") -> None:
    """Строки не исчезают молча: расхождение называет шаг и величину."""
    if expect == "equal" and before.height != after.height:
        raise ValueError(f"{step}: было {before.height}, стало {after.height}")
    if expect == "not_grow" and after.height > before.height:
        raise ValueError(f"{step}: рост строк {before.height} -> {after.height}")
