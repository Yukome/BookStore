from operator import itemgetter

from Managers_Actions import Managers_Actions
from Users import Create_User, Create_Manager
from Users_Actions import Users_Actions


class CustomError(Exception):
    pass

def error_log_pass(login, password, alphabet):
    if not alphabet.isdisjoint(login.lower()):
        raise CustomError("Логин может содержать только латинские буквы, цифры и символы!")
    if not alphabet.isdisjoint(password.lower()):
        raise CustomError("Пароль может содержать только латинские буквы, цифры и символы!")
    if len(login) < 4 or len(password) < 4:
        raise CustomError("Логин и пароль не могут быть короче 4 символов!")

def error_sign_in(login, password, user_data):
    if user_data is None or user_data['login'] != login or user_data['password'] != password:
        raise CustomError("Неверный логин или пароль!")

def error_regist(moru):
    if moru not in (1, 2):
        raise CustomError("\nТакого ответа нет! Попробуйте еще раз!")

def reg(examination, examination_number):
    if examination not in examination_number:
        raise CustomError("\nНеверный код сотрудника!")

def register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books):
    global manager_or_user
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    print("=====================================================")
    print("\n====Зарегистрируйтесь в системе====")
    print("\nМенеджер - 1")
    print("\nПользователь - 2")

    a2 = True
    while a2:
        try:
            manager_or_user = int(input("\nВыберите тип аккаунта: "))
            error_regist(manager_or_user)
            a2 = False
        except ValueError:
            print("\nВведите корректный номер типа аккаунта, а не текст!")
        except CustomError as e:
            print(e)

    examination = None
    if manager_or_user == 1:
        a2 = True
        while a2:
            try:
                examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
                reg(examination, examination_number)
                a2 = False
            except ValueError:
                print("\nВведите код сотрудника, а не текст!")
            except CustomError as e:
                print(e)

    print("=====================================================")
    a2 = True
    login = ""
    password = ""
    while a2:
        try:
            login = input("\nВведите логин (не менее 4 символов): ")
            password = input("\nВведите пароль (не менее 4 символов): ")
            error_log_pass(login, password, alphabet)
            a2 = False
        except CustomError as e:
            print(e)

    if manager_or_user == 1:
        user_data = Create_Manager(examination, login, password, 'manager')
        log_and_pass_list_m.append(user_data)
        index1 = user_data.Return_ID()
        Managers_Actions()
    else:
        user_data = Create_User(login, password, 'user')
        log_and_pass_list_u.append(user_data)
        index1 = user_data.Return_ID()
        Users_Actions()

def sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books):
    global manager_or_user, examination

    print("=====================================================")
    print("\n====Войдите в систему====")
    print("\nМенеджер - 1")
    print("\nПользователь - 2")

    a = True
    while a:
        try:
            manager_or_user = int(input("\nВыберите тип аккаунта: "))
            error_regist(manager_or_user)
            a = False
        except ValueError:
            print("\nВведите номер типа аккаунта, а не текст!")
        except CustomError as e:
            print(e)

    login = input("\nВведите логин: ")
    password = input("\nВведите пароль: ")

    if manager_or_user == 1:
        try:
            examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
        except ValueError:
            print("\nВведите код сотрудника, а не текст!")
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        try:
            reg(examination, examination_number)
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        user_data = next((u for u in log_and_pass_list_m if u.login == login and u.password == password and u.cod == examination), None)

        try:
            if user_data is None:
                raise CustomError("Неверный логин, пароль или код сотрудника!")
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        index1 = user_data.Return_ID()
        Managers_Actions()
        return

    elif manager_or_user == 2:
        user_data = next((u for u in log_and_pass_list_u if u.login == login and u.password == password), None)

        try:
            if user_data is None:
                raise CustomError("Неверный логин или пароль!")
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        index1 = user_data.Return_ID()
        Users_Actions()
        return

def error_manager(choice_manager):
    if choice_manager not in ('0', '1', '2', '3', '4'):
        raise CustomError("\nТакого действия нет! Попробуйте еще раз!")

def check_genre(genre, list_of_books):
    for genre_data in list_of_books:
        if genre in genre_data:
            return True
    return False

def check_book(genre, book, list_of_books):
    for genre_data in list_of_books:
        if genre in genre_data:
            gen1 = genre_data[genre]
            for book_data in gen1:
                if book in book_data:
                    return True
    return False

