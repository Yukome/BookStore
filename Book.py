from operator import itemgetter, index

class CustomError(Exception):
    pass

def error_log_pass(login, password, alphabet):
    if not alphabet.isdisjoint(login.lower()) == True:
        raise CustomError("Логин может содержать только латинские буквы, цифры и символы!")
    if not alphabet.isdisjoint(password.lower()) == True:
        raise CustomError("Пароль может содержать только латинские буквы, цифры и символы!")
    if len(login) < 4 or len(password) < 4:
        raise CustomError("Логин и пароль не может быть короче 4 символов!")

def error_sign_in(login, password, log_and_pass_list):
    a = 0
    b = 0
    for i in log_and_pass_list:
        if log_and_pass_list[i]['login'] == login:
            a += 1
        if log_and_pass_list[i]['password'] == password:
            b += 1
    if a == 0:
        raise CustomError("Неверный логин!")
    elif b == 0:
        raise CustomError("Неверный пароль!")

def error_regist(moru):
    if moru != 1 and moru != 2:
        raise CustomError("\nТакого ответа нет! Попробуйте еще раз!")

def reg(examination):
    if examination not in examination_number:
        raise CustomError("\nНеверный код сотрудника!")

def registration(log_and_pass_list_u,log_and_pass_list_m, examination_number):
    global manager_or_user
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    print("=====================================================")
    print("\n====Зарегистрируйтесь в системе====")
    print("\nМенеджер - 1")
    print("\nПользователь - 2")
    a2 = True
    while a2 == True:
        try:
            manager_or_user = int(input("\nВыберите тип аккаунта: "))
            if manager_or_user != 1 and manager_or_user != 2:
                error_regist(manager_or_user)
            error_regist(manager_or_user)
            a2 = False
        except ValueError:
            print("\nВведите корректный номер типа аккаунта, а не текст!")
        except CustomError as e:
            print(e)
    if manager_or_user == 1:
        a2 = True
        while a2 == True:
            try:
                examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
                reg(examination)
                a2 = False
            except ValueError:
                print("\nВведите код сотрудника, а не текст!")
            except CustomError as e:
                print(e)

    print("=====================================================")
    a2 = True
    while a2 == True:
        try:
            login = input("\nВведите логин (не менее 4 символов): ")
            password = input("\nВведите пароль (не менее 4 символов): ")
            if (not alphabet.isdisjoint(login.lower()) == True) or (not alphabet.isdisjoint(password.lower()) == True):
                error_log_pass(login, password, alphabet)
            elif len(login) < 4 or len(password) < 4:
                error_log_pass(login, password, alphabet)
            a2 = False
        except CustomError as e:
            print(e)

    if manager_or_user == 1:
        log_and_pass_list_m.append({
            'login': login,
            'password': password,
            'cod': examination,
            'role': 'manager'
        })
        index1 = next(x for x in log_and_pass_list_m if x['login'] == login)
        for i in log_and_pass_list_m:
            if i == index1:
                index1 = log_and_pass_list_m.index(i)
        return index1
    elif manager_or_user == 2:
        log_and_pass_list_u.append({
            'login': login,
            'password': password,
            'role': 'user',
            'shopping cart': []
        })
        index1 = next(x for x in log_and_pass_list_u if x['login'] == login)
        for i in log_and_pass_list_u:
            if i == index1:
                index1 = log_and_pass_list_u.index(i)
        return index1

def sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, index1):
    global manager_or_user, examination
    print("=====================================================")
    print("\n====Войдите в систему====")
    print("\nМенеджер - 1")
    print("\nПользователь - 2")
    a = True
    while a == True:
        try:
            manager_or_user = int(input("\nВыберите тип аккаунта: "))
            if manager_or_user != 1 and manager_or_user != 2:
                error_regist(manager_or_user)
            a = False
        except ValueError:
            print("\nВведите номер типа аккаунта, а не текст!")
        except CustomError as e:
            print(e)
    if manager_or_user == 1:
        a2 = True
        while a2 == True:
            try:
                examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
                a2 = False
            except ValueError:
                print("\nВведите код сотрудника, а не текст!")
                examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
            if examination not in examination_number:
                print("\nНеверный код сотрудника!")
        a5 = 0
        i1 = next(x for x in log_and_pass_list_m if x['cod'] == examination)
        a2 = True
        while a2 == True:
            if i1['cod'] == examination:
                a5 += 1
                a2 = False
            if a5 == 0:
                print("\nНеверный код сотрудника!")
                examination = int(input("\nВведите код сотрудника для входа как менеджер: "))
    print("=====================================================")
    b = 0
    while b == 0:
        if manager_or_user == 1:
            login = input("\nВведите логин: ")
            password = input("\nВведите пароль: ")
            for i in log_and_pass_list_m:
                if i == index1:
                    index1 = log_and_pass_list_m.index(i)
                    if (log_and_pass_list_m[index1]['login'] == login) and (log_and_pass_list_m[index1]['password'] == password):
                        b += 1
            if b == 0:
                try:
                    error_sign_in(login, password, log_and_pass_list_m)
                except CustomError as e:
                    print(e)
            else:
                b += 1
            index1 = next(x for x in log_and_pass_list_m if x['login'] == login)
            for i in log_and_pass_list_m:
                if i == index1:
                    index1 = log_and_pass_list_m.index(i)
            return index1
        elif manager_or_user == 2:
            login = input("\nВведите логин: ")
            password = input("\nВведите пароль: ")
            for i in log_and_pass_list_u:
                if i == log_and_pass_list_u[index1]:
                    index1 = log_and_pass_list_u.index(i)
                    if (log_and_pass_list_u[index1]['login'] == login) and (log_and_pass_list_u[index1]['password'] == password):
                        b += 1

            if b == 0:
                try:
                    error_sign_in(login, password, log_and_pass_list_u)
                except CustomError as e:
                    print(e)
            else:
                b += 1
            index1 = next(x for x in log_and_pass_list_u if x['login'] == login)
            for i in log_and_pass_list_u:
                if i == index1:
                    index1 = log_and_pass_list_u.index(i)
            return index1

def error_manager(choice_manager):
    if choice_manager != '0' and choice_manager != '1' and choice_manager != '2' and choice_manager != '3' and choice_manager != '4':
        raise CustomError("\nТакого действия нет! Попробуйте еще раз!")

def check_genre(genre, list_of_books):
    for genre_data in list_of_books:
        if genre in genre_data:
            return True
    return False

def check_book(genre, book, list_of_books):
    for genre_data in list_of_books:
        if genre in genre_data:
            a = True
            if a == True:
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
    while a2 == True:
        chk_g = check_genre(genre, list_of_books)
        if chk_g == False:
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
    while a2 == True:
        try:
            ans = int(input("Введите номер действия: "))
        except ValueError:
            print("\nВведите номер действия, а не текст!")
        if (9 < ans) and (ans < 1):
            print("\nТакого действия нет!")
        a2 = False
    if ans == 1:
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = sorted(books, key=itemgetter(2))
                for book in sorted_books:
                    print(book)
                break
    if ans == 2:
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = sorted(books, key=itemgetter(2), reverse=True)
                for book in sorted_books:
                    print(book)
                break
    if ans == 3:
        a2 = True
        while a2 == True:
            try:
                ans2 = int(input("Введите стоимость, больше которой вы хотите вывести произведения: "))
            except ValueError:
                print("\nВведите стоимость, а не текст!")
            if ans2 <= 0:
                print("\nТакой стоимости нет!")
            a2 = False
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = filter(lambda x: x[2] > ans2, books)
                for book in sorted_books:
                    print(book)
                break
    if ans == 4:
        a2 = True
        while a2 == True:
            try:
                ans2 = int(input("Введите стоимость, меньше которой вы хотите вывести произведения: "))
            except ValueError:
                print("\nВведите стоимость, а не текст!")
            if ans2 <= 0:
                print("\nТакой стоимости нет!")
            a2 = False
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = filter(lambda x: x[2] < ans2, books)
                for book in sorted_books:
                    print(book)
                break
    if ans == 5:
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = sorted(books, key=itemgetter(3))
                for book in sorted_books:
                    print(book)
                break
    if ans == 6:
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = sorted(books, key=itemgetter(3), reverse=True)
                for book in sorted_books:
                    print(book)
                break
    if ans == 7:
        a2 = True
        while a2 == True:
            try:
                ans2 = float(input("Введите рейтинг, больше которого вы хотите вывести произведения: "))
            except ValueError:
                print("\nВведите рейтинг с плавающей точкой, а не текст!")
            if (ans2 <= 0) and (ans2 > 5):
                print("\nТакого рейтинга нет!")
            a2 = False
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = filter(lambda x: x[3] > ans2, books)
                for book in sorted_books:
                    print(book)
                break
    if ans == 8:
        a2 = True
        while a2 == True:
            try:
                ans2 = float(input("Введите рейтинг, меньше которого вы хотите вывести произведения: "))
            except ValueError:
                print("\nВведите рейтинг с плавающей точкой, а не текст!")
            if (ans2 <= 0.0) and (ans2 > 5.0):
                print("\nТакого рейтинга нет!")
            a2 = False
        for genre_data in list_of_books:
            if genre in genre_data:
                books = genre_data[genre]
                sorted_books = filter(lambda x: x[3] < ans2, books)
                for book in sorted_books:
                    print(book)
                break

