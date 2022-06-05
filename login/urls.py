from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
# from .views import loginUser, logoutUser, registerUser, edit_profile
from .views import loginUser, logoutUser, registerUser, edit_profile, PasswordsChangeView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('profile/', edit_profile, name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='login/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='login/change-password.html')),
    
    # path('password/', PasswordsChangeView.as_view(template_name='change-password.html')),
]