from django.shortcuts import render
from .models import Quizes
from django.views.generic import ListView
# Create your views here.

class QuizList(ListView):
    model = Quizes
    template_name = 'quizes/quizlist.html'