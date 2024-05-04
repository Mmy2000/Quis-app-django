from django.shortcuts import render
from .models import Quizes
from django.views.generic import ListView
# Create your views here.

class QuizList(ListView):
    model = Quizes
    template_name = 'quizes/quizlist.html'

def quiz_detail(request , pk):
    quiz = Quizes.objects.get(pk=pk)
    return render(request , 'quizes/quiz_detail.html' , {'quiz':quiz})