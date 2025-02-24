from Book2 import *

def Managers_Actions():
    global index1
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    print(log_and_pass_list_m[register_user.index1])
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

            user_data = Create_User(login, password, 'user')

            log_and_pass_list_u.append(user_data)
            index1 = user_data.Return_ID()

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
            Managers_Actions()
        elif yes_or_no_manager == 2:
            print("\nВы вышли из системы менеджера!")
            Start()
            a = False