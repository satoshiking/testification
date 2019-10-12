from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Question, Group, Choice, User_choice


#Вывод списка доступных тем для тестирования
@login_required
def index(request):
    group_list = Group.objects.all()

    question_list = []
    for group in group_list:
        question_first = Question.objects.filter(group_id = group).order_by('id').first()
        question_list.append([group.group_text, question_first.id])

    template = loader.get_template('test_form/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))

#Вывод 1 вопроса
@login_required
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    choice_list = Choice.objects.filter(question_id=question.id)
    template = loader.get_template('test_form/detail.html')
    context = {
              'question': question,
              'choice_list': choice_list,
              }
    return HttpResponse(template.render(context, request))


#Запись ответа из формы в базу
@login_required
def answer(request, question_id):
    
    #Сохраняем ответ пользователя в базу методом update_or_create
    choice_list = Choice.objects.filter(question_id=question_id)
    
    for choice in choice_list:
        checkbox_name = "choice" + str(choice.id)
        if checkbox_name in request.POST:
            checked = True
        else:
            checked = False
        record = User_choice.objects.update_or_create(user=request.user, choice=choice, defaults={'checked':checked})

    #Определяем слеюующую страницу
    question = get_object_or_404(Question, pk=question_id)
    group = question.group
    question_next = Question.objects.filter(group_id = group).order_by('id')
    question_list = question_next.filter(id__gt=question_id)

    #Закончились вопросы в группе -> к результатам
    if (len(question_list) == 0):        
        return HttpResponseRedirect( reverse('test_form:results', args = (group.id,)) )
    #Иначе смотрим следующий вопрос
    else:
        question_next = question_list[0]
        return HttpResponseRedirect( reverse('test_form:detail', args = (question_next.id,)) )



#Выводим результаты тестирования 
@login_required
def results(request, group_id):
    question_list = Question.objects.filter(group_id = group_id).order_by('id')
    answer_list = []

    for question in question_list:
        choice_list = Choice.objects.filter(question_id=question.id)

        answer = False
        for choice in choice_list:
            user_answer = User_choice.objects.get(user=request.user, choice=choice)

            if (user_answer.checked == choice.right):
                answer = True
            else:
                answer = False
                break
        answer_list.append([question.question_text, answer])

    #Количество правильных/неправильных ответов
    right_answers = 0
    wrong_answers = 0

    for answer in answer_list:
        if answer[1]:
            right_answers += 1
        else:
            wrong_answers += 1
    percent_answers = int(100 * right_answers / (right_answers + wrong_answers))


    template = loader.get_template('test_form/results.html')
    context = {
        'answer_list': answer_list,
        'right_answers': right_answers,
        'wrong_answers': wrong_answers,
        'percent_answers': percent_answers,
    }
    return HttpResponse(template.render(context, request))
