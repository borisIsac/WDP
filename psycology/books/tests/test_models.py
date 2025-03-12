from django.test import TestCase
from django.urls import reverse
from books.models import Books, BookRating, Comment
from users.models import CustomUser 
from django_countries import countries


class BooksTest(TestCase):
    def test_create_new_book(self):
        new_book = Books.objects.create(
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

        self.assertEqual(new_book.title,"Docker для DevOps") 
        self.assertEqual(new_book.author, "Иван Иванов") 
        self.assertEqual(new_book.description, "Обзор Docker для разработчиков и DevOps.") 
        self.assertEqual(new_book.published_date, "2025-03-01") 
        self.assertEqual(new_book.price, 29.99) 
        self.assertEqual(new_book.format, Books.Format.PAPERBACK) 
        self.assertEqual(new_book.stock, 100) 
        self.assertEqual(new_book.category, "DevOps") 
        self.assertEqual(new_book.link_to_download, "https://example.com/download") 
        self.assertEqual(new_book.link_to_ebook, "https://example.com/ebook")
        self.assertEqual(str(new_book), "Иван Иванов-Docker для DevOps")

    def test_create_new_comments(self):
        user = CustomUser.objects.create(
                is_active=True,
                email="testemail@email.com",
                password="12345",
                full_name="Test User Test",
                phone="987654321",
                username="TestUsernameTest",
                birthday="2000-01-01",
                gender=CustomUser.Gender.MALE,
                country = countries._countries['PT']
            )
        
        book = Books.objects.create(
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


        new_comment = Comment.objects.create(
            book = book,
            user = user,
            text_comment = "!!!comment test 1!!!"
        )

        self.assertEqual(user.__str__(), 'Test User Test',)
        self.assertEqual(book.__str__(),'Иван Иванов-Docker для DevOps')
        self.assertEqual(new_comment.__str__(), "Test User Test-Иван Иванов-Docker для DevOps")

    def test_average_rating(self):

            user = CustomUser.objects.create(
                is_active=True,
                email="testemail@email.com",
                password="12345",
                full_name="Test User Test",
                phone="987654321",
                username="TestUsernameTest",
                birthday="2000-01-01",
                gender=CustomUser.Gender.MALE,
                country=countries._countries['PT']
            )

            user2 = CustomUser.objects.create(
                is_active=True,
                email="testemail1@email.com",
                password="12345",
                full_name="Test User Test",
                phone="987654321",
                username="TestUsernameTest",
                birthday="2000-01-01",
                gender=CustomUser.Gender.MALE,
                country=countries._countries['PT']
            )

            book1 = Books.objects.create(
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
            book2 = Books.objects.create(
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
            r1 = BookRating(
                rating=2,
                user_id=1,
                book_id=1,
            )
            r2 = BookRating(
                rating=3,
                user_id=1,
                book_id=2,
            )
            r3 = BookRating(
                rating=5,
                user_id=2,
                book_id=1,
            )

            r1.save()
            r2.save()
            r3.save()

            self.assertEqual(book1.average_rating(), 3.5)
