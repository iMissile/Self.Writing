/**
 * Low-level diff primitives for the canvas SDK.
 *
 * The canvas diff surface is intentionally minimal — two components that
 * compose with the generic `Card` / `CardHeader` / `CardBody` / `Pill` /
 * `Text` primitives to build any diff layout an agent can imagine:
 *
 * - `DiffView` — a monospaced unified diff renderer: a plain diff body
 *   with added / removed / unchanged line tints, a line-number gutter, and
 *   an accent strip. Drops into any container (a `Card`, a table cell, a
 *   bare layout, nothing at all). No card chrome, no header, no path
 *   display.
 *
 * - `DiffStats` — the canonical `+N` green / `-N` red glyph pair. Use
 *   it anywhere a small "added/deleted" summary makes sense — in a
 *   `CardHeader`'s `trailing` slot, next to a filename in a file tree,
 *   inside a status row, etc.
 *
 * For file-level metadata the preferred composition is to use the
 * generic `Card` family:
 *
 * ```tsx
 * <Card collapsible>
 *   <CardHeader trailing={<DiffStats additions={5} deletions={2} />}>
 *     src/utils.ts
 *   </CardHeader>
 *   <CardBody style={{ padding: 0 }}>
 *     <DiffView path="src/utils.ts" lines={lines} />
 *   </CardBody>
 * </Card>
 * ```
 */
import type { CSSProperties, JSX } from "react";
export type DiffStatsProps = {
    additions?: number;
    deletions?: number;
    style?: CSSProperties;
};
/**
 * Inline `+N` / `-N` glyph pair. Green additions, red deletions, with
 * tabular numerals so columns of stats line up. Renders nothing when
 * both counts are zero.
 *
 * @example
 * ```tsx
 * <CardHeader trailing={<DiffStats additions={12} deletions={3} />}>
 *   src/utils.ts
 * </CardHeader>
 *
 * <Row gap={8}>
 *   <Text>Refactor pass</Text>
 *   <DiffStats additions={42} deletions={17} />
 * </Row>
 * ```
 */
export declare function DiffStats({ additions, deletions, style, }: DiffStatsProps): JSX.Element | null;
export type DiffLineType = "added" | "removed" | "unchanged";
export type DiffLineData = {
    type: DiffLineType;
    content: string;
    lineNumber?: number;
};
export type DiffViewProps = {
    lines?: DiffLineData[];
    /**
     * The file the diff is of (e.g. `"src/utils.ts"`). Accepted so a page
     * can state it beside the lines; the body renders the same with or
     * without it.
     */
    path?: string;
    /**
     * The language of the diffed code (e.g. `"typescript"`). Accepted and
     * ignored: the body renders as plain monospaced text in every language.
     */
    language?: string;
    /** Show line numbers in the gutter. Default `true`. */
    showLineNumbers?: boolean;
    /** Color line numbers green/red for added/removed lines. Default `true`. */
    coloredLineNumbers?: boolean;
    /** Show a 3px accent strip on the left edge for changed lines. Default `true`. */
    showAccentStrip?: boolean;
    style?: CSSProperties;
};
/**
 * Unified diff body renderer: a plain preformatted body with monospaced
 * type, colored line backgrounds, a line-number gutter, and an accent
 * strip.
 *
 * `DiffView` does not provide any surrounding chrome — place it inside
 * a `Card` + `CardBody` (with `padding: 0`) when you want the standard
 * bordered "file diff" look, or drop it anywhere else if you want the
 * bare renderer.
 *
 * @example
 * ```tsx
 * <Card>
 *   <CardHeader trailing={<DiffStats additions={2} deletions={1} />}>
 *     src/utils.ts
 *   </CardHeader>
 *   <CardBody style={{ padding: 0 }}>
 *     <DiffView
 *       path="src/utils.ts"
 *       lines={[
 *         { type: "unchanged", content: "export function add(a: number, b: number): number {", lineNumber: 1 },
 *         { type: "removed",   content: "  return a + b;", lineNumber: 2 },
 *         { type: "added",     content: "  const result = a + b;", lineNumber: 2 },
 *         { type: "added",     content: "  return result;", lineNumber: 3 },
 *         { type: "unchanged", content: "}", lineNumber: 4 },
 *       ]}
 *     />
 *   </CardBody>
 * </Card>
 * ```
 */
export declare function DiffView({ lines, showLineNumbers, coloredLineNumbers, showAccentStrip, style, }: DiffViewProps): JSX.Element;
//# sourceMappingURL=diff-view.d.ts.map