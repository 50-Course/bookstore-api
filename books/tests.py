from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title='TestBook',
            subtitle='Book Subtitle',
            author='BigBen',
            isbn=str(126876876631)
        )
    def test_book_content(self):
        self.assertEquals(self.book.title, 'TestBook')
        self.assertEquals(self.book.subtitle, 'Book Subtitle')
        self.assertEquals(self.book.author, 'BigBen')
        self.assertEquals(self.book.isbn, '126876876631')
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertTemplateUsed(response, template_name='books/book_list.html')
        self.assertEquals(response.status_code, 200)