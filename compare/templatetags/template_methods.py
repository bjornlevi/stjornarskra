from django import template

register = template.Library()

@register.simple_tag
def matches(obj, other):
	if Match.objects.get(stjornarskra=obj,frumvarp=other):
		return True
	return False