from django.shortcuts import render
from .questions import questions

user_answers = {}
x = set()

def start(request):
    return render(request, 'start.html')


def data(request):
    return render(request, 'data.html')


def q1(request):
    user_answers['fname'] = request.GET['fname']
    return render(request,'q1.html', questions)


def q2(request):
    user_answers['answ1'] = request.GET['answ1']
    return render(request, 'q2.html', questions)


def q3(request):
    user_answers['answ2'] = request.GET['answ2']
    return render(request, 'q3.html', questions)


def q4(request):
    user_answers['answ3'] = request.GET['answ3']
    return render(request, 'q4.html', questions)


def q5(request):
    x.add(request.POST['answ4']) 
    user_answers['answ4'] = x
    #user_answers['answ4'] = request.GET['answ4']
    return render(request, 'q5.html', questions)


def result(request):
    user_answers['answ5'] = request.GET['answ5']
    return render(request, 'result.html', itog(request)) 


def itog(request):
   i = 0
   if user_answers['answ1'] == questions['quest1']['ra']:
       i += 1
   if user_answers['answ2'] == questions['quest2']['ra']:
       i += 1
   if user_answers['answ3'] == questions['quest3']['ra']:
       i += 1
   if user_answers['answ4'] == questions['quest4']['ra']:
       i += 1
   if user_answers['answ5'] == questions['quest5']['ra']:
       i += 1
   if i <= 3:
       user_answers['phrase'] = user_answers['fname'] + ', у вас плохой результат! Количество правильных ответов:'
   elif i == 4:
       user_answers['phrase'] = user_answers['fname'] + ', у вас хороший результат! Количество правильных ответов:'
   elif i == 5:
       user_answers['phrase'] = user_answers['fname'] + ', у вас отличный результат! Количество правильных ответов:'
   user_answers['i'] = i
   itog = {'user_answers':user_answers, 'questions':questions}
   return itog
        