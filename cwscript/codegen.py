import sys

from jinja2 import Environment, PackageLoader, select_autoescape

this_module = sys.modules[__name__]

env = Environment(
    loader=PackageLoader(this_module),
    autoescape=select_autoescape()
)