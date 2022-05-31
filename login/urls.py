from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('accounts/', RedirectView.as_view(url='login/')),

    path('accounts/login/', views.login, name='login'),
]