from django.db import models
from users.models import CustomUser
from books.models import *

# Create your models here.
class Cart(models.Model):
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    RJUST = 10


    def fuel_reservation(self):
        res = f'{self.id}'.rjust(self.RJUST, '0')
        return res

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cart")
    books = models.ManyToManyField(Books, related_name="cartlisted_books")
    reservation = models.CharField(max_length=RJUST, blank=True, unique=True)

    
    def save(self, *args, **kwargs):
        if not self.reservation:
            super().save(*args, **kwargs)
            self.reservation = self.fuel_reservation()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user}-{self.reservation}"
