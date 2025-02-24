from Book2 import *

def Users_Actions():
    global index1, login, password
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

    print(log_and_pass_list_u[register_user.index1])
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
                print(log_and_pass_list_u[register_user.index1])
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

                    log_and_pass_list_u[register_user.index1].login = login

                elif ans == 2:
                    a2 = True
                    while a2:
                        password = input("\nВведите новый пароль (не менее 4 символов): ")
                        try:
                            error_pass(password, alphabet)
                            a2 = False
                        except CustomError as e:
                            print(e)
                    log_and_pass_list_u[register_user.index1].password = password

        elif choice_user == 3:
            print("=====================================================")
            shopping_cart = log_and_pass_list_u[register_user.index1].get(log_and_pass_list_u[register_user.index1].shopping_cart, [])
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
            shopping_cart = add_book(list_of_books, register_user.index1, log_and_pass_list_u)

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
            Users_Actions()
        elif yes_or_no_user == 2:
            print("\nВы вышли из системы пользователя!")
            Start()
            a = False
