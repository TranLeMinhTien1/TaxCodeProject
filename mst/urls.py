from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name='index'),
    path('Search/', views.Search, name='Search'),
]