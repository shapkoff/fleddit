from django.urls import path, include
from branches import views

urlpatterns = [
    path('', views.branches_list_view, name='branches_list'),
    path('<str:name>/', views.branch_view, name='branch'),
    path('<str:branch>/<slug:slug>/', include('posts.urls')),
]