
class __Users():
    def __init__(self, login: str, password: str, role: str):
        self.login = login
        self.password = password
        self.role = role

class Create_User(__Users):
    __ID: int = 0
    def __init__(self, login: str, password: str, role: str):
        self.__ID += 1
        super().__init__(login, password, role)
        self.shopping_cart = []

    def Return_ID(self):
        return self.__ID

class Create_Manager(__Users):
    __ID: int = 0
    def __init__(self, cod: int, login: str, password: str, role: str):
        self.__ID += 1
        super().__init__(login, password, role)
        self.cod = cod

    def Return_ID(self):
        return self.__ID