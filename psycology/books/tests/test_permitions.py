from django.urls import reverse
from django_countries import countries
from rest_framework import status
from ..models import Comment, Books
from users.models import CustomUser
from rest_framework.test import APITestCase, APIClient


class IsOwnerOrReadOnlyTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        """Создаём пользователей, книгу и комментарий"""
        self.owner = CustomUser.objects.create_user(
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
        self.another_user = CustomUser.objects.create_user(
            is_active=True,
            email="testemail1@email.com",
            password="12345",
            full_name="Test1 User Test",
            phone="987654321",
            username="Test1UsernameTest",
            birthday="2000-01-01",
            gender=CustomUser.Gender.FEMALE,
            country=countries._countries['RU']
        )
        self.book = Books.objects.create(
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

        self.new_comment = Comment.objects.create(
            user=self.owner,
            book=self.book,
            text_comment="Bum"
        )

        self.url = f"/api/v1/books/{self.book.id}/comments/"

        self.url_detail = reverse("detale_comment", kwargs={"book_id": self.book.id, "pk": self.new_comment.id})
        self.url_list = reverse("book_comments", kwargs={"book_id": self.book.id})

    def test_owner_can_edit(self):
        """Владелец комментария может его редактировать"""
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.url_detail, {"text_comment": "Updated comment"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_cannot_edit(self):
        """Другой пользователь НЕ может редактировать комментарий (403 Forbidden)"""
        self.client.force_authenticate(user=self.another_user)
        response = self.client.patch(self.url_detail, {"text_comment": "Hacked comment"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anyone_can_read(self):
        """Любой пользователь может читать комментарий"""
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_create_comment(self):
        """Авторизованный пользователь может создать комментарий"""
        self.client.force_authenticate(user=self.another_user)
        data = {"text_comment": "Новый комментарий"}
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_owner_edit(self):
        self.client.force_authenticate(user=self.owner)


