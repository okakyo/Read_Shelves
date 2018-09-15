from django.db import models
import datetime
# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    text=models.TextField()
    date=models.DateField(default=datetime.date.today().strftime('%Y-%m-%d'))

