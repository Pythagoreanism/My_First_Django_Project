from django.urls import path
from . import views

urlpatterns = [
    path("", views.sayHello),
    path("report/", views.sayApp)
]