from django import template

register = template.Library()


@register.simple_tag
def my_slice(input):
    if len(input) > 30:
        return input[0:30] + "..."
    else:
        return input
