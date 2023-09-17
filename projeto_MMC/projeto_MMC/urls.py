from django.urls import path
from app_MMC import views

urlpatterns = [
    path('', views.home, name='home'),
]
