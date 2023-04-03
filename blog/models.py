from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,'Draft'), (1, 'Publish'))
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) #article title
    content = models.TextField() #article content
    date_created = models.DateTimeField(auto_now_add=True) #created date
    slug = models.SlugField(max_length=200, unique=True)  # .../slug
    author = models.ForeignKey(to=User, on_delete=models.CASCADE) #article author taken from User table
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title