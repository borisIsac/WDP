from rest_framework import serializers, response
from .models import Order, OrderItem
from books.models import Books 
from rest_framework import decorators
from users.serializers import UserSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:

        book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all(), source="book")

        model=OrderItem
        fields = [
            'id',
            'book',
            'quantity'
            ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.ReadOnlyField(source="user.email")
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'user', 'items']
    
    def create(self, validated_data):
        
        items_data = validated_data.pop('items')
        validated_data.pop("user", None)
        
        user = self.context["request"].user
        order = Order.objects.create(user=user, **validated_data)

        for i, item_data in enumerate(items_data):
            OrderItem.objects.create(order=order, **item_data)

        return order
    