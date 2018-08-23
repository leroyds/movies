from  django import forms
from . import models

class create_post(forms.ModelForm):
	class Meta:
		model=models.Post
		fields=['title','slug','description','release_date','language','tags','image']

class create_comment(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = ['comment_title','ratings','body']