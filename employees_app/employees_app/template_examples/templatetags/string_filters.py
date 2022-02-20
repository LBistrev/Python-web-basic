from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    Capitalizes the value, i. e. make first letter Capital and rest lower

    * THIS is TExt => This is text
    """
    return value[0].upper() + value[1:].lower()
