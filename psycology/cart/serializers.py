from rest_framework import serializers
from .models import *

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartList
        fields = [
            'id',
            'user',
            'books',
            'created_at',
            'updated_at',
            ]

    def create(self, validated_data):

        request = self.context['request']
        book = validated_data['books']
        
        new_wishlist, created = CartList.objects.get_or_create(user=request.user, books = book)
        return new_wishlist
    