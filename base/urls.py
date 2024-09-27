from django.urls import path, include
from base import views

urlpatterns = [
    path('', view=views.index, name="index"),
]