def add_book(list_of_books, index1, log_and_pass_list):
    global number_of_book, ind2, ind_b
    genre = input("\nВыберите жанр: ")
    genre = genre.strip().capitalize()
    a2 = True
    while a2 == True:
        chk_g = check_genre(genre, list_of_books)
        if chk_g == False:
            print("\nТакого жанра нет!")
            genre = input("\nВыберите жанр: ")
            genre = genre.strip().capitalize()
        else:
            a2 = False
    book = input("\nВыберите произведение: ")
    book = book.strip().capitalize()
    a2 = True
    while a2 == True:
        chk_b = check_book(genre, book, list_of_books)
        if chk_b == False:
            print("\nТакого произведения нет!")
            book = input("\nВыберите произведение: ")
            book = book.strip().capitalize()
        else:
            a2 = False
    a2 = True
    while a2 == True:
        try:
            number_of_book = int(input("Укажите количество: "))
            a2 = False
        except ValueError:
            print("\nВведите количество, а не текст!")
    number_of_book = number_of_book
    for genre_data in list_of_books:
        if genre in genre_data:

            a = True
            if a == True:
                gen1 = genre_data[genre]
                for book_data in gen1:
                    if book in book_data:
                        ind_b = book_data[2]
    ind = log_and_pass_list[index1]
    for i in ind:
        if i == 'shopping cart' and ind[i] != []:
            ind2 = ind[i]
            num = ind2
            d = 0
            for f in num:
                if f[0] == book:
                    d += 1
                    num1 = f[1]
                    number_of_book2 = number_of_book + num1
                    ind2[num.index(f)] = ([book, number_of_book2, number_of_book2 * ind_b])
                break
            if d == 0:
                ind2.append([book, number_of_book, number_of_book * ind_b])
        elif i == 'shopping cart' and ind[i] == []:
            ind2 = ind[i]
            ind2.append([book, number_of_book, number_of_book * ind_b])
    return ind2


