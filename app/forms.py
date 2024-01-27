from django import forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topics
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'