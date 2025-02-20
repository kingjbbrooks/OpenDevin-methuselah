from abc import ABC, abstractmethod
from typing import Dict, Tuple

from opendevin.runtime.sandbox.plugins.mixin import PluginMixin
from opendevin.runtime.sandbox.process import Process


class Sandbox(ABC, PluginMixin):
    background_commands: Dict[int, Process] = {}

    @abstractmethod
    def execute(self, cmd: str) -> Tuple[int, str]:
        pass

    @abstractmethod
    def execute_in_background(self, cmd: str) -> Process:
        pass

    @abstractmethod
    def kill_background(self, id: int) -> Process:
        pass

    @abstractmethod
    def read_logs(self, id: int) -> str:
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def copy_to(self, host_src: str, sandbox_dest: str, recursive: bool = False):
        pass

    @abstractmethod
    def get_working_directory(self):
        pass
