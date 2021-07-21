import coreapi
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from books.models import Book
from .serializers import BooksSerializer

class BookSchema(AutoSchema):

    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [
                coreapi.Field('title'), 
                coreapi.Field('description'),
                coreapi.Field('author')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class BookView(APIView):
    """
    List all books info, or create a new book info.
    """
    schema = BookSchema()

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    """
    Retrieve, update or delete a book instance.
    """

    schema = BookSchema()

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
