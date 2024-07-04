from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.addBook, name='add-book'),
    path('ranking/<str:pk>/', views.ranking, name='ranking'),
]
