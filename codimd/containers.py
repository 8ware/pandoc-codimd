#! /usr/bin/env python3

from pandocfilters import toJSONFilter, RawInline

"""
Converts :::-containers to 'tcolorboxes' according to their category. Requires
the 'tcolorbox' package to be included, e. g. using the YAML header:

  ---
  header-includes:
    - \\usepackage{tcolorbox}
  ...

Currently containers can be embedded only with a single closing delimiter, e. g.

  :::info
  :::spoiler
  Foo bar
  :::

Note that the container delimiters are required to be surrounded by blanklines
in order to be parsed correctly by pandoc.

See also https://www.npmjs.com/package/markdown-it-container.
"""


colors = {
    'info':    '[colback=blue!5!white,colframe=blue!75!black]',
    'success': '[colback=green!5!white,colframe=green!75!black]',
    'warning': '[colback=yellow!5!white,colframe=yellow!75!black]',
    'danger':  '[colback=red!5!white,colframe=red!75!black]',
}

depth = 0


def containers(key, value, fmt, meta):
    global depth

    if key == 'Str':

        # PDFs are not interactive ...
        # (somehow [the first] spoiler has only two :)
        if '::spoiler' in value:
            return []

	# May require preprocessing since `::: info` is also valid
        if value in [ ':::info', ':::warning', ':::danger', ':::success' ]:
            depth += 1

            color = colors[value[3:]]
            return RawInline('latex', '\\begin{tcolorbox}'+color)

        if value == ':::':
            # Non-nested spoilers
            if not depth:
                return []

            closing = depth * [ RawInline('latex', '\\end{tcolorbox}') ]
            depth = 0

            return closing


if __name__ == "__main__":
    toJSONFilter(containers)

