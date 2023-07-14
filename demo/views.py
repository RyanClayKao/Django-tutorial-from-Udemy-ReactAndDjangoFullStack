from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rootPath(request):
    return HttpResponse("這是 rootPath 函式的 http response 結果")

def first(request):
    return HttpResponse("這是 first 函式的 http response 結果")

def second(request):
    return HttpResponse("這是 second 函式的 http response 結果")