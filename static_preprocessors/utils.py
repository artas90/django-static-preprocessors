# -*- coding: UTF-8 -*-
import re
import posixpath
import subprocess
from django.conf import settings


ANSI_ESCAPE_SEQUENCE = re.compile(r'\x1b[^m]*m')
ASCII_CONTROL_CHARACTERS = re.compile(r"[\x00-\x1F\x7F]")


def cleanup_output(out):
    out = ANSI_ESCAPE_SEQUENCE.sub('', out)
    out = ASCII_CONTROL_CHARACTERS.sub('', out)
    return out


def system_call(args, working_dir=settings.STATIC_ROOT, print_output=False, print_errors=False):

    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_dir)
    output, errors = p.communicate()
    output_clean = cleanup_output(output)
    errors_clean = cleanup_output(errors)

    output_or_errors = False

    if print_output and output_clean:
        print '---- out ----'
        print output
        output_or_errors = True

    if print_errors and errors_clean:
        print '---- errors ----'
        print errors
        output_or_errors = True

    if output_or_errors:
        print '--------'

    return output, errors


class URLConverter(object):
    'Based on code from github.com/andreyfedoseev/django-scss'

    URL_PATTERN = re.compile(r'url\(([^\)]+)\)')

    def __init__(self, content, source_url):
        self.content = content
        self.source_url = source_url

    def convert(self):
        return self.URL_PATTERN.sub(self._convert_url, self.content)

    def _convert_url(self, matchobj):
        url = matchobj.group(1)
        url = url.strip(' \'"')

        if url.startswith(('http://', 'https://', '/', 'data:')):
            return "url('%s')" % url

        full_url = posixpath.normpath('/'.join([posixpath.dirname(self.source_url), url]))
        full_url = posixpath.join(settings.STATIC_URL, full_url)

        return "url('%s')" % full_url
