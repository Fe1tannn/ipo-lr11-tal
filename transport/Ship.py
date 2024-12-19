from .Vehicle import Vehicle # Импортируем класс Vehicle из модуля Vehicle, который находится в том же пакете

class Ship(Vehicle): # Определяем класс Ship, который наследует от класса Vehicle
    _id_counter = 1  # Счетчик для уникальных ID
    def __init__(self, capacity, name_ship): # Конструктор класса Ship, принимающий грузоподъемность и название
        super().__init__(capacity) # Вызываем конструктор родительского класса Vehicle для инициализации грузоподъемности
        self.name_ship = name_ship # Сохраняем количество вагонов поезда
        self.id = Ship._id_counter
        Ship._id_counter += 1

    def __str__(self): # Метод для строкового представления объекта Ship
        first_str = super().__str__() # Получаем строковое представление родительского класса Vehicle
        return f"Судно, {first_str}, Имя: {self.name_ship}"