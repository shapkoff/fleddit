from django.urls import path
from posts import views

urlpatterns = [
    path('', views.post_view, name='post'),
    path('new/', views.add_new_post, name='new')
]
