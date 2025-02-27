from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from users.permissions import IsSuperuser


class BookViewSet(generics.ListAPIView):
    '''
    print all book_list.
    return JSON
    '''
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class NewBookRegisterView(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuser]
   

class UpdateBookView(generics.RetrieveUpdateAPIView):

    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuser]

    def get_object(self):
        return generics.get_object_or_404(Books, pk=self.kwargs["pk"])
    

class GetSingleBookView(generics.RetrieveAPIView):

    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return generics.get_object_or_404(Books, pk=self.kwargs["pk"])
    