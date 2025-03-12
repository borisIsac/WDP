from django.test import TestCase
from django.urls import reverse
from books.models import Books, BookRating, Comment
from users.models import CustomUser 
from django_countries import countries


class BooksTest(TestCase):
    def setUp(self):
        self.book_1 = Books.objects.create(
            title="Docker для DevOps",
            author="Иван Иванов",
            description="Обзор Docker для разработчиков и DevOps.",
            published_date="2025-03-01",
            price=29.99,
            format=Books.Format.PAPERBACK,
            stock=100,
            category="DevOps",
            link_to_ebook="https://example.com/ebook",
            link_to_download="https://example.com/download"
        )

        self.user_1 = CustomUser.objects.create_user(
            is_active=True,
            email="testemail3@email.com",
            password="12345",
            full_name="Test1 User Test",
            phone="987654321",
            username="TestUsernameTest",
            birthday="2000-01-01",
            gender=CustomUser.Gender.MALE,
            country=countries._countries['PT']
        )

        self.user_2 = CustomUser.objects.create_user(
            is_active=True,
            email="testemail2@email.com",
            password="12345",
            full_name="Test User Test",
            phone="987654321",
            username="TestUsernameTest",
            birthday="2000-01-01",
            gender=CustomUser.Gender.MALE,
            country=countries._countries['PT']
        )

        self.book_2 = Books.objects.create(
            title="Docker для DevOps",
            author="Иван Иванов",
            description="Обзор Docker для разработчиков и DevOps.",
            published_date="2025-03-01",
            price=29.99,
            format=Books.Format.PAPERBACK,
            stock=100,
            category="DevOps",
            link_to_ebook="https://example.com/ebook",
            link_to_download="https://example.com/download"
        )

        self.comment_1 = Comment.objects.create(
            book=self.book_1,
            user=self.user_1,
            text_comment="!!!comment test 1!!!"
        )

        self.r1 = BookRating.objects.create(
            rating=2,
            user_id=self.user_1.id,
            book_id=self.book_1.id,
        )
        self.r2 = BookRating.objects.create(
            rating=3,
            user_id=self.user_1.id,
            book_id=self.book_2.id,
        )
        self.r3 = BookRating.objects.create(
            rating=5,
            user_id=self.user_2.id,
            book_id=self.book_1.id,
        )


    def test_create_new_book_title(self):
        self.assertEqual(self.book_1.title,"Docker для DevOps")

    def test_create_new_book_author(self):
        self.assertEqual(self.book_1.author, "Иван Иванов")

    def test_create_new_book_description(self):
        self.assertEqual(self.book_1.description, "Обзор Docker для разработчиков и DevOps.")

    def test_create_new_book_published_date(self):
        self.assertEqual(self.book_1.published_date, "2025-03-01")

    def test_create_new_book_price(self):
        self.assertEqual(self.book_1.price, 29.99)

    def test_create_new_book_format(self):
        self.assertEqual(self.book_1.format, Books.Format.PAPERBACK)

    def test_create_new_book_stock(self):
        self.assertEqual(self.book_1.stock, 100)

    def test_create_new_book_category(self):
        self.assertEqual(self.book_1.category, "DevOps")

    def test_create_new_book_download_link(self):
        self.assertEqual(self.book_1.link_to_download, "https://example.com/download")

    def test_create_new_book_ebook_link(self):
        self.assertEqual(self.book_1.link_to_ebook, "https://example.com/ebook")

    def test_create_new_book__str__(self):
        self.assertEqual(str(self.book_1), "Иван Иванов-Docker для DevOps")

    def test_create_new_comments_book(self):
        self.assertEqual(self.comment_1.__str__(), "Test1 User Test-Иван Иванов-Docker для DevOps")

    def test_average_rating(self):
        self.assertEqual(self.book_1.average_rating(), 3.5)
        self.assertEqual(self.book_2.average_rating(), 3)
