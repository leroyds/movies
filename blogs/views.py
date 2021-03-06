from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.db.models import Count 
from taggit.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import create_comment
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from . import models


class MovieList(ListView):
    paginate_by=3
    model = models.Post

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        tag=None
        tag=self.kwargs.get('tag_slug')
        if tag:
            tag=get_object_or_404(Tag,slug=tag)
            context['post_list']=self.model.objects.filter(tags__in=[tag])
        else:
            context['post_list']= self.model.objects.all()

        ############## Pagination block 
        paginating=Paginator(context['post_list'],3)
        page=self.request.GET.get('page')
        try:
            context['post_list']=paginating.page(page)
        except PageNotAnInteger:
            context['post_list']=paginating.page(1)
        except EmptyPage:
            context['post_list']=paginating.page(paginating.num_pages)
        ############################
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

        if self.request.user.is_authenticated:
            commentFormInfo = models.Comment.objects.get_comment_or_empty_comment_form(
                post=post_Info,
                user=self.request.user)
            if commentFormInfo.id:
                comment_form_url = reverse(
                    'post:UpdateComment',
                    kwargs={
                        'movie_id': commentFormInfo.post_obj.id,
                        'pk': commentFormInfo.id
                        })
            else:
                comment_form_url = reverse(
                        'post:CreateComment',
                        kwargs={
                            'movie_id': self.object.id,
                            }
                    )
            
            comment_form = create_comment(instance=commentFormInfo)
            context['comment_form'] = comment_form
            context['comment_form_url'] = comment_form_url
        return context


class CreateCommentView(LoginRequiredMixin,CreateView):
    form_class=create_comment

    def get_initial(self):
         initial=super().get_initial()
         initial['user_obj']=self.request.user.id
         initial['post_obj']=self.kwargs['movie_id']
         return initial

    def render_to_response(self,context,**kwargs):
        # import pdb
        # pdb.set_trace()
        movie_id=int(context['form']['post_obj'].value().__str__())
        movie_detail_url=reverse('post:detail_pk', kwargs={'pk':movie_id})
        return redirect(to=movie_detail_url)

    def get_success_url(self):
        movie_id = self.object.post_obj.id 
        return reverse('post:detail_pk', kwargs={'pk':movie_id})


class UpdateCommentView(LoginRequiredMixin,UpdateView):
    form_class=create_comment
    queryset = models.Comment.objects.all()

    def get_object(self,Queryset=None):
        CommentInfo=super().get_object(Queryset)
        if CommentInfo.user_obj!=self.request.user:
            raise PermissionDenied("cannot modify other user's comment")
        return CommentInfo

    def render_to_response(self,context,**kwargs):
        print(context)
        movie_id=context['object'].id 
        movie_detail_url=reverse('post:detail_pk',kwargs={'pk':movie_id})
        return redirect(to=movie_detail_url)

    def get_success_url(self):
        movie_id=self.object.post_obj.id
        return reverse('post:detail_pk',kwargs={'pk':movie_id})



