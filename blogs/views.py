from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.db.models import Count 
from taggit.models import Tag


from . import models


class MovieList(ListView):
    model = models.Post
    paginate_by=6
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        tag=None
        tag=self.kwargs.get('tag_slug')
        print(tag)
        if tag:
            tag=get_object_or_404(Tag,slug=tag)
            context['post_list']=self.model.objects.filter(tags__in=[tag])
        else:
            context['post_list']= self.model.objects.all()
        return context



class MovieDetailView(DetailView):
    model = models.Post

    def get_object(self):
        pk=self.kwargs.get('pk')
        return get_object_or_404(models.Post,id=pk)

   
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post_Info=get_object_or_404(models.Post,id=self.kwargs.get('pk'))
        context['comments']=post_Info.post_comment.all().filter(comment_status=True)
        #context['comment_added']=
        
        post_tag_related_id=post_Info.tags.values_list('id',flat=True)
        related_blogs=self.model.objects.filter(tags__in=post_tag_related_id).exclude(id=post_Info.pk)
        related_blogs=related_blogs.annotate(same_count=Count('tags')).order_by('-same_count','-created_date')
        context['related_blogs']=related_blogs
        return context
        
