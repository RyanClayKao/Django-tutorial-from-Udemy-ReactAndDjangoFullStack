from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # 設定回傳後可顯示的欄位有哪些
        fields = ['title', 'description', 'price']