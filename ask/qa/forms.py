
from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AskForm(forms.Form):
    title = forms.CharField()
    # title = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass 

    def save(self, user):
        question = models.Question(**self.cleaned_data)
        question.author = user
        question.save()
        return question
