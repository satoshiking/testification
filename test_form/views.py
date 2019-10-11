from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader

from .models import Question, Group, Choice

# Вывод список доступных групп
def index(request):
    group_list = Group.objects.all()

    group_id_list = []
    question_id_list = []
    for group in group_list:
        group_id_list.append(group.id)

        question_first = Question.objects.filter(group_id = group).order_by('id').first()
        question_id_list.append(question_first)


    template = loader.get_template('test_form/index.html')
    context = {
        'group_list': group_list,
        'question_id_list': question_id_list,
    }
    return HttpResponse(template.render(context, request))

# Вывод 1 вопроса
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_list = Choice.objects.filter(question_id=question.id)
    template = loader.get_template('test_form/detail.html')
    context = {
              'question': question,
              'choice_list': choice_list,
              }
    return HttpResponse(template.render(context, request))


# Запись ответа из формы в базу
def answer(request, question_id):

    # Сохранить ответ пользователя в базу.

    question = Question.objects.get(pk=question_id)
    group = question.group
    question_next = Question.objects.filter(group_id = group).order_by('id')
    question_list = question_next.filter(id__gt=question_id)

    #Закончились вопросы в группе-> к результатам. Иначе смотрим следующий вопрос
    if (len(question_list) == 0):        
        return HttpResponseRedirect( reverse('test_form:results', args = (group.id,)) )
    else:
        question_next = question_list[0]
        return HttpResponseRedirect( reverse('test_form:detail', args = (question_next.id,)) )

#    question = get_object_or_404(Questions, pk=question_id)
#    return render(request, 'test_form/testing.html', {'group_text': group_text})




def results(request, group_id):
    #return HttpResponse("RESULTS PAGE")

    #Достать questions, choies, user_choices и вывести результаты

    question_list = Question.objects.filter(group_id = group_id).order_by('id')

    template = loader.get_template('test_form/results.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))
    
