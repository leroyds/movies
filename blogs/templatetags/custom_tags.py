from django.db.models import Avg
from django import template
from ..models import Post

register=template.Library()

@register.simple_tag
def get_avg_ratings(Pk):
    return Post.objects.get(pk=Pk).post_comment.filter(comment_status=True).aggregate(avg_rating=Avg('ratings'))