# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from ...pp_registry import pp_registry


class Command(BaseCommand):
    help = (
        "Apply all preprocessors for static files like scss, coffeescript, etc.\n"
        "Use it after 'collect_static' command."
    )

    def handle(self, *args, **options):
        pp_registry.post_collect_static()
