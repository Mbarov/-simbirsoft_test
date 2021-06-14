from django.shortcuts import render
from .questions import testdict, allchoises
from .services import QuizResultService
from .dto import AnswersDTO

list_answers = []
user_answers = {'list_answers' : list_answers}
user_data = {}
answers = AnswersDTO('1', user_answers)
testdict['answers'] = answers
testdict['user_data'] = user_data


def start(request):
    return render(request, 'start.html')


def data(request):
    return render(request, 'data.html')


def q1(request):
    user_data['fname'] = request.GET['fname']
    user_data['lname'] = request.GET['lname']
    user_data['age'] = request.GET['age']
    user_data['phone'] = request.GET['phone']
    user_data['post'] = request.GET['post']
    return render(request,'q1.html', testdict)


def q2(request):
    list_answers.append(request.GET['answ1'])
    return render(request, 'q2.html', testdict)



def q3(request):
    list_answers.append(request.GET['answ2'])
    return render(request, 'q3.html', testdict)


def q4(request):
    list_answers.append(request.GET['answ3'])
    return render(request, 'q4.html', testdict)


def q5(request):
    list_answers.append(request.GET['answ4'])
    return render(request, 'q5.html', testdict)
    

def finish(request):
    list_answers.append(request.GET['answ5'])
    return render(request,'finish.html',testdict)
    

test_case = QuizResultService(testdict['test'], answers)


def itog_message(i):
    i = int(i * 5)
    if i <= 3:
        user_data['phrase'] = user_data['fname'] + ', у вас плохой результат! Количество правильных ответов:' + str(i)
    elif i == 4:
        user_data['phrase'] = user_data['fname'] + ', у вас хороший результат! Количество правильных ответов:' + str(i)
    elif i == 5:
        user_data['phrase'] = user_data['fname'] + ', у вас отличный результат! Количество правильных ответов:' + str(i)
    namefolder = 'results/' + user_data['lname'] + '.txt'
    fout = open(namefolder, 'w', encoding='utf8')
    print(user_data['fname'], user_data['lname'], user_data['age'],user_data['post'], user_data['phone'], '\n' + 'Итоговый балл' , str(i), sep= ' ', file = fout)
    return testdict


def text_user_answers(answers_dto, quiz_dto):
    list_right_answers = []
    for x in range(5):
        for y in range(4):
            if  answers_dto.answers['list_answers'][x]  == quiz_dto.questions[x].choices[y].uuid:
                list_right_answers.append(quiz_dto.questions[x].choices[y].text)
    testdict['list_right_answers'] = list_right_answers
    return testdict


def result(request):
    otvet = test_case.get_result()
    testdict['otvet'] = otvet
    message = itog_message(otvet)
    testdict['message'] = message
    list_user_answers = text_user_answers(answers,testdict['test'])
    testdict['list_user_answers'] = list_user_answers
  
    return render(request,'result.html', testdict)
