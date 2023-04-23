from django import template
from store.models import Category


register = template.Library()

@register.inclusion_tag('giftzone/menu_content.html')
def menu_content():
    categories = Category.objects.all()
    return {'categories': categories}