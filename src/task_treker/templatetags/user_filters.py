from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Код фильтра.

    Returns:
        фильтр addclass с параметром form-control.
    """
    return field.as_widget(attrs={'class': css})
