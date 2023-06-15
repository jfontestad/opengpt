import tempfile
from functools import cached_property

from jcloud.flow import CloudFlow
from jinja2 import BaseLoader, Environment, FileSystemLoader


@cached_property
def flow_template(template):
    if template.endswith('.jinja2'):
        from open_gpt import __resources_path__

        env = Environment(loader=FileSystemLoader(__resources_path__))
        return env.get_template(template)
    else:
        return Environment(loader=BaseLoader()).from_string(template)


async def deploy(flow: str):
    import os

    if os.path.isfile(flow):
        return await CloudFlow(path=flow).deploy()
    else:
        with tempfile.NamedTemporaryFile() as f:
            with open(f.name, 'w') as _:
                _.write(flow)
            return await CloudFlow(path=f.name).deploy()
