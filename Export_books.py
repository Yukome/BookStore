import json
from Create_Products import Create_Prod

def export_books(list_of_books):
    with open('Export.json', 'w', encoding='utf-8') as file:
        for genre in list_of_books:
            genre = list(genre.values())
            for books in genre:
                for book in books:
                    if isinstance(book, list):
                        books[books.index(book)] = [book[0], book[1], book[2], book[3]]
                    else:
                        books[books.index(book)] = [book.name, book.autor, book.cost, book.rating]
        json.dump(list_of_books, file, indent='\t', ensure_ascii=False)