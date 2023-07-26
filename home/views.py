# quiz_app/views.py
from django.shortcuts import render
# from .models import QuizQuestion
# from .forms import QuizForm

# def quiz_view(request):
#     if request.method == 'POST':
#         form = QuizForm(request.POST)
#         if form.is_valid():
#             selected_answer_id = form.cleaned_data['answer']
#             selected_answer = QuizAnswer.objects.get(pk=selected_answer_id)
#             is_correct = selected_answer.is_correct
#             # Implement your logic here to handle correct and incorrect answers
#     else:
#         question = QuizQuestion.objects.first()
#         form = QuizForm(question)
    
#     return render(request, 'home/quiz.html', {'form': form})

def quiz_view(request):
    return render(request, 'home/quiz.html')