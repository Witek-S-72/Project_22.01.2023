"""mycalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import datetime as dt
import random
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, HttpResponse

def show_datetime(request):
    actual_date = dt.datetime.now()
    date_todayt = f"Dzisiaj jest: {actual_date.strftime('%A; %d-%b-%Y')}"
    actual_time = f"Bieżąca godzina to: {actual_date.strftime('%H:%M')}"
    return HttpResponse(f"<h1>{date_todayt}</h1>"
                       f"<h2>{actual_time}</h2>")

def show_random_numb(request):
    numbers = [str(random.randint(1,100)) for i in range(0,10)]
    return HttpResponse(f"Twoje liczby to: {'...'.join(numbers)}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_time/', show_datetime),
    path('random_data/', show_random_numb),
    path('examples/', include('examples.urls')),
    path('notes/', include('notes.urls')),

]
