
from django.shortcuts import render


def quiz_view(request):
    return render(request, 'home/quiz.html')