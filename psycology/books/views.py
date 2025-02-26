from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from users.permissions import IsSuperuser

print(IsSuperuser.has_permission)

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
   
class UpdateBookRegisterView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuser]

    def get_object(self):
        return self.request.user