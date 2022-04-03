from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=33)
    text = models.TextField()
    is_premium = models.BooleanField(default=True)

