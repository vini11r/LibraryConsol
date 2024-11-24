import os
import unittest

from Library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создание тестовой библиотеке с временным файлом."""
        self.library = Library("test_library.json")
        self.library.books.clear()  # Очищаем книги для тестов
        self.library.max_book_id = 0  # Сбрасываем максимальный ID для тестирования

    def tearDown(self):
        """Удаление временного файла после тестов."""
        try:
            os.remove("test_library.json")
        except OSError:
            pass

    def test_add_book(self):
        """Тест на добавление книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")
        self.assertEqual(self.library.books[0].author, "Джордж Оруэлл")
        self.assertEqual(self.library.books[0].year, 1949)
        self.assertEqual(self.library.books[0].status, "в наличии")
        self.assertEqual(self.library.books[0].book_id, 1)

    def test_remove_book(self):
        """Тест на удаление книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        result = self.library.remove_book(1)
        self.assertEqual(result, "Книга с ID 1 удалена.")
        self.assertEqual(len(self.library.books), 0)

        with self.assertRaises(ValueError) as context:
            self.library.remove_book(1)
        self.assertEqual(str(context.exception), "Книга с указанным id не найдена.")

    def test_search_books(self):
        """Тест на поиск книг."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.add_book("Animal Farm", "Джордж Оруэлл", 1945)

        results = self.library.search_books("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")

        results = self.library.search_books("Джордж Оруэлл")
        self.assertEqual(len(results), 2)

        results = self.library.search_books("Счётная книга")  # Книга не существует
        self.assertEqual(len(results), 0)

    def test_display_books(self):
        """Тест на отображение книг."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.add_book("Animal Farm", "Джордж Оруэлл", 1945)
        self.library.display_books()  # Проверяем вывод в консоль

    def test_change_status(self):
        """Тест на изменение статуса книги."""
        self.library.add_book("1984", "Джордж Оруэлл", 1949)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

        with self.assertRaises(ValueError) as context:
            self.library.change_status(1, "недоступно")  # Ошибка статуса
        self.assertEqual(str(context.exception), "Неверный статус. Используйте 'в наличии' или 'выдана'.")

        with self.assertRaises(ValueError) as context:
            self.library.change_status(2, "в наличии")  # Книга не найдена
        self.assertEqual(str(context.exception), "Книга с указанным id не найдена.")


if __name__ == "__main__":
    unittest.main()
