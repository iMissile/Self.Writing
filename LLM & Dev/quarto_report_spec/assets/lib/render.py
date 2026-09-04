"""Отрисовка: таблицы, карточки, графики. Два графических стека, один на отчёт.

Однородность отчётов держится здесь. Один табличный движок на длинные витрины
(reactable), один на короткие фиксированные выборки (great_tables), один
графический — ECharts ЛИБО Plotly. Смешивать нельзя: читатель считает разное
оформление разным смыслом.

Движок объявляется отчётом один раз: `inject_css(engine="echarts")` или
`inject_css(engine="plotly")` в setup-чанке. Второй движок в том же документе
даёт исключение, а не второй `<script>`: правило, за которым нет исполнителя,
остаётся намерением.

Подписи по-русски живут ТОЛЬКО на этом слое. В данных колонки латиницей: иначе
имя колонки становится частью предметной модели и меняется вместе с
формулировкой в отчёте.

pandas здесь нет и не предполагается. ECharts принимает списки, Plotly —
numpy; ни одному из них pandas не нужен.
"""
from __future__ import annotations

import json
import uuid
from pathlib import Path

import polars as pl
import reactable as rt
from great_tables import GT, md  # noqa: F401  (md — для разметки в шапках)
from htmltools import HTML, TagList
from IPython.display import HTML as IpyHTML
from IPython.display import display as _ipy_display
from reactable import Reactable
from reactable.models import RowInfo
from reactable.widgets import STATIC_FILES

__all__ = ["inject_css", "react", "react_nested", "gt_table", "gt_num",
           "cards", "legend", "nfmt", "mfmt",
           "bar", "pie", "hist", "tree", "show", "PALETTE", "ENGINES"]

#: Палитра отчёта. Смысловая, а не декоративная: результат, триаж и
#: неисполненная проверка обязаны различаться с одного взгляда.
PALETTE = {
    "money": "#1f77b4",    # предъявляемый результат
    "triage": "#e8a33d",   # сортировка, ещё не результат
    "service": "#8c8c8c",  # служебное
    "good": "#2e8b57",
    "bad": "#c0392b",
    "none": "#b0b0b0",     # пусто / не исполнено
}
COLORWAY = [PALETTE["money"], PALETTE["triage"], PALETTE["service"],
            PALETTE["good"], PALETTE["bad"]]

ENGINES = ("echarts", "plotly")

_MIN_W, _MAX_W, _PX_PER_CHAR, _FIT_W = 90, 460, 8, 1080

# Состояние документа. Отчёт объявляет движок один раз; повторное объявление
# другого — ошибка устройства отчёта, а не повод выдать второй вендор.
_ENGINE: str | None = None
_LIB_EMITTED: set[str] = set()


# --------------------------------------------------------------------------
# подключение
# --------------------------------------------------------------------------

_RT_CSS = """
<style>
.rp-rt{width:100%;max-width:100%;min-width:0;box-sizing:border-box;}
.rp-rt .rt-table{width:100%!important;max-width:100%!important;min-width:0;table-layout:fixed;}
.rp-rt .rt-th-inner,.rp-rt .rt-td-inner,.rp-rt .rt-text-content{white-space:normal!important;overflow:visible!important;}
.rp-rt .rt-td,.rp-rt .rt-th{font-size:14px!important;}
.rp-rt .rt-td{word-break:break-word;white-space:normal;vertical-align:top;}
</style>"""


