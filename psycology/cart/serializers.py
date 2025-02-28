from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'books'
        ]
    
    def create(self, validated_data):

        request = self.context['request']
        book = validated_data['books']
        
        new_cart, created = Cart.objects.get_or_create(user=request.user, books = book)
        return new_cart