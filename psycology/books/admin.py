from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    model=Books
    list_display=['id','title', 'author', 'category', 'price', 'stock']

class BooksComment(admin.ModelAdmin):
    model = Comment
    list_display=['id','user','book','published_at']

class BooksRatingAdmin(admin.ModelAdmin):
    model = BookRating
    list_display = ['id','user', 'book', 'rating', 'published_at']

admin.site.register(Books, BooksAdmin)
admin.site.register(Comment, BooksComment)
admin.site.register(BookRating, BooksRatingAdmin)