from django.db import models
from django.contrib.auth.models import User

#class QuestionManager():
#    def new:
#        return
#    def popular:
#        return

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set') 
#    objects=QuestionManager()
#    class Meta:
#        db_table = 'question'
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
#    question = models.OneToOneField(AnswerQuestion)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
#    class Meta:
#        db_table = 'answer'
