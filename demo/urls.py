from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    # demo/
    path('', views.rootPath),
    # demo/first/
    path('first', views.first),
    # demo/second/
    path('second', views.second),

    # 使用 class view 的方式
    # demo/another/
    path('another', Another.as_view()),
]