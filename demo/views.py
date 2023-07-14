from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def rootPath(request):
    return HttpResponse("這是 rootPath 函式的 http response 結果")

def first(request):
    return HttpResponse("這是 first 函式的 http response 結果")

def second(request):
    return HttpResponse("這是 second 函式的 http response 結果")

# 使用 class view 的方式
class Another(View):    
    def get(self, request):
        return HttpResponse("這是 Another 類別 get 函式的 http response 結果")