import os


class AlreadyRegistered(Exception):
    pass


class NotRegistered(Exception):
    pass


class PreprocessorRegistry(object):

    def __init__(self):
        self._registry = {}

    def process_path(self, source_url):
        path_dir, ext =  os.path.splitext(source_url)

        new_url = source_url
        for pp in self._registry.itervalues():
            if ext in pp.EXTENSIONS:
                new_url = pp.compile_url(source_url)
                break

        return new_url

    def post_collect_static(self):
        for pp in self._registry.itervalues():
            pp.post_collect_static()

    def register(self, model_or_instance):
        instance = self.__get_instance(model_or_instance)
        model_name = instance.__class__.__name__

        if model_name in self._registry:
            raise AlreadyRegistered('The model %s is already registered' % model_name)

        self._registry[model_name] = instance

    def unregister(self, model_or_instance):
        instance = self.__get_instance(model_or_instance)
        model_name = instance.__class__.__name__

        if model_name not in self._registry:
            raise NotRegistered('The model %s is not registered' % model_name)
        del self._registry[model_name]

    def __get_instance(self, model_or_instance):
        if isinstance(model_or_instance, type):
            return model_or_instance()
        else:
            return model_or_instance


_pp_registry = None

def get_pp_registry():
    global _pp_registry

    if _pp_registry is None:
        _pp_registry = PreprocessorRegistry()
        
        from .preprocessors.scss import ScssPreprocessor
        _pp_registry.register(ScssPreprocessor)

    return _pp_registry
