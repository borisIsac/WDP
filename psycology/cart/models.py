from django.db import models
from users.models import *
from books.models import *

# Create your models here.
class CartList(models.Model):
    class Meta:
        verbose_name = "CartList"
        verbose_name_plural = "CartLists"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cartlist")
    books = models.ManyToManyField(Books, related_name="cartlisted_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.user}"