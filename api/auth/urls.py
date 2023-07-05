from django.urls import path, include
from rest_framework import routers
from .views import SignupView, LoginView, LogoutView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
