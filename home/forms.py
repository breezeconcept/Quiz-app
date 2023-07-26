
from django import forms

class QuizForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ChoiceField(choices=[(answer.id, answer.answer_text) for answer in question.quizanswer_set.all()])
