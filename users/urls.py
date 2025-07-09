from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.my_profile, name='profile'),
    path('password/', views.change_password, name='password'),
    path('disable/', views.disable_user, name='disable')
]