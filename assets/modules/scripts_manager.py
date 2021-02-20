import importlib
import importlib.util
import inspect
import os
from scripts import scripts


class ScriptObject:
    def __init__(self, path=None, maindef=None):
        self.path = path
        self.maindef = maindef
        self.directory = os.path.dirname(self.path)

    def _start_from_path(self):
        os.system(f"python3 {self.path}")

    def start(self):
        os.chdir(self.directory)

        if self.maindef is not None:
            self.maindef()
        else:
            self._start_from_path()


def get_script(choice, path) -> ScriptObject:
    for script_dict in scripts:
        exhaust_dir = os.path.dirname(path)

        script_path = os.path.join(
            exhaust_dir,
            script_dict["path"]
        )

        if choice == script_dict["alias"]:
            if script_dict.get("def"):
                name = script_path.split("/")[-1]

                spec = importlib.util.spec_from_file_location(
                    name, script_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for def_name, function in \
                        inspect.getmembers(module, inspect.isfunction):
                    if def_name == script_dict["def"]:
                        return ScriptObject(
                            path=script_path,
                            maindef=function
                        )

            else:
                return ScriptObject(
                    path=script_path
                )
