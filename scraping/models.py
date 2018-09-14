from django.db import models
import datetime
# Create your models here.

class Title(models.Model):
    title=models.CharField(max_length=100)

class Article(models.Model):
    title=models.ForeignKey(Title,on_delete=models.CASCADE)
    url=models.URLField()
    text=models.TextField()
    date=models.DateField(default=datetime.date.today().strftime('%Y-%m-%d'))

