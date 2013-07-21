from django.conf import settings


STATIC_PP_AUTO_BUILD = getattr(settings, "STATIC_PP_AUTO_BUILD", False)

STATIC_PP_SCSS_EXECUTABLE = getattr(settings, "STATIC_PP_SCSS_EXECUTABLE", 'scss')
STATIC_PP_COMPASS_EXECUTABLE = getattr(settings, "STATIC_PP_COMPASS_EXECUTABLE", 'compass')
STATIC_PP_SCSS_DEBUG_INFO = getattr(settings, "STATIC_PP_SCSS_DEBUG_INFO", False)
