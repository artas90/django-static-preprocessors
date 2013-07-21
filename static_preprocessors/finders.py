from django.contrib.staticfiles.finders import BaseStorageFinder
from .storages import StaticFolderStorage


class StaticFolderFinder(BaseStorageFinder):
    """
    A staticfiles finder that looks in STATIC_ROOT for compiled files.
    """
    storage = StaticFolderStorage

    def list(self, ignore_patterns):
        return []
