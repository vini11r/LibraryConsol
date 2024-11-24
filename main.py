from Library import Library


def main():
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, year)
            print("Книга успешно добавлена.")
        elif choice == "2":
            book_id = int(input("Введите id книги для удаления: "))
            try:
                library.remove_book(book_id)
                print("Книга успешно удалена.")
            except ValueError as e:
                print(e)
        elif choice == "3":
            search_term = input("Введите название, автора или год для поиска: ")
            results = library.search_books(search_term)
            if results:
                for book in results:
                    print(
                        f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите id книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            try:
                library.change_status(book_id, new_status)
                print("Статус книги успешно изменён.")
            except ValueError as e:
                print(e)
        elif choice == "6":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()