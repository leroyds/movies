from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.conf import settings

app_name = 'post'

urlpatterns = [
    path('',views.MovieList.as_view(),name='list'),
    path('post_key/<int:pk>/',views.MovieDetailView.as_view(),name='detail_pk'),
    url(r'^post/(?P<tag_slug>[-\w]+)/$',views.MovieList.as_view(),name='list_slug'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
