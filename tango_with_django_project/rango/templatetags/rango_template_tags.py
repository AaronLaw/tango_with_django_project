from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
	return {'cats': Category.objects.all(), 
		'act_cat': cat}	 # We use parameterisation to highlight which category we are looking at when visiting its page. Note the inclusion of cat parameter to get_category_list() , which is optional - and if yu don't pass in a category, None is used as the subsequent value.
