from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец: возвращение короля")
        assert "Властелин колец: возвращение короля" in collector.get_books_genre()


    def test_set_book_genre_add_genre_for_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")
        assert collector.get_book_genre("1984") == "Ужасы"

    def test_get_book_genre_empty_books_genre(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Book1') == None


    def test_get_books_with_specific_genre_getting_a_book_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_new_book("Скотный двор")
        collector.set_book_genre("1984", "Ужасы")
        collector.set_book_genre("Скотный двор", "Детективы")
        assert collector.get_books_with_specific_genre("Ужасы") == ["1984"]
        assert collector.get_books_with_specific_genre("Детективы") == ["Скотный двор"]


    def test_get_books_for_children_childrens_books(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Lord of the Rings")
        collector.set_book_genre("Harry Potter", "Фантастика")
        collector.set_book_genre("Lord of the Rings", "Детективы")
        assert collector.get_books_for_children() == ["Harry Potter"]


    def test_add_book_in_favorites_adding_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Детективы Дарьи Донцовой")
        collector.add_book_in_favorites("Детективы Дарьи Донцовой")
        assert collector.get_list_of_favorites_books() == ["Детективы Дарьи Донцовой"]


    def test_delete_book_from_favorites_remove_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 1")
        assert collector.get_list_of_favorites_books() == []


    @pytest.mark.parametrize("genre, expected", [
        ("Фантастика", ["Книга 1"]),
        ("Ужасы", ["Книга 2"]),
        ("Детективы", [])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        collector.set_book_genre("", "Детективы")
        assert collector.get_books_with_specific_genre(genre) == expected