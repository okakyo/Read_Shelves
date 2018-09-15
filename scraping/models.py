from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    text=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

