import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_book_added_without_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    @pytest.mark.parametrize('book_name', ['', 'К' * 41])
    def test_add_new_book_name_with_invalid_number_of_characters_not_added(self, book_name, collector):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_book_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book(str(collector.books_genre.keys()))
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_existing_genre_added(self, collector, genre):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == genre

    def test_set_book_genre_not_existing_genre_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Мюзикл')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_genre_for_not_existing_book_not_added(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') is None

    def test_get_book_genre_genre_for_existing_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre_genre_from_not_existing_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Отсутствующая книга') is None

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_get_books_for_existing_in_books_genre(self, collector, genre):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.get_books_with_specific_genre(genre) == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_get_books_for_not_existing_in_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Мюзикл') == []

    @pytest.mark.parametrize('age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_no_book_with_age_rating(self, collector, age_rating):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', age_rating)
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize('age_rating', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_get_book_without_age_rating(self, collector, age_rating):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', age_rating)
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_existing_book_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_not_existing_book_not_added(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate_book_not_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_existing_book_delete(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_existing_book_not_delete(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
