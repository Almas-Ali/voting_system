from django import template


register = template.Library()


@register.filter(name='o')
def o():
    pass
