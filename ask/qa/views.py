from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def allq(request):
    all_question = Question.objects.filter(is_published=True)
    all_questions = Question.objects.order_by('-id')
    page = request.GET.get('page', 1)
#    limit = request.GET.get('limit', 10)
    paginator = Paginator(all_question, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return HttpResponse('NOK')
#    return render(request, 'qa/question.html', {
#        'question' : page.object_list,
#        'paginator': paginator, 'page' = page,
#         })

def popular(request):
    pops=Question.objects.order_by('rating')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_question, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return HttpResponse('POK')
#    return render(request, 'qa/question.html', {
#        'question' : page.object_list,
#        'paginator': paginator, 'page' = page,
#         })
    
def show_question(request, q_id):
    try:
        question = Question.objects.get(id = q_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'qa/question.html', {
        'question' : question,
#        'answer' : ,
        'title' : question.title,
        'text' : question.text,
        })
