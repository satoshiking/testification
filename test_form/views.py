from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question, Group


def index(request):    

    # - Начать тестирование выбранной группы
    #   Вывести список доступных групп с вопросами
    
    group_list = Group.objects.all()
    template = loader.get_template('test_form/index.html')
    context = {
        'group_list': group_list,
    }
    return HttpResponse(template.render(context, request))


def testing(request, group_id):
    question_list = Question.objects.all().filter(group_id=group_id)
    template = loader.get_template('test_form/testing.html')
    context = {
              'question_list': question_list,
              'group_id': group_id,
              }
    return HttpResponse(template.render(context, request))

    #return HttpResponse("Hello, world. You're at the polls index.")

#    question = get_object_or_404(Questions, pk=question_id)
#    return render(request, 'test_form/testing.html', {'group_text': group_text})


    

def results(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    
    #Логика выборки пройденных тестов.
    question_list = Question.objects.all()


    template = loader.get_template('test_form/results.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))
    
