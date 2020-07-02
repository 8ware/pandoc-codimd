#! /usr/bin/env python3

from pandocfilters import toJSONFilters
from codimd.containers import containers
from codimd.crossrefs import crossrefs
from codimd.emojis import emojis
from codimd.images import images


if __name__ == '__main__':
    toJSONFilters([ containers, crossrefs, emojis, images ])

