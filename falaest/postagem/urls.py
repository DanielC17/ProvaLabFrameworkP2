
from django.urls import path
from postagem import views

urlpatterns = [
    path('', views.index,)
]