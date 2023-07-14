from django.urls import path
from . import views

urlpatterns = [
    # demo/
    path('', views.rootPath),
    # demo/first/
    path('first', views.first),
    # demo/second/
    path('second', views.second),
]