from django.contrib import admin

from .models import Question, Choice, Group

admin.site.register(Group)
admin.site.register(Question)
admin.site.register(Choice)