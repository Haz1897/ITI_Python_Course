from django.urls import path
from theatre.api import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
]