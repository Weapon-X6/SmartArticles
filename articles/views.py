from django.shortcuts import render
from .models import Article


def home(request):
    articles = Article.objects
    return render(request, 'articles/home.html', {'articles': articles})

