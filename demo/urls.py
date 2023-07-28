from django.urls import path, include
from . import views
from .views import Another, BookDao, BookViewSet
from rest_framework import routers

# ========= 使用 rest_framework =======
router = routers.DefaultRouter()
router.register('books', BookViewSet)

# =======Django 原生的 route url 路徑設定 =======
urlpatterns = [
    # demo/
    # path('', views.rootPath),
    # ========= 使用 rest_framework 的 router 來設定跟路徑 ======= Start
    path('', include(router.urls)),
    # ========= 使用 rest_framework 的 router 來設定跟路徑 ======= End

    # demo/first/
    path('first/', views.first),
    # demo/second/
    path('second/', views.second),

    # 使用 class view 的方式
    # demo/another/
    path('another/', Another.as_view()),
    path('books/', BookDao.as_view()),

    # 使用 template 來渲染呈現 html
    path('template1', views.template1)


    
]