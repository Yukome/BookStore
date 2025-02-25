from operator import itemgetter

from Import_books import import_books, print_katalog
from Export_books import export_books
from Users import Create_User, Create_Manager

list_of_books = import_books()

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

def register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number):
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
        index1 = user_data.Return_ID() - 1
        Managers_Act(index1)
    else:
        user_data = Create_User(login, password, 'user')
        log_and_pass_list_u.append(user_data)
        index1 = user_data.Return_ID() - 1
        Users_Act(index1)

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
        Managers_Act(index1)
        return

    elif manager_or_user == 2:
        user_data = next((u for u in log_and_pass_list_u if u.login == login and u.password == password), None)

        try:
            if user_data is None:
                raise CustomError("Неверный логин или пароль!")
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        index1 = user_data.Return_ID() - 1
        Users_Act(index1)
        return

def error_manager(choice_manager, addition):
    if choice_manager not in ('0', '1', '2', '3', '4') and addition == False:
        raise CustomError("\nТакого действия нет! Попробуйте еще раз!")
    if choice_manager not in ('0', '1', '2', '3', '4', '5') and addition == True:
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
                if isinstance(book_data, list):
                    if book_data[0] == book:
                        return True
                else:
                    if book_data.name == book:
                        return True
    return False

def Filter(list_of_books):
    global sorted_books
    print_katalog(list_of_books)
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

    ind_b = 0
    for genre_data in list_of_books:
        if genre in genre_data:
            gen1 = genre_data[genre]
            for book_data in gen1:
                if book_data.name == book:
                    ind_b = book_data.cost
                    break
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

