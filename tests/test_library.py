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
