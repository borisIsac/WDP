from rest_framework import viewsets, permissions, response, status
from rest_framework.views import APIView
from .models import *
from orders.models import Order, OrderItem
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import views, response


class CartListViewSet(viewsets.ModelViewSet):
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users only see their own cartlist.
        """
        return CartList.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Books, id=book_id)

        cartlist, created = CartList.objects.get_or_create(user=request.user, books = book)

        if not created:
            context = {
                'error_msg': 'A book already exist in your cartlist'
            }
            return response.Response(context, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(cartlist)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        """
        Set the cartlist owner to the logged-in user.
        """
        serializer.save(user=self.request.user)


class BookToCartlist(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        cartlist, created = CartList.objects.get_or_create(user=request.user)

        book = get_object_or_404(Books, id=book_id)

        
        if book in cartlist.books.all():
            return response.Response({'messege': 'book already exist in your wishlist'})

        cartlist.books.add(book)
        #wishlist.save()
        return response.Response({"message": "Book added to cartlist"}, status=status.HTTP_200_OK)
    
    def delete(self, request, book_id):
        
        cartlist = get_object_or_404(CartList, user=request.user)

        book = get_object_or_404(Books, id=book_id)

        if book not in cartlist.books.all():
            context = {
                'message': 'Book does not exist in cartlist'
            }
            return response.Response(context,status=status.HTTP_204_NO_CONTENT)

        cartlist.books.remove(book)
        #cartlist.save()
        context = {
                'message': f"Book '{book}' has been eleminated"
            }
        return response.Response(context,status=status.HTTP_204_NO_CONTENT)
    
class CheckoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Checkout process and creating order.
        """
        book_ids = request.data.get("books", [])  # Lista de IDs de livros
        if not book_ids:
            return response.Response({"error": "No books sellected"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user)

        for book_id in book_ids:
            book = Books.objects.get(id=book_id)
            digital_book = book.digital_book 
            book_file = book.book_file if digital_book else None
            
            OrderItem.objects.create(order=order, book=book, is_ebook=digital_book, ebook_file=book_file)

        return response.Response({"message": "Purchase completed successfully!", "order_id": order.id}, status=status.HTTP_201_CREATED)

