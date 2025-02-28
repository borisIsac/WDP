from django.shortcuts import render
from rest_framework import viewsets, permissions, response, status, generics
from rest_framework.views import APIView
from users.permissions import IsSuperuser
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404





class WishListViewSet(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users only see their own wishlist.
        """
        return WishList.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Books, id=book_id)

        wishlist, created = WishList.objects.get_or_create(user=request.user, books = book)

        if not created:
            context = {
                'error_msg': 'A book already exist in your wishlist'
            }
            return response.Response(context, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(wishlist)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """
        Set the wishlist owner to the logged-in user.
        """
        serializer.save(user=self.request.user)

class BookToWishlist(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        wishlist, created = WishList.objects.get_or_create(user=request.user)

        book = get_object_or_404(Books, id=book_id)

        
        if book in wishlist.books.all():
            return response.Response({'messege': 'book already exist in your wishlist'})

        wishlist.books.add(book)
        #wishlist.save()
        return response.Response({"message": "Book added to wishlist"}, status=status.HTTP_200_OK)
    
    def delete(self, request, book_id):
        
        wishlist = get_object_or_404(WishList, user=request.user)

        book = get_object_or_404(Books, id=book_id)

        if book not in wishlist.books.all():
            context = {
                'message': 'Book does not exist in wishlist'
            }
            return response.Response(context,status=status.HTTP_204_NO_CONTENT)

        wishlist.books.remove(book)
        #wishlist.save()
        context = {
                'message': f"Book '{book}' has been eleminated"
            }
        return response.Response(context,status=status.HTTP_204_NO_CONTENT)