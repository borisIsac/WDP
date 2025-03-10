from django.db import models
from users.models import *

class Books(models.Model):

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


    class Format(models.TextChoices):
        PAPERBACK = "Paperback", "Paperback"
        EBOOK = "Ebook", "Ebook"

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    format = models.CharField(choices=Format.choices, max_length=15)
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    link_to_ebook = models.URLField(blank=True)
    link_to_download = models.URLField(blank=True)
    #TODO add cover field to DB, form and template and speack with team about storege
    cover = models.ImageField(upload_to='img/',  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.author} - {self.title}"


class Comment(models.Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_comment")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="books_comment")
    text_comment = models.TextField()
    published_at = models.DateTimeField("Published date", auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.book}"
