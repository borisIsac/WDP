from django.contrib import admin
from .models import WishList
# Register your models here.
class WishListAdmin(admin.ModelAdmin):
    class Meta:
        model=WishList
        list_display=['__all__']

admin.site.register(WishList, WishListAdmin)