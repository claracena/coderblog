from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # path('accounts/login/', views.loginUser, name='login'),
    path('', RedirectView.as_view(url='login/')),
    # path('', views.loginUser, name='accounts'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.edit_profile, name='edit_profile'),
]