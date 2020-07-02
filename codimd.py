#! /usr/bin/env python3

from pandocfilters import toJSONFilters
from codimd.containers import containers
from codimd.crossrefs import crossrefs
from codimd.emojis import emojis
from codimd.images import images

import sys
from os import path
sys.path.insert(0, path.realpath(path.join(path.dirname(__file__), 'pandocfilters', 'examples')))
from graphviz import graphviz
from plantuml import plantuml
del sys.path[0]


if __name__ == '__main__':
    toJSONFilters([ containers, crossrefs, emojis, images, graphviz, plantuml ])

