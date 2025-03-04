from django.contrib import admin
from .models import *
# Register your models here.
class CartListAdmin(admin.ModelAdmin):
    model=CartList
    list_display=['user']

admin.site.register(CartList, CartListAdmin)