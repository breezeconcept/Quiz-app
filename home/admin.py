from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Quiz)

class AnswerInline(admin.TabularInline):
    model = models.Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(models.Question, QuestionAdmin)

admin.site.register(models.Answer)

admin.site.register(models.Result)



