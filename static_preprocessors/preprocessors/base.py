from abc import ABCMeta, abstractmethod


class AbstractPreprocessor(object):
    __metaclass__ = ABCMeta

    EXTENSIONS = []

    @abstractmethod
    def compile_url(self, source_url):
        pass

    @abstractmethod
    def post_collect_static(self):
        pass
