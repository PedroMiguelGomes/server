from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)
    correct = models.IntegerField()
    score = models.IntegerField()
    chapter = models.IntegerField()
    number = models.IntegerField()
    def __str__(self):
        return self.question

class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    score = models.IntegerField()
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.name

class Progress(models.Model):
    progress = models.FloatField()
    def __str__(self):
        return self.progress
