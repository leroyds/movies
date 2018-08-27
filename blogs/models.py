from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Post(models.Model):
    POST_STATUS     ={('A','ACTIVE'),('D',"INACTIVE"),}
    title           = models.CharField(max_length=200)
    image           = models.ImageField(default='default.png',blank=True)
    slug            = models.SlugField(unique=True)
    description     = models.TextField(blank=True,default='')
    release_date    = models.DateTimeField(blank=True)
    language        = models.CharField(default='', max_length=100)
    created_date    = models.DateTimeField(auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)
    status          = models.CharField(default='A', max_length=50,choices=POST_STATUS)
    tags            = TaggableManager()
    

    def __str__(self):
        return self.title
    
    def TruncateStringTo50(self):
        return self.description[0:80]+"..."	
        
    def get_absolute_url(self):
        return reverse('post:detail_pk',kwargs={'pk':self.pk})

    class Meta:
        ordering = ('-created_date',)


class CommentManager(models.Manager):
    def get_comment_or_empty_comment_form(self,post,user):
        try:
            return Comment.objects.get(post_obj=post,user_obj=user)
        except Comment.DoesNotExist:
            return Comment.setComment(post_obj=post,user_obj=user)


class Comment(models.Model):
    post_obj        = models.ForeignKey(Post, related_name="post_comment", on_delete=models.CASCADE)
    user_obj        = models.ForeignKey(User,related_name='user_comment', on_delete=models.CASCADE)
    comment_title   = models.CharField(max_length=255)
    ratings         = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(10)])
    body            = models.TextField(default='')
    created_date    = models.DateTimeField( auto_now_add=True)
    updated_date    = models.DateTimeField(auto_now=True)
    comment_status  = models.BooleanField(default=True)
    objects         = CommentManager()
    
    @classmethod
    def setComment(self, post_obj,user_obj):
        return self(post_obj=post_obj, user_obj=user_obj)

    class Meta:
        ordering = ['-updated_date','-ratings']
        unique_together = ('post_obj','user_obj')
	
    def __str__(self):
        return 'Comment by {} on {}'.format(self.comment_title, self.post_obj)
