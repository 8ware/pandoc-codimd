#! /usr/bin/env python3

from pandocfilters import toJSONFilter, RawInline, elt, Str
from os import path
import re

"""
Replaces :emoji: strings by actual images.

Requires CodiMD's emoji images that can be obtained using the get-emojis.sh
script in 'scripts/'.
"""

MetaBool = elt('MetaBool', 1)

EMOJI_IMAGES = path.realpath(path.join(path.dirname(__file__), 'resources', 'emojis'))
EMOJI_REGEX = re.compile('^:(.+):$')


configured = False


def configure(meta):
    global configured

    if not configured:
        configured = True

        meta.update({ 'graphics': MetaBool(True) })

def latex_image(path):
    return RawInline('latex', '\\includegraphics[height=1.7ex]{' + path + '}')

def emojis(key, value, fmt, meta):
    if key == 'Str':
        match = EMOJI_REGEX.match(value)
        if match:
            configure(meta)

            name = match.group(1)
            image = path.join(EMOJI_IMAGES, name + '.png')

            if path.exists(image):
                return latex_image(image)


if not path.exists(EMOJI_IMAGES):
    raise Exception("You'll need to execute scripts/get-emojis.sh first!")


if __name__ == "__main__":
    toJSONFilter(emojis)

