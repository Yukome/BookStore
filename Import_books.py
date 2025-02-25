import json
from Create_Products import Create_Prod

def import_books():
    with open('Import.json', 'r', encoding='utf-8') as file:
        list_of_books = json.load(file)
        for genre in list_of_books:
            genre = list(genre.values())
            for books in genre:
                for book in books:
                    ind = books.index(book)
                    new_book = Create_Prod(book[0], book[1], book[2], book[3])
                    books[ind] = new_book
    return list_of_books

def print_katalog(list_of_books):
    count_genre = 0
    for genre in list_of_books:
        key = list(genre.keys())[0]
        print(f"\n{key}: ")
        value = list(genre.values())
        for i in value:
            for book in i:
                book_index = i.index(book)
                book_print = list_of_books[count_genre][key][book_index]
                if isinstance(list_of_books[count_genre][key][book_index], list):
                    print(f"Название: {book_print[0]}, Автор: {book_print[1]}, Цена: {str(book_print[2])}, Рейтинг: {str(book_print[3])}")
                else:
                    print(book_print.get_full_inf())
        count_genre += 1