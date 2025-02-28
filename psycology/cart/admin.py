from django.contrib import admin
from .models import *
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'user', 'get_books']
    readonly_fields = ['reservation']

    def get_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])
    get_books.short_description = "Books"
       
admin.site.register(Cart, CartAdmin)
