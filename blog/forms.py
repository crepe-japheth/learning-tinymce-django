""" from dataclasses import fields
from django import forms

from blog.models import Articles


class ArticlesForm(forms.ModelForm):

    post = forms.CharField(widget=forms.Textarea(attrs={'id':'richtext_field'}))

    class Meta:
        model = Articles
        fields = '__all__' """