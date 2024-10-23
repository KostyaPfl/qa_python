# qa_python
### test_add_new_book_add_two_books - проверяет добавление книг в словарь
### test_add_new_book_book_added_without_genre - проверяет что новые книги добавляются с пустым жанром
### test_add_new_book_name_with_invalid_number_of_characters_not_added - проверяет что книги не добавляются если в названии недопустимое количество символов
### test_add_new_book_duplicate_book_not_added - проверяет что нельзя добавить одну книгу дважды
### test_set_book_genre_existing_genre_added - проверяет что книге можно установить разрешенный жанр
### test_set_book_genre_not_existing_genre_not_added - проверяет что книге не выставить не разрешенный жанр
### test_set_book_genre_genre_for_not_existing_book_not_added - проверяет что нельзя выставить жанр несуществующей книге
### test_get_book_genre_genre_for_existing_book - проверяет получение жанра у существующей книги
### test_get_book_genre_genre_from_not_existing_book - проверяет что невозможно получить жанр несуществующей книги
### test_get_books_with_specific_genre_get_books_for_existing_in_books_genre - проверяет получение книг по разрешенному жанру
### test_get_books_with_specific_genre_get_books_for_not_existing_in_books_genre - проверяет что невозможно получить список книг по неразрешенному жанру
### test_get_books_for_children_no_book_with_age_rating - проверяет что в список книг для датей не попадают книги с возрастными жанрами
### test_get_books_for_children_get_book_without_age_rating - проверяет что в список книг для детей попадают книги с жанрами без возрастных ограничений
### test_add_book_in_favorites_existing_book_added - проверяет что в список избранных можно добавить существующую книгу
### test_add_book_in_favorites_not_existing_book_not_added - проверяет что неевозможно дабавить в список избранного несуществующую книгу
### test_add_book_in_favorites_duplicate_book_not_added - проверяет что невозможно дабавить в список избранного одну книгу дважды
### test_delete_book_from_favorites_existing_book_delete - проверяет что можно удалить из списка избранного существующую в нем книгу
### test_delete_book_from_favorites_not_existing_book_not_delete - проверет что невозмозно удалить из списка несуществующую в нем книгу
