from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertionsort/', views.insertion_sort, name="insertion_sort"),
]