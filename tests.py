from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверка устанавливки жанра книги, если книга есть в books_genre и её жанр входит в список genre.
    def test_set_book_genre_from_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert  collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    # Проверка устанавливки жанра книги, если книга есть в books_genre и её жанр не входит в список genre.
    @pytest.mark.parametrize('genre', ['Драма', 'Документальный фильм', 'анимэ'])
    def test_set_book_genre_not_in_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre )
        assert collector.books_genre not in collector.genre

    # Проверка вывода жанра книги по её имени
    def  test_get_book_genre_book_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # Проверка вывода списка книг с определённым жанром.
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        books_with_specific_genre = collector.get_books_with_specific_genre('Ужасы')
        assert books_with_specific_genre == ['Гордость и предубеждение и зомби']

    # Проверка получени словаря books_genre
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre == {'Гордость и предубеждение и зомби': 'Ужасы'}

    # Проверка возврата книг, подходящие детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Колобок']

    # Проверка добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        book_in_favorites = collector.get_list_of_favorites_books()
        assert book_in_favorites == ['Гордость и предубеждение и зомби']

    # Проверка удаляения книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Оно')

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Оно')
        book_in_favorites = collector.get_list_of_favorites_books()
        assert book_in_favorites == ['Гордость и предубеждение и зомби']

    #  Проверка получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        сollector = BooksCollector()
        сollector.add_new_book('Оно')
        сollector.set_book_genre('Оно', 'Ужасы')
        сollector.add_book_in_favorites('Оно')

        сollector.add_new_book('Гордость и предубеждение и зомби')
        сollector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        сollector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites = сollector.get_list_of_favorites_books()
        assert favorites == ['Оно', 'Гордость и предубеждение и зомби']