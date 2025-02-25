from abc import ABC, abstractmethod

class Abs_Print(ABC):
    @abstractmethod
    def get_full_inf(self)->str:
        pass

class __Users:
    def __init__(self, login: str, password: str, role: str):
        self.login = login
        self.password = password
        self.role = role

class Create_User(__Users):
    __ID: int = 0
    def __init__(self, login: str, password: str, role: str):
        Create_User.__ID += 1
        self.__ID = Create_User.__ID
        super().__init__(login, password, role)
        self.shopping_cart = []

    def Return_ID(self):
        return self.__ID

    def get_full_inf(self)->str:
        return f'\nЛогин: {self.login}\nПароль: {self.password}\nКорзина: {str(self.shopping_cart)}'

class Create_Manager(__Users):
    __ID: int = 0
    def __init__(self, cod: int, login: str, password: str, role: str):
        Create_Manager.__ID += 1
        self.__ID = Create_Manager.__ID
        super().__init__(login, password, role)
        self.cod = cod

    def Return_ID(self):
        return self.__ID

    def get_full_inf(self) -> str:
        return f'\nЛогин: {self.login}\nПароль: {self.password}\nКод сотрудника: {str(self.cod)}'