from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('about/<str:pk>',views.about, name='about'),
]