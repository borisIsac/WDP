from django.contrib import admin
from .models import WishList
# Register your models here.
class WishListAdmin(admin.ModelAdmin):
    model=WishList
    list_display=['user']

admin.site.register(WishList, WishListAdmin)