def Filter(list_of_books):
    global sorted_books
    for i in list_of_books:
        print(i)
        print("---------------------------------------------------------------------------")
    genre = input("\nВыберите жанр: ")
    genre = genre.strip().capitalize()
    a2 = True
    while a2:
        chk_g = check_genre(genre, list_of_books)
        if not chk_g:
            print("\nТакого жанра нет!")
            genre = input("\nВыберите жанр: ")
            genre = genre.strip().capitalize()
        else:
            a2 = False
    print("\nКак вы хотите отфильтровать каталог:")
    print("\n1 - Отфильтровать по возрастанию в цене"
          "\n2 - Отфильтровать по убыванию в цене"
          "\n3 - Вывод произведений больше определенной цены"
          "\n4 - Вывод произведений меньше определенной цены"
          "\n5 - Отфильтровать по возрастанию рейтинга"
          "\n6 - Отфильтровать по убыванию рейтинга"
          "\n7 - Вывод произведений больше определенного рейтинга"
          "\n8 - Вывод произведений меньше определенного рейтинга")
    a2 = True
    ans = 0
    while a2:
        try:
            ans = int(input("Введите номер действия: "))
        except ValueError:
            print("\nВведите номер действия, а не текст!")
        if not 1 <= ans <= 8:
            print("\nТакого действия нет!")
            continue
        a2 = False

    for genre_data in list_of_books:
        if genre in genre_data:
            books = genre_data[genre]
            if ans == 1:
                sorted_books = sorted(books, key=itemgetter(2))
            elif ans == 2:
                sorted_books = sorted(books, key=itemgetter(2), reverse=True)
            elif ans == 3:
                a2 = True
                while a2:
                    try:
                        ans2 = int(input("Введите стоимость, больше которой вы хотите вывести произведения: "))
                        if ans2 <= 0:
                            print("\nТакой стоимости нет!")
                            continue
                        a2 = False
                    except ValueError:
                        print("\nВведите стоимость, а не текст!")
                sorted_books = filter(lambda x: x[2] > ans2, books)
            elif ans == 4:
                a2 = True
                while a2:
                    try:
                        ans2 = int(input("Введите стоимость, меньше которой вы хотите вывести произведения: "))
                        if ans2 <= 0:
                            print("\nТакой стоимости нет!")
                            continue
                        a2 = False
                    except ValueError:
                        print("\nВведите стоимость, а не текст!")
                sorted_books = filter(lambda x: x[2] < ans2, books)
            elif ans == 5:
                sorted_books = sorted(books, key=itemgetter(3))
            elif ans == 6:
                sorted_books = sorted(books, key=itemgetter(3), reverse=True)
            elif ans == 7:
                a2 = True
                while a2:
                    try:
                        ans2 = float(input("Введите рейтинг, больше которого вы хотите вывести произведения: "))
                        if not 0 < ans2 <= 5:
                            print("\nТакого рейтинга нет!")
                            continue
                        a2 = False
                    except ValueError:
                        print("\nВведите рейтинг с плавающей точкой, а не текст!")
                sorted_books = filter(lambda x: x[3] > ans2, books)
            elif ans == 8:
                a2 = True
                while a2:
                    try:
                        ans2 = float(input("Введите рейтинг, меньше которого вы хотите вывести произведения: "))
                        if not 0 < ans2 <= 5:
                            print("\nТакого рейтинга нет!")
                            continue
                        a2 = False
                    except ValueError:
                        print("\nВведите рейтинг с плавающей точкой, а не текст!")
                sorted_books = filter(lambda x: x[3] < ans2, books)

            for book in sorted_books:
                print(book)
            break

