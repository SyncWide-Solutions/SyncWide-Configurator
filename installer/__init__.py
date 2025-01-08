import os
import importlib

__all__ = []

for file in os.listdir(os.path.dirname(__file__)):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]
        globals()[module_name] = importlib.import_module(f".{module_name}", package="plugins")
        __all__.append(module_name)
