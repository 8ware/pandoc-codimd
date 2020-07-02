
from os import path
import importlib

EXAMPLES = path.realpath(path.join(path.dirname(__file__), 'pandocfilters', 'examples'))

def load_module(name, module_dir):
    module_path = path.join(module_dir, name + '.py')
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

graphviz = load_module('graphviz', EXAMPLES).graphviz
plantuml = load_module('plantuml', EXAMPLES).plantuml

