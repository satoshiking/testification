from django.db import models


class Group(models.Model):
    group_text = models.CharField(max_length=200)
    def __str__(self):
    	return self.group_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)     
    def __str__(self):
    	return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    right = models.BooleanField()

    def __str__(self):
    	return self.choice_text



