# quiz_app/models.py
from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
