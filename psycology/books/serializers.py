from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):

    average_rating = serializers.SerializerMethodField()
    ratings_list = serializers.SerializerMethodField()

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
            'ratings_list',
            'average_rating',
            'link_to_ebook',
            'link_to_download',
            'cover',
            'created_at',
            'updated_at',
            ]
        
    def get_ratings_list(self, obj):
        return list(obj.rating_list().values_list('rating', flat=True))

    def get_average_rating(self, obj):
        return obj.average_rating()


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

class BooksRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookRating
        fields = ['id', 'user', 'book', 'rating', 'published_at']