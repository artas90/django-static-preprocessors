from django.core.files.storage import FileSystemStorage
from django.conf import settings


class StaticFolderStorage(FileSystemStorage):
    """
    Standard file system storage for files STATIC_ROOT folder.
    """
    def __init__(self, location=None, base_url=None):
        if location is None:
            location = settings.STATIC_ROOT
        super(StaticFolderStorage, self).__init__(location, base_url)
