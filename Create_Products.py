class Create_Prod:
    def __init__(self, name: str, autor: str, cost: int, rating: float):
        self.name = name
        self.autor = autor
        self.cost = cost
        self.rating = rating

    def get_full_inf(self)->str:
        return f'Название: {self.name}, Автор: {self.autor}, Цена: {str(self.cost)}, Рейтинг: {str(self.rating)}'