from django.db.models import Avg
from django import template
from ..models import Post

register=template.Library()

@register.simple_tag(name='TotalPosts')
def PostCount():
    return Post.objects.count()

@register.simple_tag(name='AVERAGE_RATINGS')
def get_avg_ratings(pk):
    return Post.objects.get(pk=pk).post_comment.filter(comment_status=True).aggregate(avg_rating=Avg('ratings'))


@register.inclusion_tag("blogs/latest_posts.html")
def most_recent_added_movies(count=5):
    latest_posts= Post.objects.all().order_by('-created_date')[:count]
    return {'latest_posts':latest_posts}
