
from django import forms
from . import models
from models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AskForm(forms.Form):
    title = forms.CharField()
    # title = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
#    def clean(self):
#        pass 
#    def save(self, user):
    def save(self):
        question = Question(**self.cleaned_data)
#        question.author = user
        question.author_id = 1
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        pass 

    def save(self, user):
        text = self.cleaned_data['text']
        question = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(text=text, question=question)
        answer.author = user
        answer.save()
        return answer