def Users_Act(index1):
    global login, password
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    def error_log(login, alphabet):
        if not alphabet.isdisjoint(login.lower()):
            raise CustomError("Логин может содержать только латинские буквы, цифры и символы!")
        if len(login) < 4:
            raise CustomError("Логин не может быть короче 4 символов!")

    def error_pass(password, alphabet):
        if not alphabet.isdisjoint(password.lower()):
            raise CustomError("Пароль может содержать только латинские буквы, цифры и символы!")
        if len(password) < 4:
            raise CustomError("Пароль не может быть короче 4 символов!")

    user1 = log_and_pass_list_u[index1]
    print(user1.get_full_inf())
    print("=====================================================")
    print("\nДобро пожаловать в учетную запись пользователя!")
    print("\nВыберите действие: ")
    print("\n0 - ВЫХОД"
          "\n1 - Каталог товаров"
          "\n2 - Посмотреть профиль или изменить его"
          "\n3 - Корзина"
          "\n4 - Добавить товар в корзину")

    a = True
    while a:
        choice_user = input("Номер действия: ")
        try:
            error_manager(choice_user, False)
            choice_user = int(choice_user)
        except CustomError as e:
            print(e)
            continue

        if choice_user == 0:
            a = False
        elif choice_user == 1:
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть каталог товаров"
                  "\n2 - Отфильтровать каталог товаров")
            a2 = True
            choice_user2 = 0
            while a2:
                try:
                    choice_user2 = int(input("Номер действия: "))
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
                    continue

                if choice_user2 not in (1, 2):
                    print("\nНеверный номер действия!")
                    continue
                a2 = False
            if choice_user2 == 1:
                print_katalog(list_of_books)
            elif choice_user2 == 2:
                Filter(list_of_books)

        elif choice_user == 2:
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть профиль"
                  "\n2 - Изменить профиль")

            a2 = True
            choice_user2 = 0
            while a2:
                try:
                    choice_user2 = int(input("Номер действия: "))
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
                    continue

                if choice_user2 not in (1, 2):
                    print("\nНеверный номер действия!")
                    continue
                a2 = False

            if choice_user2 == 1:
                user = log_and_pass_list_u[index1]
                print(user.get_full_inf())

            elif choice_user2 == 2:
                print("\nЧто вы хотите изменить: ")
                print("\n1 - Логин"
                      "\n2 - Пароль")

                a2 = True
                ans = 0
                while a2:
                    try:
                        ans = int(input("Введите номер действия: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                        continue

                    if ans not in (1, 2):
                        print("\nТакого действия нет!")
                        continue
                    a2 = False

                if ans == 1:
                    a2 = True
                    while a2:
                        login = input("\nВведите новый логин (не менее 4 символов): ")
                        try:
                            error_log(login, alphabet)
                            a2 = False
                        except CustomError as e:
                            print(e)

                    log_and_pass_list_u[index1].login = login

                elif ans == 2:
                    a2 = True
                    while a2:
                        password = input("\nВведите новый пароль (не менее 4 символов): ")
                        try:
                            error_pass(password, alphabet)
                            a2 = False
                        except CustomError as e:
                            print(e)
                    log_and_pass_list_u[index1].password = password

        elif choice_user == 3:
            print("=====================================================")
            shopping_cart = log_and_pass_list_u[index1].shopping_cart
            if not shopping_cart:
                print("\nКорзина пуста")
            else:
                for i in shopping_cart:
                    print(i)

        elif choice_user == 4:
            print("=====================================================")
            print_katalog(list_of_books)
            shopping_cart = add_book(list_of_books, index1, log_and_pass_list_u)

        a3 = True
        yes_or_no_user = 0
        while a3:
            try:
                yes_or_no_user = int(input("Хотите продолжить в качестве пользователя? (1 - да, 2 - нет): "))
                if yes_or_no_user not in (1, 2):
                    print("\nТакого ответа нет!")
                    continue
                a3 = False
            except ValueError:
                print("\nВведите номер ответа, а не текст!")

        if yes_or_no_user == 1:
            Users_Act(index1)
        elif yes_or_no_user == 2:
            print("\nВы вышли из системы пользователя!")
            Start()
            a = False

def Managers_Act(index1):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    user1 = log_and_pass_list_m[index1]
    print(user1.get_full_inf())
    print("=====================================================")
    print("\nДобро пожаловать в учетную запись менеджера!")
    print("\nВыберите действие: ")
    print("\n0 - ВЫХОД"
          "\n1 - Каталог товаров"
          "\n2 - Добавление пользователя"
          "\n3 - Просмотр данных пользователя"
          "\n4 - Просмотр профиля"
          "\n5 - Добавить товар")
    a = True
    while a:
        choice_manager = input("Номер действия: ")
        try:
            error_manager(choice_manager, True)
        except CustomError as e:
            print(e)
            continue

        if choice_manager == '0':
            a = False
        elif choice_manager == '1':
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть или отфильтровать каталог товаров"
                  "\n2 - Изменить каталог товаров"
                  "\n3 - Удалить товар")
            a2 = True
            choice_manager2 = 0
            while a2:
                try:
                    choice_manager2 = int(input("Номер действия: "))
                    if not 1 <= choice_manager2 <= 3:
                        print("\nНеверный номер действия!")
                        continue
                    a2 = False
                except ValueError:
                    print("\nВведите номер действия, а не текст!")

            if choice_manager2 == 1:
                print("\nЧто вы хотите изменить:")
                print("\n1 - Просмотреть имеющийся каталог"
                      "\n2 - Отфильтровать каталог")
                a2 = True
                ans = 0
                while a2:
                    try:
                        ans = int(input("Введите номер действия: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                    if ans not in (1, 2):
                        print("\nТакого действия нет!")
                        continue
                    a2 = False
                if ans == 1:
                    print_katalog(list_of_books)
                elif ans == 2:
                    Filter(list_of_books)

            elif choice_manager2 == 2:
                print_katalog(list_of_books)
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
                change = 0
                while a2:
                    try:
                        print("\nЧто вы хотите изменить:")
                        print("\n1 - Автора"
                              "\n2 - Стоимость"
                              "\n3 - Рейтинг")
                        change = int(input("\nВыберите действие: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                    if change not in (1, 2, 3):
                        print("\nТакого действия нет!")
                        continue
                    a2 = False

                for genre_data in list_of_books:
                    if genre in genre_data:
                        books = genre_data[genre]
                        for book_data in books:
                            if book == book_data.name:
                                if change == 1:
                                    autor1 = input("На какого автора вы хотите заменить: ")
                                    if isinstance(book_data, list):
                                        book_data[1] = autor1
                                    else:
                                        book_data.autor = autor1
                                elif change == 2:
                                    s = True
                                    cost1 = 0
                                    while s:
                                        try:
                                            cost1 = int(input("На какую стоимость вы хотите заменить: "))
                                        except ValueError:
                                            print("\nВведите стоимость, а не текст!")
                                            continue
                                        s = False
                                    if isinstance(book_data, list):
                                        book_data[2] = cost1
                                    else:
                                        book_data.cost = cost1
                                elif change == 3:
                                    s = True
                                    rating1 = float(0)
                                    while s:
                                        try:
                                            rating1 = float(input("На какой рейтинг вы хотите заменить: "))
                                        except ValueError:
                                            print("\nВведите рейтинг с плавающей точкой, а не текст!")
                                            continue
                                        s = False
                                    if isinstance(book_data, list):
                                        book_data[3] = rating1
                                    else:
                                        book_data.rating = rating1
                                break
                        break

                print_katalog(list_of_books)
                export_books(list_of_books)

            elif choice_manager2 == 3:
                print_katalog(list_of_books)
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
                for genre_data in list_of_books:
                    if genre in genre_data:
                        books = genre_data[genre]
                        for i in books:
                            if isinstance(i, list):
                                if i[0] == book:
                                    books.remove(i)
                                    break
                            else:
                                if i.name == book:
                                    books.remove(i)
                                    break
                        break

                print_katalog(list_of_books)
                export_books(list_of_books)

        elif choice_manager == '2':
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

            user_data = Create_User(login, password, 'user')

            log_and_pass_list_u.append(user_data)
            index1 = user_data.Return_ID() - 1

            print("\nВы добавили нового пользователя!")
            print(f"Данные пользователя: {log_and_pass_list_u[-1]}")

        elif choice_manager == '3':
            def error_login(login, log_and_pass_list):
                if not any(u.login == login for u in log_and_pass_list):
                    raise CustomError("Неверный логин!")

            a2 = True
            login_user = ""
            while a2:
                try:
                    login_user = input("Введите логин пользователя, которого вы хотите просмотреть: ")
                    error_login(login_user, log_and_pass_list_u)
                    a2 = False
                except CustomError as e:
                    print(e)

            for user_data in log_and_pass_list_u:
                if user_data.login == login_user:
                    print(user_data.get_full_inf())
                    break

            for user_data in log_and_pass_list_u:
                if user_data.login == login_user:
                    print(Create_User.get_full_inf)
                    break
        elif choice_manager == '4':
            user = log_and_pass_list_m[index1]
            print(user.get_full_inf())
        elif choice_manager == '5':
            print_katalog(list_of_books)
            genre = input("\nВыберите жанр: ").strip().capitalize()
            a2 = True
            while a2:
                if not check_genre(genre, list_of_books):
                    print("\nТакого жанра нет!")
                    genre = input("\nВыберите жанр: ").strip().capitalize()
                else:
                    a2 = False
            book = input("\nВведите название нового произведения: ").strip().capitalize()
            for genre_data in list_of_books:
                if genre in genre_data:
                    books = genre_data[genre]
                    for book_data in books:
                        if isinstance(book_data, list):
                            book_data[0] = book
                            autor1 = input("Введите автора нового произведения: ")
                            book_data[1] = autor1
                            s = True
                            cost1 = 0
                            while s:
                                try:
                                    cost1 = int(input("Введите стоимость нового произведения: "))
                                except ValueError:
                                    print("\nВведите стоимость, а не текст!")
                                    continue
                                s = False
                            book_data[2] = cost1
                            s = True
                            rating1 = float(0)
                            while s:
                                try:
                                    rating1 = float(input("Введите рейтинг нового произведения: "))
                                except ValueError:
                                    print("\nВведите рейтинг с плавающей точкой, а не текст!")
                                    continue
                                s = False
                            book_data[3] = rating1
                            break
                        else:
                            book_data.name = book
                            autor1 = input("Введите автора нового произведения: ")
                            book_data.autor = autor1
                            s = True
                            cost1 = 0
                            while s:
                                try:
                                    cost1 = int(input("Введите стоимость нового произведения: "))
                                except ValueError:
                                    print("\nВведите стоимость, а не текст!")
                                    continue
                                s = False
                            book_data.cost = cost1
                            s = True
                            rating1 = float(0)
                            while s:
                                try:
                                    rating1 = float(input("Введите рейтинг нового произведения: "))
                                except ValueError:
                                    print("\nВведите рейтинг с плавающей точкой, а не текст!")
                                    continue
                                s = False
                            book_data.rating = rating1
                            break
                    break
            print_katalog(list_of_books)
            export_books(list_of_books)

        a3 = True
        yes_or_no_manager = 0
        while a3:
            try:
                yes_or_no_manager = int(input("Хотите продолжить в качестве менеджера? (1 - да, 2 - нет): "))
                if yes_or_no_manager not in (1, 2):
                    print("\nТакого ответа нет!")
                    continue
                a3 = False
            except ValueError:
                print("\nВведите номер ответа, а не текст!")
        if yes_or_no_manager == 1:
            Managers_Act(index1)
        elif yes_or_no_manager == 2:
            print("\nВы вышли из системы менеджера!")
            Start()
            a = False

print("\nДобро пожаловать в книжный магазин!")
log_and_pass_list_u = []
log_and_pass_list_m = []
examination_number = [1234, 2256, 1569]
f = 0

def Start():
    if not log_and_pass_list_u and not log_and_pass_list_m:
        register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number)

    while True:
        try:
            continue_or_not = int(input("Хотите продолжить? (1 - да, 2 - нет): "))
            error_regist(continue_or_not)
            if continue_or_not == 2:
                exit()
        except ValueError:
            print("\nВведите номер ответа, а не текст!")
            continue
        except CustomError as e:
            print(e)
            continue

        print("=====================================================")
        print("\nВойти в существующий аккаунт - 1")
        print("\nЗарегистрироваться как новый пользователь - 2")

        while True:
            try:
                sign_in_or_regist = int(input("\nВыберите действие: "))
                if sign_in_or_regist not in (1, 2):
                    print("\nТакого действия нет!")
                    continue
                break
            except ValueError:
                print("\nВведите номер действия, а не текст!")

        if sign_in_or_regist == 1:
            sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)
        elif sign_in_or_regist == 2:
            register_user(log_and_pass_list_u, log_and_pass_list_m, examination_number)

if f == 0:
    Start()
    f += 1