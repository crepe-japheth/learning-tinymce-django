from turtle import title
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Articles(models.Model):

    title = models.CharField(max_length=200)
    post = HTMLField()

    def __str__(self):
        return self.title
