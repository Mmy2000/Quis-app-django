from django.db import models
from django.contrib.auth.models import User
from quizes.models import Quizes
# Create your models here.
class Result(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quizes,  on_delete=models.CASCADE)
    score = models.FloatField()


    def __str__(self):
        return str(self.pk)
    