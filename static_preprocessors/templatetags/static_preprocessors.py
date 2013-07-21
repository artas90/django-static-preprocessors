from django import template
from django.templatetags.static import static as original_static
from ..pp_registry import pp_registry


register = template.Library()


@register.simple_tag
def static(path):
    """
    Joins the given path with the STATIC_URL setting
    and apply registered preprocessors like scss or coffee-script.

    Usage::

        {% static path %}

    Examples::

        {% static "myapp/css/base.css" %}
        {% static variable_with_path %}

    """

    new_path = pp_registry.process_path(path)
    return original_static(new_path)
