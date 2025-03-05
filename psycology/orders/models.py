from django.db import models
from books.models import *
from users.models import *

# Create your models here.
class Order(models.Model):
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Order Nº{} belong to {}".format(self.id, self.user)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    digital_book = models.BooleanField(default=False)
    book_file = models.FileField(upload_to='ebooks/', null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} item(s) {self.book} of {self.order}"