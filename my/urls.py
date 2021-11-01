from os import name
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
    #path('home/', admin.site.urls),
    #path('projects/', projects, name='projects'),
    #path('profiles/', admin.site.urls),
]
