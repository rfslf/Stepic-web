from django.db import models
from django.contrib.auth.models import User

#class QuestionManager(models.Manager):
#    def new(self):
#        return self.filter(added_at = datetime.now())
#    def popular(self):
#        pop = self.order_by('rating')
#        return pop[0:5]

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
#    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='likes_set') 
    def __unicode__(self):
        return self.title
    def get_url(self):
        return reverse('question', kwargs={"id": self.id})
      
class Answer(models.Model):
    text = models.TextField()
#    added_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, default=1)

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    hidden = forms.CharField(widget=forms.HiddenInput())
    def clean(self):
        text = self.cleaned_data['text']
        if not text.is_valid():
            raise forms.ValidationError('question text is wrong', code=12)
        return text
    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question
