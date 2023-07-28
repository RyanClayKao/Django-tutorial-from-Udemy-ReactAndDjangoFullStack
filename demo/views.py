from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

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

class BookDao(View):
    outputHtmlString = ""

    # 「objects.all() 用法」
    # 取用 Book model 中的所有資料 
    # (可以理解為像是 C# 讀取了 Book資料表的資料，並放到一個 list裡面，而這裡的用法像是 entity framework 的用法，可以再針對 books 進行類似 list的操作)
    books = Book.objects.all()

    outputHtmlString += "====== model.objects.all() 的應用 ======<br>"
    outputHtmlString += f"There are {len(books)} books in DB.<br>"
    outputHtmlString += "book list: <br>"
    for book in books:
        outputHtmlString += f" id: {book.id} ,book title: {book.title}.<br>"


    # 「objects.filter(篩選條件) 用法」
    # 範例：過濾出指定 ID的資料
    filteredBooks = Book.objects.filter(is_published = True)

    outputHtmlString += "====== model.objects.filter(篩選條件) 的應用 ======<br>"
    outputHtmlString += "以 is_published = True 為篩選條件<br>"
    outputHtmlString += "篩選後的查詢結果: <br>"
    for filteredBook in filteredBooks:
        outputHtmlString += f"id: {filteredBook.id}, title: {filteredBook.title} <br>"



    # 「objects.get(篩選條件) 用法，單筆查詢」
    pickedBook = Book.objects.get(id = 1)
    outputHtmlString += "====== model.objects.get(篩選條件) 的應用，做單筆查詢 ======<br>"
    outputHtmlString += "以 id = 1為條件，做單筆查詢<br>"
    outputHtmlString += "查詢結果: <br>"
    outputHtmlString += f"id: {pickedBook.id}, title: {pickedBook.title}"

    def get(self, request):      
        # self 指的是現在這個類別，所以可以用物件導向的方式來取用類別中的屬性 
        return HttpResponse(self.outputHtmlString)



# ============= 使用 template ============
def template1(request):
    books = Book.objects.all()

    return render(request, 'template1.html', {
        'message': "this message is from backend.",
        'books': books
    })