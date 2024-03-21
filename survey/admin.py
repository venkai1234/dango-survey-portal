
from django.contrib import admin
import nested_admin
from .models import Survey, Question, Choice


class ChoiceInLine(nested_admin.NestedTabularInline):

    model = Choice
    extra = 2
    classes = ['collapse']


class QuestionInLine(nested_admin.NestedTabularInline):

    model = Question
    extra = 1
    classes = ['collapse']
    inlines = [ChoiceInLine]


class SurveyAdmin(nested_admin.NestedModelAdmin):

    fieldsets = [
        ('Survey Name', {'fields': ['name']}),
        ('When would you like to publish it?', {'fields': ['published_on'], 'classes': ['collapse']})
    ]
    inlines = [QuestionInLine]
    list_filter = ['published_on']
    search_fields = ['name']



admin.site.register(Survey, SurveyAdmin)
