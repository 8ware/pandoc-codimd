#! /usr/bin/env python3

from pandocfilters import toJSONFilter, Link

"""
Sanitizes internal cross references to match pandoc's 'auto_identifiers'
extension. In fact, the link targets are converted to lowercase and some
specially converted characters are replaced.
"""


def is_cross(ref):
    return ref[0] == '#'

def sanitize(ref):
    ref = ref.lower()

    # Replace characters that were specially translated by CodiMD
    ref = ref.replace('-amp-', '-') # & → amp

    return ref

def crossrefs(key, value, fmt, meta):
    if key == 'Link':
        attr, fmt, target = value

        ref, title = target
        if is_cross(ref):
            ref = sanitize(ref)
            target = [ ref, title ]

        return Link(attr, fmt, target)


if __name__ == "__main__":
    toJSONFilter(crossrefs)

