from django.shortcuts import render, get_object_or_404, redirect
from .models import Article


def home(request):
    articles = Article.objects
    return render(request, 'articles/home.html', {'articles': articles})


def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.is_premium:
        return redirect('join')
    else:
        return render(request, 'articles/article.html', {'article': article})


def join(request):
    return render(request, 'articles/join.html')

