from django.contrib import admin
from .models import *

class BooksAdmin(admin.ModelAdmin):
    model=Books
    list_display=['title', 'author', 'category', 'price', 'stock']

admin.site.register(Books, BooksAdmin)