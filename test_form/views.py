from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Question, Group, Choice


# Вывод список доступных групп
@login_required
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


# Запись ответа из формы в базу
@login_required
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



@login_required
def results(request, group_id):
    #return HttpResponse("RESULTS PAGE")

    #Достать questions, choies, user_choices и вывести результаты

    question_list = Question.objects.filter(group_id = group_id).order_by('id')

    template = loader.get_template('test_form/results.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))
    

@login_required
def authtest(request):
    result = "AUTH SUCCESS", "request.user=", request.user.id
    return HttpResponse(result)

"""    
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponse("success AUTH")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("AUTH TEST PAGE")
    

"""