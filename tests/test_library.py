import unittest
from src.library import Library

class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_successful_book_addition(self):
        self.library.add_book("B101", "The Stranger", "Albert Camus")
        self.assertIn("B101", self.library.books)

    def test_duplicate_book_addition_raises_error(self):
        self.library.add_book("B101", "The Stranger", "Albert Camus")
        with self.assertRaises(ValueError):
            self.library.add_book("B101", "The Stranger", "Albert Camus")

if __name__ == "__main__":
    unittest.main()
class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("B101", "Clean Code", "Robert C. Martin")

    def test_borrow_available_book(self):
        self.library.borrow_book("B101")
        self.assertTrue(self.library.books["B101"].borrowed)

    def test_borrow_unavailable_book_raises_error(self):
        self.library.borrow_book("B101")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B101")

    def test_return_book_updates_status(self):
        self.library.borrow_book("B101")
        self.library.return_book("B101")
        self.assertFalse(self.library.books["B101"].borrowed)
