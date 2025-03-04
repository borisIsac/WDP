from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    model=Books
    list_display=['title', 'author', 'category', 'price', 'stock']

class BooksComment(admin.ModelAdmin):
    model = Comment
    list_display=['user','book','published_at']

admin.site.register(Books, BooksAdmin)
admin.site.register(Comment, BooksComment)