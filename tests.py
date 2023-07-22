from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# Тест проверки добавления книги:
    def test_add_new_book_add_book(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец: возвращение короля")
        assert "Властелин колец: возвращение короля" in collector.get_books_genre()
        assert collector.get_book_genre("Властелин колец: возвращение короля") == ""

# Тест установки жанра книге:
    def test_set_book_genre_add_genre_for_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Ужасы")
        assert collector.get_book_genre("1984") == "Ужасы"

# Тест получения жанра книги по имени:
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Фантастика")
        assert collector.get_book_genre("Ведьмак") == "Фантастика"

# Тест получения списка книг с определённым жанром:
    def test_get_books_with_specific_genre_getting_a_book_by_genre(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_new_book("Скотный двор")
        collector.set_book_genre("1984", "Ужасы")
        collector.set_book_genre("Скотный двор", "Детективы")
        assert collector.get_books_with_specific_genre("Ужасы") == ["1984"]
        assert collector.get_books_with_specific_genre("Детективы") == ["Скотный двор"]

# Тест на возврат книг, подходящих детям:
    def test_get_books_for_children_childrens_books(self):
        collector = BooksCollector()
        collector.add_new_book("Harry Potter")
        collector.add_new_book("Lord of the Rings")
        collector.set_book_genre("Harry Potter", "Фантастика")
        collector.set_book_genre("Lord of the Rings", "Детективы")
        assert collector.get_books_for_children() == ["Harry Potter"]

# Тест добавления книги в Избранное:
    def test_add_book_in_favorites_adding_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Детективы Дарьи Донцовой")
        collector.add_book_in_favorites("Детективы Дарьи Донцовой")
        assert collector.get_list_of_favorites_books() == ["Детективы Дарьи Донцовой"]

# Тест удаления книги из Избранного:
    def test_delete_book_from_favorites_remove_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Book 1")
        collector.add_book_in_favorites("Book 1")
        collector.delete_book_from_favorites("Book 1")
        assert collector.get_list_of_favorites_books() == []

    @pytest.fixture
    def collector(self):
        return BooksCollector()

# Вывод списка книг с определённым жанром
    @pytest.mark.parametrize("genre, expected", [
        ("Фантастика", ["Книга 1"]),
        ("Ужасы", ["Книга 2"]),
        ("Детективы", []),
        ("Мультфильмы", []),
        ("Комедии", [])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_with_specific_genre(genre) == expected