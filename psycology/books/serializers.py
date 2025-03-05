from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
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

'''    def create(self, validated_data):
        new_book = Books.objects.create(**validated_data)
        return new_book
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)'''
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'book', 'text_comment', 'published_at']
        read_only_fields = ['id', 'user', 'book', 'published_at']

'''
    def create(self, validated_data):
        new_comment= Comment.objects.create(**validated_data)
        return new_comment
    
    def update(self, instance, validated_data):
        return super().update(instance=instance, validated_data=validated_data)'''