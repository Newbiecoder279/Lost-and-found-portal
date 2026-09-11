from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.LandingView, name="landing"),
    path('signup/', views.SignUpView, name="signup"),
    path('login/', views.LoginView, name="login")
]
