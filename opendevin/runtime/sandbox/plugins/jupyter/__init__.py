import os
from dataclasses import dataclass

from opendevin.runtime.sandbox.plugins.requirement import PluginRequirement


@dataclass
class JupyterRequirement(PluginRequirement):
    name: str = 'jupyter'
    host_src: str = os.path.dirname(
        os.path.abspath(__file__)
    )  # The directory of this file (sandbox/plugins/jupyter)
    sandbox_dest: str = '/opendevin/plugins/jupyter'
    bash_script_path: str = 'setup.sh'
