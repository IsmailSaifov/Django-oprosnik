from django.contrib import admin
from . import models
from .models import Response,Choice,Question, MainQuestion
# Register your models here.


@admin.register(Question)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question_text','only_text','requires_text_response','question_main')  # Поля, которые будут отображаться в списке объектов

@admin.register(Choice)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text',)  # Поля, которые будут отображаться в списке объектов

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_main',  'choice', 'text_response','cr_date','ip_address')

admin.site.register(MainQuestion)