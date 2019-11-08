from django.contrib import admin

from .models import Question, Choice, Group

class ChoiceInline(admin.TabularInline):
    model = Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'group')
    list_filter = ('group',)
    inlines = [ChoiceInline, ]


#@admin.register(Choice)
#class ChoiceAdmin(admin.ModelAdmin):
#	list_display = ('choice_text', 'question', 'right')
#	list_filter = ('question', 'right')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	pass
