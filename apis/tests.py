from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from books.models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            author='Django Foundation',
            title='Django Front to Back',
            isbn='6781291477712',
            subtitle='This is a description'
        )
    def test_book_list_api_view(self):
        response = self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(Book.objects.count(), 1)
        self.assertEqual(response, self.book)
