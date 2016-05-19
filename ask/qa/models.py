from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField
    added_at = models.DateTimeField
    rating = models.IntegerField
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set') 
class Answer(models.Model):
    text = models.TextField
    added_at = models.DateTimeField
    question = models.OneToOneField(AnswerQuestion)
    author = models.ForeignKey(User)
# Create your models here.
