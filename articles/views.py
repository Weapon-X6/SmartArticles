import stripe
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
import stripe

from .forms import ArticlesSignUpForm
from .models import Article


stripe.api_key = 'sk_test_'


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


@login_required
def checkout(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        coupon = 'none'
        price = 1000
        og_dollar = 10
        coupon_dollar = 0
        final_dollar = 10
        if request.method == 'GET' and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 10000
                og_dollar = 100
                final_dollar = 100
        return render(request, 'articles/checkout.html', )


class SignUp(generic.CreateView):
    form_class = ArticlesSignUpForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
