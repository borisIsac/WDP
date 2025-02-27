from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from users.permissions import IsSuperuser


class BookViewSet(viewsets.ModelViewSet):
    '''
    print all book_list.
    return JSON
    '''
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    
    def get_permissions(self):
        """
        Assign different permissions based on the action.
        """
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsSuperuser()]
        return [permissions.AllowAny()]


    def get_object(self):
        """
        Get a single book by primary key.
        """
        return generics.get_object_or_404(self.queryset, pk=self.kwargs["pk"])




'''

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
    

class DeleteBookView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuser]  # Only admin users can delete

    def get_object(self):
        return generics.get_object_or_404(self.queryset, pk=self.kwargs["pk"])'''