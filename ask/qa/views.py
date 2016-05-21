from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

def test(request, *args, **kwargs):
    return HttpResponse('OK')
# Create your views here.
def allq(request):

def popular(request):  

def show_question(request, q_id):
    try:
        question = Question.objects.get(id = q_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'ask/question.html', {
        'question' : question,
        'title' : question.title,
        'text' : question.text,
         })