def add_book(list_of_books, index1, log_and_pass_list):
    genre = input("\nВыберите жанр: ").strip().capitalize()
    a2 = True
    while a2:
        if not check_genre(genre, list_of_books):
            print("\nТакого жанра нет!")
            genre = input("\nВыберите жанр: ").strip().capitalize()
        else:
            a2 = False

    book = input("\nВыберите произведение: ").strip().capitalize()
    a2 = True
    while a2:
        if not check_book(genre, book, list_of_books):
            print("\nТакого произведения нет!")
            book = input("\nВыберите произведение: ").strip().capitalize()
        else:
            a2 = False

    a2 = True
    number_of_book = 0
    while a2:
        try:
            number_of_book = int(input("Укажите количество: "))
            a2 = False
        except ValueError:
            print("\nВведите количество, а не текст!")

    ind_b = ""
    for genre_data in list_of_books:
        if genre in genre_data:
            gen1 = genre_data[genre]
            book_data = next((b for b in gen1 if book in b), None)
            if book_data:
                ind_b = book_data[2]
                break

    ind = log_and_pass_list[index1]
    shopping_cart = ind.shopping_cart
    if shopping_cart is None:
        ind.shopping_cart = []
    shopping_cart = ind.shopping_cart

    existing_book = next((item for item in shopping_cart if item[0] == book), None)

    if existing_book:
        existing_book[1] += number_of_book
        existing_book[2] = existing_book[1] * ind_b
    else:
        shopping_cart.append([book, number_of_book, number_of_book * ind_b])
    print(f"\nКнига '{book}' успешно добавлена в корзину!")
    return shopping_cart

print("\nДобро пожаловать в книжный магазин!")
log_and_pass_list_u = []
log_and_pass_list_m = []
list_of_books = [{'Современная проза': [['Если все кошки в мире исчезнут', 'Гэнки Кавамура', 332, 4.4], ['Норвежский лес', 'Харуки Мураками', 424, 4.1], ['Круть', 'Виктор Пелевин', 1288, 3.7], ['Бог всегда путешествует инкогнито', 'Лоран Гунель', 314, 4.2], ['Собаки и другие люди', 'Захар Прилепин', 1334, 4.2]]},
            {'Фентези': [['Ужасы фазбера', 'Скотт Коутон', 672, 4.0], ['Злодейский путь', 'Эл Моргот', 1243, 4.7], ['Мара и морок', 'Лия Арден', 721, 4.2], ['Белая рыба', 'Шу Гу', 696, 4.8], ['Повелитель тайн', 'Е Юань', 790, 4.9]]},
            {'Детектив': [['Странные игры', 'Майк Омер', 749, 4.7], ['Дикий зверь', 'Жоэль Диккер', 1236, 4.8], ['Убийства по алфавиту', 'Агата Кристи', 370, 4.3], ['Колодец и бабочка', 'Елена Михалкова', 814, 4.7], ['Черный кофе', 'Агата Кристи', 370, 4.4]]},
            {'Любовные романы': [['Твое сердце будет разбито', 'Анна Джейн', 313, 4.2], ['Поклонник', 'Анна Джейн', 398, 4.2], ['Спеши любить', 'Николас Спаркс', 314, 4.3], ['Шах и мат', 'Али Хейзелвуд', 846, 4.4], ['Миля над землей', 'Лиз Томфорд', 847, 4.7]]},
            {'Классическая проза': [['1984', 'Джордж Оруэлл', 305, 4.1], ['Человек недостойный', 'Дадзай Осаму', 255, 4.5], ['Преступление и наказание', 'Федор Достоевский', 297, 4.2], ['Три товарища', 'Эрих Ремарк', 390, 4.2], ['Портрет дориана грея', 'Оскар Уайльд', 255, 4.2]]}]
examination_number = [1234, 2256, 1569]
f = 0

def Start():
    if not log_and_pass_list_u and not log_and_pass_list_m:
        register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

    contin = True
    while contin:
        try:
            continue_or_not = int(input("Хотите продолжить? (1 - да, 2 - нет): "))
            error_regist(continue_or_not)
            if continue_or_not == 2:
                contin = False
                break
        except ValueError:
            print("\nВведите номер ответа, а не текст!")
        except CustomError as e:
            print(e)
            continue

        print("=====================================================")
        print("\nВойти в существующий аккаунт - 1")
        print("\nЗарегистрироваться как новый пользователь - 2")

        a = True
        sign_in_or_regist = 0
        while a:
            try:
                sign_in_or_regist = int(input("\nВыберите действие: "))
            except ValueError:
                print("\nВведите номер действия, а не текст!")
                continue

            if sign_in_or_regist not in (1, 2):
                print("\nТакого действия нет!")
                continue
            a = False

        if sign_in_or_regist == 1:
            sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)
        elif sign_in_or_regist == 2:
            register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

if f == 0:
    Start()
    f += 1