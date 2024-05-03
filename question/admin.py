from django.contrib import admin
from .models import Question , Answer
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
admin.site.register(Question)
admin.site.register(Answer)