from django import template
from sweets.models import Category

register = template.Library()


@register.inclusion_tag('sweets/menu_tpl.html')
def menu_category(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}