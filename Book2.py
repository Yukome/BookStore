from operator import itemgetter

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

    user_data = {
        'login': login,
        'password': password,
        'role': 'manager' if manager_or_user == 1 else 'user',
    }

    if manager_or_user == 1:
        user_data['cod'] = examination
        log_and_pass_list_m.append(user_data)
        index1 = len(log_and_pass_list_m) - 1
        Manager(log_and_pass_list_u, log_and_pass_list_m, index1, examination_number, list_of_books)
    else:
        user_data['shopping cart'] = []
        log_and_pass_list_u.append(user_data)
        index1 = len(log_and_pass_list_u) - 1
        User(log_and_pass_list_u, index1, list_of_books)

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

        user_data = next((u for u in log_and_pass_list_m if u['login'] == login and u['password'] == password and u['cod'] == examination), None)

        try:
            if user_data is None:
                raise CustomError("Неверный логин, пароль или код сотрудника!")
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        index1 = log_and_pass_list_m.index(user_data)
        Manager(log_and_pass_list_u, log_and_pass_list_m, index1, examination_number, list_of_books)
        return

    elif manager_or_user == 2:
        user_data = next((u for u in log_and_pass_list_u if u['login'] == login and u['password'] == password), None)

        try:
            if user_data is None:
                raise CustomError("Неверный логин или пароль!")
        except CustomError as e:
            print(e)
            return sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, list_of_books)

        index1 = log_and_pass_list_u.index(user_data)
        User(log_and_pass_list_u, index1, list_of_books)
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
    shopping_cart = ind.get('shopping cart')
    if shopping_cart is None:
        ind['shopping cart'] = []
    shopping_cart = ind['shopping cart']

    existing_book = next((item for item in shopping_cart if item[0] == book), None)

    if existing_book:
        existing_book[1] += number_of_book
        existing_book[2] = existing_book[1] * ind_b
    else:
        shopping_cart.append([book, number_of_book, number_of_book * ind_b])
    print(f"\nКнига '{book}' успешно добавлена в корзину!")
    return shopping_cart

def Manager(log_and_pass_list_u, log_and_pass_list_m, index1, examination_number, list_of_books):
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    print(log_and_pass_list_m[index1])
    print("=====================================================")
    print("\nДобро пожаловать в учетную запись менеджера!")
    print("\nВыберите действие: ")
    print("\n0 - ВЫХОД"
          "\n1 - Каталог товаров"
          "\n2 - Добавление пользователя"
          "\n3 - Просмотр данных пользователя"
          "\n4 - Добавить товар")
    a = True
    while a:
        choice_manager = input("Номер действия: ")
        try:
            error_manager(choice_manager)
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
                    for i in list_of_books:
                        print(i)
                        print("---------------------------------------------------------------------------")
                elif ans == 2:
                    Filter(list_of_books)

            elif choice_manager2 == 2:
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
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
                            if book in book_data:
                                if change == 1:
                                    autor1 = input("На какого автора вы хотите заменить: ")
                                    book_data[1] = autor1
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
                                    book_data[2] = cost1
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
                                    book_data[3] = rating1
                                break
                        break

                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")

            elif choice_manager2 == 3:
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
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
                            if i[0] == book:
                                books.remove(i)
                                break
                        break

                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")

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

            user_data = {'login': login, 'password': password, 'role': 'user', 'shopping cart': []}

            log_and_pass_list_u.append(user_data)
            index1 = len(log_and_pass_list_u) - 1

            print("\nВы добавили нового пользователя!")
            print(f"Данные пользователя: {log_and_pass_list_u[-1]}")

        elif choice_manager == '3':
            def error_login(login, log_and_pass_list):
                if not any(u['login'] == login for u in log_and_pass_list):
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
                if user_data['login'] == login_user:
                    print(user_data)
                    break
        elif choice_manager == '4':
            for i in list_of_books:
                print(i)
                print("---------------------------------------------------------------------------")
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
                    break
            for i in list_of_books:
                print(i)
                print("---------------------------------------------------------------------------")

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
            Manager(log_and_pass_list_u, log_and_pass_list_m, index1, examination_number, list_of_books)
        elif yes_or_no_manager == 2:
            print("\nВы вышли из системы менеджера!")
            Start()
            a = False

def User(log_and_pass_list_u, index1, list_of_books):
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

    print(log_and_pass_list_u[index1])
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
            error_manager(choice_user)
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
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
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
                print(log_and_pass_list_u[index1])
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

                    log_and_pass_list_u[index1]['login'] = login

                elif ans == 2:
                    a2 = True
                    while a2:
                        password = input("\nВведите новый пароль (не менее 4 символов): ")
                        try:
                            error_pass(password, alphabet)
                            a2 = False
                        except CustomError as e:
                            print(e)
                    log_and_pass_list_u[index1]['password'] = password

        elif choice_user == 3:
            print("=====================================================")
            shopping_cart = log_and_pass_list_u[index1].get('shopping cart', [])
            if not shopping_cart:
                print("\nКорзина пуста")
            else:
                for i in shopping_cart:
                    print(i)

        elif choice_user == 4:
            print("=====================================================")
            for i in list_of_books:
                print(i)
                print("---------------------------------------------------------------------------")
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
            User(log_and_pass_list_u, index1, list_of_books)
        elif yes_or_no_user == 2:
            print("\nВы вышли из системы пользователя!")
            Start()
            a = False

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