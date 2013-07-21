# -*- coding: UTF-8 -*-
import os
from itertools import repeat, chain, ifilter
from django.contrib.staticfiles import finders
from django.conf import settings
from .base import AbstractPreprocessor
from ..utils import system_call, URLConverter
from ..finders import StaticFolderFinder
from ..settings import STATIC_PP_SCSS_EXECUTABLE, STATIC_PP_COMPASS_EXECUTABLE, \
    STATIC_PP_SCSS_DEBUG_INFO, STATIC_PP_AUTO_BUILD


class ScssPreprocessor(AbstractPreprocessor):
    EXTENSIONS = ['.scss']

    _PATHS_CACHE = None

    def compile_url(self, source_url):
        base_path, ext =  os.path.splitext(source_url)
        new_url = base_path + '.css'

        if not STATIC_PP_AUTO_BUILD:
            return new_url

        self._init_paths_cache()

        input_path = finders.find(source_url)
        output_path = os.path.join(settings.STATIC_ROOT, base_path) + '.css'

        compile_scss = [STATIC_PP_SCSS_EXECUTABLE, '--compass']
        if STATIC_PP_SCSS_DEBUG_INFO:
            compile_scss += ['--debug-info']
        compile_scss += ['--style', 'expanded'] + self._PATHS_CACHE + [input_path]

        output_directory = os.path.dirname(output_path)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print "Compile scss: '%s'" % source_url
        output, errors = system_call(compile_scss, print_errors=True)

        with open(output_path, 'w+') as f:
            compiled_css = URLConverter(
                output.decode(settings.FILE_CHARSET),
                source_url
            ).convert()

            f.write(compiled_css.encode(settings.FILE_CHARSET))

        return new_url

    def post_collect_static(self):
        compass_compile = [
            STATIC_PP_COMPASS_EXECUTABLE, 'compile',
            '--sass-dir', settings.STATIC_ROOT, '--css-dir', settings.STATIC_ROOT
        ]

        print "Compile scss files.."
        system_call(compass_compile, print_output=True, print_errors=True)

    def _init_paths_cache(self):
        if not self._PATHS_CACHE:
            finders_ = (finder for finder in finders.get_finders() if not isinstance(finder, StaticFolderFinder))

            for finder in finders_:
                if hasattr(finder, 'storages'):
                    paths = (storage.location for storage in finder.storages.itervalues())
                    paths = ifilter(lambda p: os.path.os.path.exists(p), paths)
                    paths = chain(*zip(repeat('-I'), paths))
                    self._PATHS_CACHE = list(paths)
