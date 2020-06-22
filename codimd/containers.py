#! /usr/bin/env python3

from pandocfilters import toJSONFilter, RawInline, elt, Str

"""
Converts :::-containers to 'tcolorboxes' according to their category. Adds the
'tcolorbox' package to the 'header-includes' header automatically.

Currently containers can be embedded only with a single closing delimiter, e. g.

  :::info
  :::spoiler
  Foo bar
  :::

Note that the container delimiters are required to be surrounded by blanklines
in order to be parsed correctly by pandoc.

See also https://www.npmjs.com/package/markdown-it-container.
"""


MetaInlines = elt('MetaInlines', 1)
MetaList = elt('MetaList', 1)

DELIMITER = ':::'

colors = {
    'info':    '[colback=blue!5!white,colframe=blue!75!black]',
    'success': '[colback=green!5!white,colframe=green!75!black]',
    'warning': '[colback=yellow!5!white,colframe=yellow!75!black]',
    'danger':  '[colback=red!5!white,colframe=red!75!black]',
}

configured = False
depth = 0


def configure(meta):
    global configured

    if not configured:
        configured = True

        if 'header-includes' in meta:
            meta['header-includes']['c'].extend([
                MetaInlines([ RawInline('tex', '\\usepackage{tcolorbox}') ]),
            ])
        else:
            meta.update({ 'header-includes': MetaList([
                MetaInlines([ RawInline('tex', '\\usepackage{tcolorbox}') ]),
            ]) })

def containers(key, value, fmt, meta):
    global depth

    if key == 'Str':

        if value.startswith(DELIMITER):
            category = value[len (DELIMITER):]

            # PDFs are not interactive ...
            if category == 'spoiler':
                return []

            if category in [ 'info', 'warning', 'danger', 'success' ]:
                configure(meta)
                depth += 1

                color = colors[category]
                return RawInline('latex', '\\begin{tcolorbox}'+color)

            if not category:
                # Non-nested spoilers
                if not depth:
                    return []

                closing = depth * [ RawInline('latex', '\\end{tcolorbox}') ]
                depth = 0

                return closing


if __name__ == "__main__":
    toJSONFilter(containers)

