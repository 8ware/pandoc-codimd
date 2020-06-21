#! /usr/bin/env python3

from pandocfilters import toJSONFilters
from codimd.containers import containers
from codimd.crossrefs import crossrefs


if __name__ == '__main__':
    toJSONFilters([ containers, crossrefs ])

