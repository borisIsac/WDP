from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        new_book = Books.objects.create(**validated_data)
        print(new_book.data)
        return new_book.data