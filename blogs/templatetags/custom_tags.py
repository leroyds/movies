from django.db.models import Avg
from django import template
from ..models import Post

register=template.Library()

@register.simple_tag(name='AVERAGE_RATINGS')
def get_avg_ratings(pk):
    return Post.objects.get(pk=pk).post_comment.filter(comment_status=True).aggregate(avg_rating=Avg('ratings'))