from .models import *

from django import forms




class BlogForm(forms.ModelForm):
	bloguser = forms.CharField(widget=forms.HiddenInput())
	date = forms.CharField(widget=forms.HiddenInput())
	
	class Meta:
		model=BlogEdit
		fields="__all__"