from django.db import models

# Create your models here.

DIFF_CSOICES = (
        ('easy','easy'),
        ('meduim','meduim'),
        ('hard','hard'),
    )

class Quizes(models.Model):
    name = models.CharField( max_length=150)
    topic = models.CharField( max_length=150)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_scored_to_pass = models.IntegerField(help_text="required score to pass")
    diffculity = models.CharField( max_length=6 , choices=DIFF_CSOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_questions(self):
        return self.question_set.all()
    
    