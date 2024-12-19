import uuid # Импортируем модуль uuid для генерации уникальных идентификаторов

class Vehicle: # Определяем класс Vehicle
    def __init__(self, capacity): # Конструктор класса
        if not isinstance(capacity, (int, float)) or capacity < 0:  # Проверка, является ли capacity положительным числом
            raise ValueError("Грузоподъемность должна быть положительным числом.")
        
        self.vehicle_id = str(uuid.uuid4()) # Генерируем уникальный идентификатор для транспортного средства
        self.capacity = capacity
        self.current_load = 0
        self.clients_list = [] # Инициализация списка для хранения загруженных клиентов

    def load_cargo(self, client): # Метод для загрузки груза
        if not hasattr(client, 'cargo_weight'): # Проверка, имеет ли объект client атрибут cargo_weight
            raise ValueError("Объект client должен иметь cargo_weight.")

        cargo_weight = client.cargo_weight # Достаем вес груза из объекта client
        if not isinstance(cargo_weight, (float, int)) or cargo_weight < 0: # Проверка, является ли cargo_weight положительным числом
            raise ValueError("Вес груза должен быть положительным числом.")
        
        if self.current_load + cargo_weight > self.capacity: # Проверка, не превышает ли текущая загрузка плюс вес груза грузоподъемность
            raise ValueError("Недостаточно грузоподъемности для загрузки данного груза.")
        
        self.current_load += cargo_weight # Увеличиваем текущую загрузку на вес груза
        self.clients_list.append(client) # Добавляем клиента в список загруженных клиентов

    def __str__(self): # Магический метод для строкового представления объекта
        return f"Уникальный идентификатор: {self.vehicle_id}, Грузоподъемность: {self.capacity} тонн, Текущая загрузка: {self.current_load} тонн"