def Manager(log_and_pass_list_u, log_and_pass_list_m, index1, list_of_books):
    global choice_manager2, ans, change, login_user
    print(log_and_pass_list_m[index1])
    print("=====================================================")
    print("\nДобро пожаловать в учетную запись менеджера!")
    print("\nВыберите действие: ")
    print("\n0 - ВЫХОД"
          "\n1 - Каталог товаров"
          "\n2 - Добавление пользователя"
          "\n3 - Просмотр данных пользователя")
    a = True
    a2 = True
    while a == True:
        choice_manager = input("Номер действия: ")
        if choice_manager != '0' and choice_manager != '1' and choice_manager != '2' and choice_manager != '3':
            try:
                choice_manager = int(choice_manager)
                error_manager(choice_manager)
            except ValueError:
                print("\nВведите корректный номер действия, а не текст!")
            except CustomError as e:
                print(e)
        elif choice_manager == '0':
            a = False
        elif choice_manager == '1':
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть или отфильтровать каталог товаров"
                  "\n2 - Изменить каталог товаров"
                  "\n3 - Удалить товар"
                  "\n4 - Добавить товар")
            while a2 == True:
                try:
                    choice_manager2 = int(input("Номер действия: "))
                    if choice_manager2 != 1 and choice_manager != 2 and choice_manager != 3:
                        print("\nНеверный номер действия!")
                    a2 = False
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
            if choice_manager2 == 1:
                print("\nЧто вы хотите изменить:")
                print("\n1 - Просмотреть имеющийся каталог"
                      "\n2 - Отфильтровать каталог")
                a2 = True
                while a2 == True:
                    try:
                        ans = int(input("Введите номер действия: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                    if ans != 1 and ans != 2:
                        print("\nТакого действия нет!")
                    a2 = False
                if ans == 1:
                    for i in list_of_books:
                        print(i)
                        print("---------------------------------------------------------------------------")
                if ans == 2:
                    Filter(list_of_books)
            if choice_manager2 == 2:
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
                genre = input("\nВыберите жанр: ")
                genre = genre.strip().capitalize()
                a2 = True
                while a2 == True:
                    chk_g = check_genre(genre, list_of_books)
                    if chk_g == False:
                        print("\nТакого жанра нет!")
                        genre = input("\nВыберите жанр: ")
                        genre = genre.strip().capitalize()
                    else:
                        a2 = False
                book = input("\nВыберите произведение: ")
                book = book.strip().capitalize()
                a2 = True
                while a2 == True:
                    chk_b = check_book(genre, book, list_of_books)
                    if chk_b == False:
                        print("\nТакого произведения нет!")
                        book = input("\nВыберите произведение: ")
                        book = book.strip().capitalize()
                    else:
                        a2 = False
                a2 = True
                while a2 == True:
                    try:
                        print("\nЧто вы хотите изменить:")
                        print("\n1 - Автора"
                              "\n2 - Стоимость"
                              "\n3 - Рейтинг")
                        change = int(input("\nВыберите действие: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                    if change != 1 and change != 2 and change != 3:
                        print("\nТакого действия нет!")
                    a2 = False
                if change == 1:
                    autor1 = input("На какого автора вы хотите заменить: ")
                    res = [cost.get(genre) for cost in list_of_books]
                    res = res[1]
                    for i in res:
                        if book in i:
                            i[1] = autor1
                elif change == 2:
                    s = True
                    while s == True:
                        try:
                            cost1 = int(input("На какую стоимость вы хотите заменить: "))
                        except ValueError:
                            print("\nВведите стоимость, а не текст!")
                        s = False
                    res = [cost.get(genre) for cost in list_of_books]
                    res = res[1]
                    print(res)
                    for i in res:
                        if book in i:
                            i[2] = cost1
                elif change == 3:
                    s = True
                    while s == True:
                        try:
                            rating1 = float(input("На какой рейтинг вы хотите заменить: "))
                        except ValueError:
                            print("\nВведите рейтинг с плавающей точкой, а не текст!")
                        s = False
                    res = [cost.get(genre) for cost in list_of_books]
                    res = res[1]
                    for i in res:
                        if book in i:
                            i[3] = rating1
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
            if choice_manager2 == 3:
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
                genre = input("\nВыберите жанр: ")
                genre = genre.strip().capitalize()
                a2 = True
                while a2 == True:
                    chk_g = check_genre(genre, list_of_books)
                    if chk_g == False:
                        print("\nТакого жанра нет!")
                        genre = input("\nВыберите жанр: ")
                        genre = genre.strip().capitalize()
                    else:
                        a2 = False
                book = input("\nВыберите произведение: ")
                book = book.strip().capitalize()
                a2 = True
                while a2 == True:
                    chk_b = check_book(genre, book, list_of_books)
                    if chk_b == False:
                        print("\nТакого произведения нет!")
                        book = input("\nВыберите произведение: ")
                        book = book.strip().capitalize()
                    else:
                        a2 = False
                res = [cost.get(genre) for cost in list_of_books]
                res = res[1]
                for i in res:
                    if book in i:
                        res.remove(i)
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")
        elif choice_manager == '2':
            print("=====================================================")
            alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            a2 = True
            while a2 == True:
                try:
                    login = input("\nВведите логин (не менее 4 символов): ")
                    password = input("\nВведите пароль (не менее 4 символов): ")
                    if (not alphabet.isdisjoint(login.lower()) == True) or (not alphabet.isdisjoint(password.lower()) == True):
                        error_log_pass(login, password, alphabet)
                    elif (len(login) < 4 or len(password) < 4):
                        error_log_pass(login, password, alphabet)
                    a2 = False
                except CustomError as e:
                    print(e)
            log_and_pass_list_u.append({
                'login': login,
                'password': password,
                'role': 'user',
                'shopping cart': []
            })
            index11 = next((index for (index, d) in enumerate(log_and_pass_list_u) if d['login'] == login), None)
            print("\nВы добавили нового пользователя!")
            print(f"Данные пользователя: {log_and_pass_list_u[index11]}")
        elif choice_manager == '3':
            print("=====================================================")
            def error_login(login, log_and_pass_list):
                a = 0
                for i in log_and_pass_list:
                    if i['login'] == login:
                        a += 1
                if a == 0:
                    raise CustomError("Неверный логин!")
            a2 = True
            while a2 == True:
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
            print("=====================================================")
            for i in list_of_books:
                print(i)
                print("---------------------------------------------------------------------------")
            genre = input("\nВведите название нового жанра или существующего: ")
            genre = genre.strip().capitalize()
            chk_g = check_genre(genre, list_of_books)
            new_book = input("Введите название произведения: ")
            new_autor = input("Введите автора: ")
            a2 = True
            while a2 == True:
                try:
                    new_cost = int(input("Введите стоимость книги: "))
                    if new_cost <= 0:
                        print("\nСтоимость не может быть ниже нуля!")
                        continue
                    a2 = False
                except ValueError:
                    print("\nВведите стоимость книги, а не текст!")
            a2 = True
            while a2 == True:
                try:
                    new_rating = int(input("Введите рейтинг книги: "))
                    if new_rating <= 0.0 and new_rating > 5.0:
                        print("\nРейтинг не может быть ниже нуля и выше 5!")
                        continue
                    a2 = False
                except ValueError:
                    print("\nВведите число с плавующей точкой, а не текст!")
            if chk_g == False:
                list_of_books.append({genre:[[new_book, new_autor, new_cost, new_rating]]})
            else:
                for genre_data in list_of_books:
                    if genre in genre_data:
                        list_of_books[genre_data][genre].append([new_book, new_autor, new_cost, new_rating])
        a3 = True
        while a3 == True:
            try:
                yes_or_no_manager = int(input("Хотите продолжить в качестве менеджера? (1 - да, 2 - нет): "))
                if yes_or_no_manager != 1 and yes_or_no_manager != 2:
                    print("\nТакого ответа нет!")
                    continue
                a3 = False
            except ValueError:
                print("\nВведите номер ответа, а не текст!")
        if yes_or_no_manager == 1:
            Manager(log_and_pass_list_u, log_and_pass_list_m, index1, list_of_books)
        elif yes_or_no_manager == 2:
            print("\nВы вышли из системы менеджера!")
            Start()
            a = False

def User(log_and_pass_list_u, index1, list_of_books):
    global login, password
    alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    def error_log(login, alphabet):
        if not alphabet.isdisjoint(login.lower()) == True:
            raise CustomError("Логин может содержать только латинские буквы, цифры и символы!")
        if len(login) < 4:
            raise CustomError("Логин не может быть короче 4 символов!")
    def error_pass(password, alphabet):
        if not alphabet.isdisjoint(password.lower()) == True:
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
    while a == True:
        choice_user = input("Номер действия: ")
        if choice_user != '0' and choice_user != '1' and choice_user != '2' and choice_user != '3' and choice_user != '4':
            try:
                choice_user = int(choice_user)
                error_manager(choice_user)
            except ValueError:
                print("\nВведите корректный номер действия, а не текст!")
            except CustomError as e:
                print(e)
        elif choice_user == '0':
            a = False
        elif choice_user == '1':
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть каталог товаров"
                  "\n2 - Отфильтровать каталог товаров")
            a2 = True
            while a2 == True:
                try:
                    choice_user2 = int(input("Номер действия: "))
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
                if choice_user2 != 1 and choice_user2 != 2:
                    print("\nНеверный номер действия!")
                a2 = False
            if choice_user2 == 1:
                for i in list_of_books:
                    print(i)
                    print("---------------------------------------------------------------------------")

            elif choice_user2 == 2:
                Filter(list_of_books)
        elif choice_user == '2':
            print("=====================================================")
            print("\nВыберите действие: ")
            print("\n1 - Просмотреть профить"
                  "\n2 - Изменить профиль")
            a2 = True
            while a2 == True:
                try:
                    choice_user2 = int(input("Номер действия: "))
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
                if choice_user2 != 1 and choice_user2 != 2 and choice_user2 != 3:
                    print("\nНеверный номер действия!")
                a2 = False
            if choice_user2 == 1:
                print(log_and_pass_list_u[index1])
            elif choice_user2 == 2:
                print("\nЧто вы хотите изменить: ")
                print("\n1 - Логин"
                      "\n2 - Пароль")
                a2 = True
                while a2 == True:
                    try:
                        ans = int(input("Введите номер действия: "))
                    except ValueError:
                        print("\nВведите номер действия, а не текст!")
                    if ans != 1 and ans != 2:
                        print("\nТакого действия нет!")
                    a2 = False
                if ans == 1:
                    a2 = True
                    while a2 == True:
                        login = input("\nВведите новый логин (не менее 4 символов): ")
                        while (len(login) < 4) or (not alphabet.isdisjoint(login.lower()) == True):
                            try:
                                error_log(login, alphabet)
                            except CustomError as e:
                                print(e)
                        a2 = False
                    log_and_pass_list_u[index1]['login'] = login
                elif ans == 2:
                    a2 = True
                    while a2 == True:
                        password = input("\nВведите новый пароль (не менее 4 символов): ")
                        while (len(password) < 4) or (not alphabet.isdisjoint(password.lower()) == True):
                            try:
                                error_pass(password, alphabet)
                            except CustomError as e:
                                print(e)
                        a2 = False
                    log_and_pass_list_u[index1]['password'] = password
        elif choice_user == '3':
            print("=====================================================")
            shopping_cart = log_and_pass_list_u[index1]['shopping cart']
            if shopping_cart == []:
                print("\nКорзина пуста")
            else:
                for i in shopping_cart:
                    print(i)
        elif choice_user == '4':
            print("=====================================================")
            for i in list_of_books:
                print(i)
                print("---------------------------------------------------------------------------")
            shopping_cart = add_book(list_of_books, index1, log_and_pass_list_u)
            a2 = True
            while a2 == True:
                try:
                    yes_or_no_user1 = int(input("Хотите продолжить покупки? (1 - да, 2 - нет): "))
                    if yes_or_no_user1 != 1 and yes_or_no_user1 != 2:
                        print("\nТакого ответа нет!")
                        continue
                except ValueError:
                    print("\nВведите номер ответа, а не текст!")
                if yes_or_no_user1 == 1:
                    shopping_cart = add_book(list_of_books, index1, log_and_pass_list_u)
                elif yes_or_no_user1 == 2:
                    print("=====================================================")
                    print("\nВаш заказ: ")
                    for i in shopping_cart:
                        print(i)
                    a2 = False
        a3 = True
        while a3 == True:
            try:
                yes_or_no_user = int(input("Хотите продолжить в качестве пользователя? (1 - да, 2 - нет): "))
                if yes_or_no_user != 1 and yes_or_no_user != 2:
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
    global index1, continue_or_not
    if log_and_pass_list_u == [] and log_and_pass_list_m == []:
        index1 = registration(log_and_pass_list_u, log_and_pass_list_m, examination_number)
        if log_and_pass_list_u == []:
            Manager(log_and_pass_list_u, log_and_pass_list_m, index1, list_of_books)
        elif log_and_pass_list_m == []:
            User(log_and_pass_list_u, index1, list_of_books)
    d = True
    while d == True:
        a = True
        while a == True:
            try:
                continue_or_not = int(input("Хотите продолжить? (1 - да, 2 - нет): "))
                if continue_or_not != 1 and continue_or_not != 2:
                    error_regist(continue_or_not)
                a = False
            except ValueError:
                print("\nВведите номер ответа, а не текст!")
            except CustomError as e:
                print(e)
            if continue_or_not == 2:
                break
        if continue_or_not == 2:
            break
        elif continue_or_not == 1:
            print("=====================================================")
            print("\nВойти в существующий аккаунт - 1")
            print("\nЗарегистрироваться как новый пользователь - 2")
            a = True
            while a == True:
                try:
                    sign_in_or_regist = int(input("\nВыберите действие: "))
                except ValueError:
                    print("\nВведите номер действия, а не текст!")
                if sign_in_or_regist != 1 and sign_in_or_regist != 2:
                    print("\nТакого действия нет!")
                a = False
            if sign_in_or_regist == 1:
                index1 = sign_in(log_and_pass_list_u, log_and_pass_list_m, examination_number, index1)
                User(log_and_pass_list_u, index1, list_of_books)
            elif sign_in_or_regist == 2:
                index1 = registration(log_and_pass_list_u, log_and_pass_list_m, examination_number)
                Manager(log_and_pass_list_u, log_and_pass_list_m, index1, examination_number)

if f == 0:
    Start()
    f += 1
