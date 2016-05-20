from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def new(self):
        return self.filter(added_at = datetime.now())
    def popular(self):
        pop = self.order_by('rating')
        return pop.[0:5]

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
#    added_at = models.DateField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set') 
    objects = QuestionManager()
#    class Meta:
#        db_table = 'question'
        
class Answer(models.Model):
    text = models.TextField()
#    added_at = models.DateField(auto_now_add=True)
    added_at = models.DateField()
#    question = models.OneToOneField(AnswerQuestion)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
#   class Meta:
#       db_table = 'answer'
