from .pp_registry import pp_registry
from .preprocessors.scss import ScssPreprocessor

pp_registry.register(ScssPreprocessor)
