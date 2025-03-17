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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'book', 'text_comment', 'published_at']
        read_only_fields = ['id', 'user', 'book', 'published_at']

class BooksRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookRating
        fields = ['id', 'user', 'book', 'rating', 'published_at']

    def create(self, validated_data):

        user = self.context['request'].user
        book = validated_data['book']

        return BookRating.objects.create(user=user,book=book, **validated_data)
