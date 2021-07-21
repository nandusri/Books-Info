from rest_framework import serializers
from .models import Book

class BooksSerializer(serializers.ModelSerializer):
    """Serialize Books"""
    total_books = serializers.SerializerMethodField()
    total_authors = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ("id","title","author","description","total_books","total_authors")
    
    def get_total_books(self, request):
        return Book.objects.count()

    def get_total_authors(self, request):
        return Book.objects.values('author').distinct()