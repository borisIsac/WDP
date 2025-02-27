from rest_framework import serializers
from .models import WishList

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = [
            'id',
            'user',
            'books',
            'created_at',
            'updated_at',
            ]

    def create(self, validated_data):
        new_wishlist = WishList.objects.create(**validated_data)
        return new_wishlist
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)