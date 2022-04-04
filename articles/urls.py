from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('articles/<int:pk>', views.article, name='article'),
    path('join', views.join, name='join'),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
]
