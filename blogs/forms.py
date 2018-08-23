from  django import forms
from . import models
from django.contrib.auth.models import User


class create_post(forms.ModelForm):
	class Meta:
		model=models.Post
		fields=['title','slug','description','release_date','language','tags','image']

class create_comment(forms.ModelForm):
	post_obj=forms.ModelChoiceField(
		widget=forms.HiddenInput,
		disabled=True,
		queryset=models.Post.objects.all()
	)
	user_obj=forms.ModelChoiceFields(
		widget=forms.HiddenInput,
		disabled=True,
		queryset=User.objects.all()
	)
	class Meta:
		model = models.Comment
		fields = ['post_obj','user_obj','comment_title','ratings','body']