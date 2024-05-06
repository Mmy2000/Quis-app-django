from django.urls import path
from . import views

app_name = "quizes"
urlpatterns = [
    path('' , views.QuizList.as_view() , name="QuizList"),
    path('<pk>/' , views.quiz_detail , name="quiz_detail"),
    path('<pk>/save/' , views.save_quiz_view , name="save_quiz"),
    path('<pk>/data/' , views.quiz_data_view , name="quiz_data_view"),
]
