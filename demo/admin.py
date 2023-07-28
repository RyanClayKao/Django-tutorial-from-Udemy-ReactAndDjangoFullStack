from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

# 使用 class 的方式來註冊及設定操作介面
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 「資料列表介面設定」
    # 設定列表上顯示的欄位 (可以想像成像是資料庫查詢後，列表結果的欄位要有那些)
    list_display = ['title', 'price', 'published']

    # 設定列表的篩選器
    list_filter = ['published']
    # list_filter = ['published', 'price']

    # 設定列表的查詢功能
    search_fields = ['title']
    # 可以多欄位查詢
    # search_fields = ['title', 'description']



    # 「單筆資料介面設定」
    # 針對單筆資料操作時，設定該筆可見的欄位
    # fields = ['title', 'description']