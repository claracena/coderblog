from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('accounts/', RedirectView.as_view(url='login/')),

    path('accounts/login/', views.loginUser, name='login'),
    path('accounts/logout/', views.logoutUser, name='logout'),
    path('accounts/register/', views.registerUser, name='register'),
]