def inject_css(engine: str = "echarts") -> None:
    """CSS витрин и ОДИН графический вендор — из setup-чанка, не из шапки.

    Порядок обязателен и наблюдался на живом рендере Quarto:

    1. CSS эмитится первым. Вывод ячейки, состоящий из одних <script>,
       Quarto теряет целиком; CSS из той же ячейки доезжает и служит якорем.
    2. Библиотека эмитится здесь и только здесь. Ячейка с `#| label: fig-…`
       оборачивается в <figure>, и огромный <script> из неё вырезается:
       короткий init остаётся, библиотека — нет.
    3. Рядом с megascript — скрытый якорный элемент.

    Quarto грузит RequireJS: UMD-сборка, видящая `define`, уходит в AMD и не
    создаёт глобал — canvas пустой, ошибки нет. Поэтому `define` снимается
    на время загрузки. Для plotly.js >= 3 это избыточно (ветки AMD в бандле
    нет), но порядок держится один на оба движка.
    """
    global _ENGINE
    if engine not in ENGINES:
        raise ValueError(f"неизвестный движок: {engine!r}; ожидается {ENGINES}")
    if _ENGINE is not None and _ENGINE != engine:
        raise RuntimeError(
            f"в документе уже объявлен движок {_ENGINE!r}, запрошен {engine!r}. "
            "Один отчёт — один графический движок: смешение читается как "
            "разный смысл. Разнести графики по двум отчётам или переписать "
            "их на один стек."
        )
    _ENGINE = engine

    css = STATIC_FILES.joinpath("reactable-py.esm.css").read_text(encoding="utf-8")
    _ipy_display(IpyHTML(f"<style>{css}</style>"))
    _ipy_display(IpyHTML(_RT_CSS))

    lib = _vendor(engine)
    if lib:
        _ipy_display(IpyHTML(f'{lib}<div id="rp-lib-anchor" hidden></div>'))


def _vendor(engine: str) -> str:
    """Вендоренный JS движка, один раз на документ."""
    if engine in _LIB_EMITTED:
        return ""
    _LIB_EMITTED.add(engine)
    src = _vendor_source(engine)
    return ("<script>window.__rp_def=window.define; window.define=undefined;</script>"
            f"<script>{src}</script>"
            "<script>window.define=window.__rp_def; delete window.__rp_def;</script>")


def _vendor_source(engine: str) -> str:
    if engine == "echarts":
        # Пакета нет и не нужен: опции — обычный dict. Цена отказа от пакета:
        # версия движка не связана с окружением и обновляется руками.
        p = Path(__file__).parent / "assets" / "echarts.min.js"
        if not p.exists():
            raise FileNotFoundError(f"вендор ECharts не найден: {p}")
        return p.read_text(encoding="utf-8")

    # Plotly: бандл берётся ИЗ УСТАНОВЛЕННОГО ПАКЕТА, не из CDN и не из npm.
    # pio.to_json кодирует числовые массивы в base64 (bdata); бандл другой
    # ветки прочитает такую фигуру пустым графиком без ошибки.
    import plotly
    p = Path(plotly.__file__).parent / "package_data" / "plotly.min.js"
    if not p.exists():
        raise FileNotFoundError(f"вендор Plotly не найден в пакете: {p}")
    _register_template()
    return p.read_text(encoding="utf-8")


def _register_template() -> None:
    """Проектный шаблон Plotly. Умолчание `plotly` весит ~7 КБ на КАЖДУЮ
    фигуру и рисует чужой палитрой; минимальный проектный — десятки байт."""
    import plotly.graph_objects as go
    import plotly.io as pio
    if "report" not in pio.templates:
        pio.templates["report"] = go.layout.Template(layout=dict(
            colorway=COLORWAY,
            font=dict(size=13),
            paper_bgcolor="white", plot_bgcolor="white",
            separators=", ",          # локали внутри бандла нет
            margin=dict(l=56, r=24, t=48, b=48),
        ))
    pio.templates.default = "report"


def _require(engine: str, genre: str) -> None:
    if _ENGINE is None:
        raise RuntimeError("сначала inject_css(engine=…) в setup-чанке")
    if _ENGINE != engine:
        raise RuntimeError(
            f"{genre} рисуется движком {engine!r}, а отчёт объявил {_ENGINE!r}. "
            "Стек выбирается по жанру при создании отчёта и не меняется внутри него."
        )


# --------------------------------------------------------------------------
# графики: ECharts
# --------------------------------------------------------------------------

class _Js(str):
    """Тело JS-функции. В option JSON остаётся функцией, а не строкой."""


