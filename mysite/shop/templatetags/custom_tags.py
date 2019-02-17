from django import template

register = template.Library()


@register.simple_tag
def my_slice(input):
    if len(input) > 35:
        return input[0:35] + "..."
    else:
        return input
