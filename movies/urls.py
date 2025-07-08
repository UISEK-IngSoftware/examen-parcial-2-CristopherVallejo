from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.movie_details, name='detail'),
    path('movie/add/', views.add_movie, name='add_movie'), 
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('movie/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('movie/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]