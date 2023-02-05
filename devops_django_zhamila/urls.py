from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, HttpRequest

def hello(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hello)
]
