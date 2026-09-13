from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.LandingView, name="landing"),
    path('signup/', views.SignUpView, name="signup"),
    path('login/', views.LoginView, name="login"),
    path('home/',views.HomeView,name="home"),
    path('report/',views.ReportItemView,name="report-item")
]
