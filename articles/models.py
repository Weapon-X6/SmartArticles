from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=33)
    text = models.TextField()
    is_premium = models.BooleanField(default=True)


class StripeCostumer(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
