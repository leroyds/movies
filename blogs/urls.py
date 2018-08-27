from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

app_name = 'post'

urlpatterns = [
    path('post_key/<int:pk>/',views.MovieDetailView.as_view(),name='detail_pk'),
    url(r'^post/(?P<tag_slug>[-\w]+)/$',views.MovieList.as_view(),name='list_slug'),
    path('',views.MovieList.as_view(),name='list'),
    url(r'post_key/(?P<movie_id>[\d]+)/comment/$',views.CreateCommentView.as_view(),name='CreateComment'),
    url(r'post_key/(?P<movie_id>[\d]+)/comment/(?P<pk>[\d]+)/$',views.UpdateCommentView.as_view(),name='UpdateComment'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
