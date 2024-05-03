from django.db import models
from quizes.models import Quizes
# Create your models here.
class Question(models.Model):
    text = models.CharField( max_length=500)
    quiz = models.ForeignKey(Quizes , on_delete=models.CASCADE)
    created_at = models.DateField( auto_now_add=False)

    def __str__(self):
        return self.text
    
    def get_answer(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField( max_length=500)
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    created_at = models.DateField( auto_now_add=False)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    