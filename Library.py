import json


class Book:

    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """
        Преобразование книги в словарь
        """
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}', year={self.year}, status={self.status})"


class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.max_book_id = self.load_books()

    def load_books(self):
        """
        Загрузка книг из файла
        """
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                data = json.load(file)
                for book_data in data:
                    book = Book(**book_data)
                    self.books.append(book)
                return  max(book.book_id for book in self.books) if self.books else 0
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

    def save_books(self):
        """
        Сохранение книг в файл
        """
        with open(self.filename, "w", encoding='utf-8') as file:
            data = [book.to_dict() for book in self.books]
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """
        Добавление новой книги в библиотеку
        """
        self.max_book_id += 1
        new_book = Book(self.max_book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id):
        """
        Удаление книги из библиотеки по ID
        """
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                return f"Книга с ID {book_id} удалена."
        raise ValueError("Книга с указанным id не найдена.")

    def search_books(self, search_term):
        """
        Поиск книг
        """
        results = [
            book
            for book in self.books
            if (
                search_term.lower() in book.title.lower()
                or search_term.lower() in book.author.lower()
                or search_term == str(book.year)
            )
        ]
        return results

    def display_books(self):
        for book in self.books:
            print(
                f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
            )

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book.book_id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    return
                else:
                    raise ValueError(
                        "Неверный статус. Используйте 'в наличии' или 'выдана'."
                    )
        raise ValueError("Книга с указанным id не найдена.")
