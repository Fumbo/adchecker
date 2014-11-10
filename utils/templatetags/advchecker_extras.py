from django import template

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