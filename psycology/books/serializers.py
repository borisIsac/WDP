from rest_framework import serializers
from .models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'description',
            'published_date',
            'price',
            'format',
            'stock',
            'category',
            'average_rating',
            'link_to_ebook',
            'link_to_download',
            'cover',
            'created_at',
            'updated_at',
            ]
        
    def get(self, request):
        print('-----hello world')

    def create(self, validated_data):
        new_book = Books.objects.create(**validated_data)
        return new_book
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)