_NUM_AXIS = _Js("function(v){if(v==null||v==='')return '';"
                "return Math.round(Number(v)).toLocaleString('ru-RU');}")
_NUM_LABEL = _Js("function(p){var n=p.value;if(n==null||n==='-')return '';"
                 "return Math.round(Number(n)).toLocaleString('ru-RU');}")


def _dumps_opts(options: dict) -> str:
    """JSON опций ECharts: функции не квотируются, `<` не рвёт HTML."""
    funcs: dict[str, str] = {}

    def walk(obj):
        if isinstance(obj, _Js):
            key = f"__JS_{len(funcs)}__"
            funcs[key] = str(obj)
            return key
        if isinstance(obj, dict):
            return {k: walk(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [walk(v) for v in obj]
        return obj

    raw = json.dumps(walk(options), ensure_ascii=False)
    for key, code in funcs.items():
        raw = raw.replace(f'"{key}"', code)
    return raw.replace("<", "\\u003c")


def _echarts_html(options: dict, *, height: str) -> HTML:
    """div + короткий init. Библиотека уже в документе из inject_css()."""
    cid = f"ec_{uuid.uuid4().hex[:10]}"
    return HTML(f"""<div id="{cid}" style="width:100%;min-height:{height};"></div>
<script>
(function() {{
  function boot() {{
    var el = document.getElementById("{cid}");
    if (!el) return;
    if (!window.echarts) {{
      el.textContent = "диаграмма не загрузилась: нет echarts";
      el.style.color = "{PALETTE['bad']}"; return;
    }}
    var inst = echarts.getInstanceByDom(el) || echarts.init(el, null, {{renderer: "canvas"}});
    inst.setOption({_dumps_opts(options)}, true);
    inst.resize();
  }}
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
  window.addEventListener("resize", function() {{
    var el = document.getElementById("{cid}");
    var inst = el && echarts.getInstanceByDom(el);
    if (inst) inst.resize();
  }});
}})();
</script>""")


# --------------------------------------------------------------------------
# графики: Plotly
# --------------------------------------------------------------------------

def _plotly_html(fig, *, height: int) -> HTML:
    """div + короткий init. pio.to_json сам экранирует `<` и не-ASCII,
    поэтому ручная замена, нужная ECharts, здесь не требуется."""
    import plotly.io as pio
    cid = f"pl_{uuid.uuid4().hex[:10]}"
    fig.update_layout(height=height)
    spec = pio.to_json(fig)
    # typesetMath: false — публичный конфиг. Приватный patch plotly.io._html
    # не применяется: он читается только to_html, а глобал PlotlyConfig
    # в plotly.js >= 3 не используется вовсе.
    cfg = json.dumps({"responsive": True, "displaylogo": False,
                      "typesetMath": False})
    return HTML(f"""<div id="{cid}" style="width:100%;"></div>
<script>
(function() {{
  function boot() {{
    var el = document.getElementById("{cid}");
    if (!el) return;
    if (!window.Plotly) {{
      el.textContent = "диаграмма не загрузилась: нет plotly";
      el.style.color = "{PALETTE['bad']}"; return;
    }}
    var f = {spec};
    Plotly.react(el, f.data, f.layout, {cfg});
  }}
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
}})();
</script>""")


# --------------------------------------------------------------------------
# графики: единый вызов из отчёта
# --------------------------------------------------------------------------

def bar(df: pl.DataFrame, cat: str, val: str, *, title: str = "",
        series: str = "", height: int = 360, horizontal: bool = False):
    """Полоса. Порядок категорий — порядок строк во фрейме: сортировка
    делается до вызова, а не выражением внутри графика.

    Ось величин от нуля: обрезанная шкала преувеличивает разность и читается
    как находка."""
    cats = [("—" if c is None else str(c)) for c in df[cat].to_list()]
    if _ENGINE == "plotly":
        import plotly.graph_objects as go
        vals = df[val].to_numpy()          # bdata компактнее списка
        fig = go.Figure(go.Bar(
            x=vals if horizontal else cats,
            y=cats if horizontal else vals,
            orientation="h" if horizontal else "v",
            name=series or val,
            marker_color=PALETTE["money"],
            texttemplate="%{value:,.0f}",   # знаменатель и величина — на печати,
            textposition="outside",         # а не в подсказке
        ))
        axis = dict(categoryorder="array", categoryarray=cats)
        fig.update_layout(
            title=title, showlegend=False,
            **({"yaxis": axis, "xaxis": dict(rangemode="tozero")} if horizontal
               else {"xaxis": axis, "yaxis": dict(rangemode="tozero")}),
        )
        return _plotly_html(fig, height=height)

    _require("echarts", "полоса")
    vals = [None if v is None else float(v) for v in df[val].to_list()]
    value_axis = {"type": "value", "min": 0, "axisLabel": {"formatter": _NUM_AXIS}}
    cat_axis = {"type": "category", "data": cats,
                "axisLabel": {"interval": 0, "rotate": 0 if horizontal else 30}}
    opt = {
        "type": "bar", "name": series or val, "data": vals,
        "itemStyle": {"color": PALETTE["money"]},
    }
    if horizontal:
        height = max(height, 72 * len(cats) + 140)
        opt["label"] = {"show": True, "position": "right", "formatter": _NUM_LABEL}
    return _echarts_html({
        "title": {"text": title, "left": "center", "padding": [0, 0, 12, 0]},
        "tooltip": {"trigger": "axis"},
        "grid": {"left": "2%", "right": "14%", "top": "18%", "bottom": "8%",
                 "containLabel": True},
        "xAxis": value_axis if horizontal else cat_axis,
        "yAxis": cat_axis if horizontal else value_axis,
        "series": [opt],
    }, height=f"{height}px")


def pie(df: pl.DataFrame, cat: str, val: str, *, title: str = "", height: int = 360):
    """Доли. Жанр стека A; в отчёте на Plotly — та же величина полосой."""
    names = [str(k) for k in df[cat].to_list()]
    values = [float(v or 0) for v in df[val].to_list()]
    if _ENGINE == "plotly":
        import plotly.graph_objects as go
        fig = go.Figure(go.Pie(labels=names, values=values, hole=0.38,
                               sort=False, texttemplate="%{label}: %{value:,.0f}"))
        fig.update_layout(title=title)
        return _plotly_html(fig, height=height)

    _require("echarts", "круг")
    return _echarts_html({
        "title": {"text": title},
        "legend": {"orient": "vertical", "left": "right"},
        "series": [{"type": "pie", "radius": ["38%", "68%"],
                    "data": [{"name": n, "value": v} for n, v in zip(names, values)],
                    "label": {"formatter": "{b}: {c} ({d}%)"}}],
    }, height=f"{height}px")


def hist(df: pl.DataFrame, val: str, *, by: str | None = None, title: str = "",
         bins: int = 40, log_y: bool = False, height: int = 400):
    """Непрерывное распределение, при `by` — наложение выборок.

    Жанра нет в стеке A: у ECharts нет ни bins, ни overlay. Отчёт с этим
    жанром объявляет Plotly в setup."""
    _require("plotly", "распределение")
    import plotly.graph_objects as go
    fig = go.Figure()
    groups = df.partition_by(by, as_dict=True) if by else {(None,): df}
    for key, sub in groups.items():
        name = str(key[0]) if by else val
        fig.add_histogram(x=sub[val].to_numpy(), name=name, opacity=0.6,
                          nbinsx=bins)
    fig.update_layout(title=title, barmode="overlay",
                      xaxis_title=val, yaxis_title="строк",
                      yaxis_type="log" if log_y else "linear",
                      showlegend=by is not None)
    return _plotly_html(fig, height=height)


def tree(df: pl.DataFrame, *, ids: str, parents: str, values: str,
         labels: str | None = None, title: str = "", height: int = 470):
    """Иерархия одним следом (icicle). Жанра нет в стеке A."""
    _require("plotly", "иерархия")
    import plotly.graph_objects as go
    fig = go.Figure(go.Icicle(
        ids=df[ids].to_list(), parents=df[parents].to_list(),
        values=df[values].to_numpy(),
        labels=df[labels or ids].to_list(),
        branchvalues="total", tiling=dict(orientation="v"),
        textinfo="label+value",
    ))
    fig.update_layout(title=title)
    return _plotly_html(fig, height=height)


# --------------------------------------------------------------------------
# таблицы, карточки, форматы
# --------------------------------------------------------------------------

def col_widths(df: pl.DataFrame) -> dict[str, int]:
    """Ширина по СОДЕРЖИМОМУ, по медиане длины: одна аномально длинная ячейка
    иначе растягивает колонку на весь лист. Расчёт обязан трогать данные —
    он же исполняется дымовым прогоном вместо настоящей отрисовки."""
    out: dict[str, int] = {}
    for name in df.columns:
        lens = df[name].cast(pl.String, strict=False).str.len_chars()
        med = float(lens.median() or 0)
        need = max(len(name), med) * _PX_PER_CHAR + 24
        out[name] = int(min(max(need, _MIN_W), _MAX_W))
    total = sum(out.values())
    if total > _FIT_W:                      # горизонтального скролла быть не должно
        k = _FIT_W / total
        out = {n: max(_MIN_W, int(w * k)) for n, w in out.items()}
    return out


def react(df: pl.DataFrame, *, names: dict[str, str] | None = None, **kw):
    """Длинная витрина. Русские подписи приходят сюда, в данных — латиница."""
    widths = col_widths(df)
    cols = {c: rt.Column(name=(names or {}).get(c, c), min_width=widths[c])
            for c in df.columns}
    tbl = Reactable(df, columns=cols, searchable=df.height > 15,
                    sortable=True, class_="rp-rt", **kw)
    return tbl.to_widget()                  # сырой Reactable даёт пустую заглушку


def react_nested(outer: pl.DataFrame, key: str, child: pl.DataFrame, child_key: str,
                 *, names: dict[str, str] | None = None,
                 child_names: dict[str, str] | None = None,
                 groups=None, child_groups=None,
                 child_label: str = "состав", **kw):
    """Разворот строки: снаружи итог, внутри — из чего он сложился.

    Три вещи, каждая из которых стоила молчаливого дефекта.

    **Колбэк — замыкание на КОНКРЕТНУЮ пару кадров.** `RowInfo.row_index`
    отсчитывается внутри своего виджета. Один общий колбэк на несколько таблиц
    (вкладки, разрезы) берёт ключ из чужого кадра и выдаёт чужой состав.

    **Ключ — отдельная колонка, а не номер строки.** Номер позиции внутри
    документа повторяется от документа к документу; составной ключ собирается
    явно и прячется из показа.

    **Верхний ряд шапки нужен обеим таблицам.** Плоская таблица с группами
    колонок, переведённая на развороты, теряет их молча — и дюжина колонок
    снова читается одним рядом цифр.

    Проверяется это ТОЛЬКО полным рендером: дымовой прогон заглушает развороты
    целиком, чтобы не тянуть браузерный рантайм.
    """
    def _details_for(o: pl.DataFrame, c: pl.DataFrame):
        def _d(ri: RowInfo):
            k = o.get_column(key).to_list()[ri.row_index]
            sub = c.filter(pl.col(child_key) == k).drop(child_key, strict=False)
            if sub.is_empty():
                # Пустой разворот подписывается словами: пустое место читается
                # как «здесь ничего не требуется», а это другое утверждение.
                return HTML(f'<div class="rp-empty">— {child_label}: строк нет —</div>')
            w = col_widths(sub)
            cols = {n: rt.Column(name=(child_names or {}).get(n, n), min_width=w[n])
                    for n in sub.columns}
            inner = Reactable(sub, columns=cols, column_groups=child_groups,
                              sortable=True, outlined=True, class_="rp-rt rp-inner")
            return inner.to_widget()
        return _d

    widths = col_widths(outer)
    cols = {c: rt.Column(name=(names or {}).get(c, c), min_width=widths[c])
            for c in outer.columns}
    cols[key] = rt.Column(show=False)       # ключ разворота из показа убирается
    tbl = Reactable(outer, columns=cols, column_groups=groups,
                    details=_details_for(outer, child),
                    searchable=outer.height > 15, sortable=True,
                    class_="rp-rt rp-outer", **kw)
    return tbl.to_widget()


def gt_table(df: pl.DataFrame, *, title: str = "", subtitle: str = "",
             labels: dict[str, str] | None = None):
    """Короткая сводка, читается целиком."""
    gt = GT(df).tab_options(table_font_size="14px")
    if title:
        gt = gt.tab_header(title=title, subtitle=subtitle or None)
    if labels:
        gt = gt.cols_label(**labels)
    return gt


#: Разрядный разделитель — НЕРАЗРЫВНЫЙ пробел. Обычный пробел переносит хвост
#: числа на следующую строку, и «1 234» читается как два числа. Десятичная —
#: точка: пара «пробел + точка» однозначна, ни один знак нельзя принять
#: за другой. Отступление от ГОСТ объявлено вслух; меняется ЗДЕСЬ, а не в вызовах.
NBSP = "\u00a0"


def nfmt(x, dec: int = 0, *, drop_trailing_zeros: bool = False) -> str:
    """Число человеку: разряды неразрывным пробелом, десятичная точка — точка.

    Прочерк и ноль различаются: прочерк — «величина не наблюдалась», ноль —
    наблюдение. Подменять первое вторым запрещено.

    `drop_trailing_zeros` по умолчанию ВЫКЛЮЧЕН: «90.9000» рядом с «90.0096»
    в одной колонке читается как разная точность измерения, хотя это одна
    и та же величина. Резать хвост можно там, где величина стоит одна.
    """
    if x is None:
        return "—"
    s = f"{float(x):,.{dec}f}"
    whole, _, frac = s.partition(".")
    # Замена ТОЛЬКО в целой части. Применённая ко всей собранной строке, она
    # съедает запятые прозы: «по накладной  а не объём выполненного».
    whole = whole.replace(",", NBSP)
    if frac and drop_trailing_zeros:
        frac = frac.rstrip("0")
    return f"{whole}.{frac}" if frac else whole


def mfmt(x, unit: str = "₽") -> str:
    return "—" if x is None else f"{nfmt(x)} {unit}"


def gt_num(gt, cols, dec: int = 0):
    """Тот же канон для great_tables: движок форматирует числа сам.

    Ловушка порядка: общий форматтер, применённый ПОСЛЕДНИМ, переопределяет
    формат колонок, которые ему передали. Дробную колонку ему отдавать нельзя —
    расход 0.0112 напечатается как «0». Либо вызывать до частных `fmt_number`,
    либо передавать только целочисленные колонки.
    """
    if not cols:
        return gt
    return gt.fmt_number(columns=cols, decimals=dec, use_seps=True,
                         sep_mark=NBSP, dec_mark=".")


def cards(items: list[tuple[str, str, str]]):
    """(подпись, величина, знаменатель). Знаменатель печатается ПОД величиной,
    а не в подсказке: подсказка не попадает в распечатку."""
    from htmltools import div, span
    return div(*[
        div(span(cap, class_="rp-cap"), div(val, class_="rp-val"),
            div(den, class_="rp-den"), class_="rp-card")
        for cap, val, den in items
    ], class_="rp-cards")


def legend(items: list[tuple[str, str]]):
    from htmltools import div, span
    return div(*[
        span(span(style=f"background:{color}", class_="rp-dot"), text, class_="rp-leg")
        for text, color in items
    ], class_="rp-legend")


def show(*items):
    """Явная отрисовка. Автоматически показывается только последнее выражение
    ячейки, а из ветви `if` не показывается вовсе."""
    for it in items:
        _ipy_display(it)


def taglist(*items):
    return TagList(*items)
