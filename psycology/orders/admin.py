from django.contrib import admin
from .models import *
# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    class Meta:
        model=Order
        fields=['user', 'created_at']
    

class OrderItemAdmin(admin.ModelAdmin):
    class Meta:
        model=OrderItem
        fields=['order', 'book', 'digital_book']


admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderItem,OrderItemAdmin)