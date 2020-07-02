#! /usr/bin/env python3

from pandocfilters import toJSONFilter, Image
import re

"""
Translates CodiMD-specific image size information (`... =70%x`) to appropriate
key-value pairs.
"""

SIZESPEC_REGEX = re.compile('%20=(\d+%?)?x(\d+%?)?')


def resolve(key, value, keyvals):
    if not value:
        return

    keyvals.append([key, value])

def images(key, value, fmt, meta):
    if key == 'Image':
        [[ident, classes, keyvals], caption, [url, typef]] = value

        match = SIZESPEC_REGEX.search(url)
        if match:
            resolve('width', match.group(1), keyvals)
            resolve('height', match.group(2), keyvals)
            url = SIZESPEC_REGEX.sub('', url)

        return Image([ident, classes, keyvals], caption, [url, typef])


if __name__ == "__main__":
    toJSONFilter(images)

