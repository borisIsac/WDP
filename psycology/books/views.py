from rest_framework import viewsets, permissions, response
from .models import *
from .serializers import *
from .permissions import *
from rest_framework import generics
from users.permissions import IsSuperuser
from wish_list.models import *
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_book_rating_list(request, book_id):
    ratings = BookRating.objects.filter(book_id=book_id)
    serializer = BooksRatingSerializer(ratings, many=True)
    return response.Response(serializer.data)

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
    

class CommentsViewSet(viewsets.ModelViewSet):
    '''
    print all comments to each books.
    return JSON
    '''
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def get_permissions(self):
        """
        Assign different permissions based on the action.
        """
        if self.action in ["create", "update", "partial_update",]:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        elif self.action in ["destroy"]:
            return [permissions.IsAuthenticated(), IsSuperuser()]
        return [permissions.AllowAny()]


    
    def get_queryset(self):
        """
        Get a comment witch bellongs to single book by primary key.
        """
        book_id = self.kwargs['book_id']
    
        return Comment.objects.filter(book_id=book_id)
    
    def perform_create(self, serializer):
        book_id = self.kwargs['book_id']
        return serializer.save(user=self.request.user, book_id=book_id)
    