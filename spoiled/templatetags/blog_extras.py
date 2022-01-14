from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html


get_user_model = get_user_model()
register = template.Library()


@register.simple_tag(name="owner_check_edit")
def owner_check_edit(owner, current_user, spoiled_id):
    if not isinstance(owner, get_user_model):
        return ""
    if owner == current_user:
        return format_html("<a href='spoiled/{}/delete'>Delete </a><a href='spoiled/{}/update'>Update</a>", spoiled_id, spoiled_id)
