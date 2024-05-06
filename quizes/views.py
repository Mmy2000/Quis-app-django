from django.shortcuts import render
from .models import Quizes
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.

class QuizList(ListView):
    model = Quizes
    template_name = 'quizes/quizlist.html'

def quiz_detail(request , pk):
    quiz = Quizes.objects.get(pk=pk)
    return render(request , 'quizes/quiz_detail.html' , {'obj':quiz})

def quiz_data_view(request,pk):
    quiz = Quizes.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse({
        'data':questions ,
        'time': quiz.time
    })
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def save_quiz_view(request , pk):
    # print(request.POST)
    if is_ajax(request=request):
        data = request.POST
        data_ = dict(data.lists())
        print(data_)
        data_.pop('csrfmiddlewaretoken')
        print(data_)
    return JsonResponse({'text':'works'})