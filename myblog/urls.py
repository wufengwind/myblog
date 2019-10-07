from django.contrib import admin
from django.urls import path,include
from blog.views import index
from blog.views import login
from blog.views import register
from blog.views import essay
from blog.views import write
from blog.views import pulish
from blog.views import viwe
from blog.views import viewone
from blog.views import search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('index/essay/',essay),
    path('write/',write),
    path('index/pulish/',pulish),
    path('viwe/',viwe),
    path('viewone/',viewone),
    path('search/',search),
]
