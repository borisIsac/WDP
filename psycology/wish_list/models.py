from django.db import models
from users.models import *
from books.models import *

# Create your models here.
class WishList(models.Model):
    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"
        unique_together = ('user',)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="wishlist")
    books = models.ManyToManyField(Books, blank=True, related_name="wishlisted_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.id}"
