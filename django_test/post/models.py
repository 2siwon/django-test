from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
