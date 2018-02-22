from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=1024)
    text = models.TextField(default="")
    added_at = models.DateField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default= 'x')
    likes = models.ManyToManyField(User, related_name="like_set")

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, default= 'x')

    def __str__(self):
        return self.text