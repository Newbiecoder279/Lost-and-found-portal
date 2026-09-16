from django.urls import path 
from . import views

urlpatterns = [
    path('report/',views.ReportItemView,name="report-item"),
    path('details/<int:pk>/',views.ItemDetailsView, name="item-details"),
    path('search/',views.ItemSearchView,name="item-list")
    
]
