from django import template
from django.utils.importlib import import_module

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def add_class(field, css):
    field.field.widget.attrs.update({"class": css})
    return field


@register.filter
def add_placeholder(field, args=None):
    if not args:
        return field
    field.field.widget.attrs.update({"placeholder": args})
    return field


@register.filter
def is_inst(value, class_str):
    split = class_str.split('.')
    return isinstance(value, getattr(import_module('.'.join(split[:-1])), split[-1]))


@register.filter
def add_data_parsley_mincheck(field, args=None):
    if not args:
        return field
    field.field.widget.attrs.update({"data-parsley-mincheck": args})
    field.field.widget.attrs.update({"required": ''})
    return field
