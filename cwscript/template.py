import os
from collections import defaultdict
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

this_dir = Path(os.path.dirname(__file__))
parent_dir = this_dir.parent.absolute()
templates_dir = os.path.join(parent_dir, "templates")
j_env = Environment(loader=FileSystemLoader(templates_dir))
templates = defaultdict(dict)

## load templates
for path in j_env.list_templates():
    slash_idx = path.find("/")
    domain = path[:slash_idx]
    name = path[slash_idx + 1 :]
    templates[domain][name] = j_env.get_template(path)

codegen_templates = templates["codegen"]
contract_crate_templates = templates["contract_crate"]


def render_to_file(template, path, **args):
    with open(path, "w") as file:
        file.write(template.render(**args))
