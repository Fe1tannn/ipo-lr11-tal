from .Vehicle import Vehicle # Импортируем классы из модулей, которые находятся в том же пакете
from .Client import Client

class TransportCompany: # Определяем класс TransportCompany, который представляет транспортную компанию
    def __init__(self, name): # Конструктор класса, принимающий название компании
        if not name or not name.strip():
            raise ValueError("Название компании не может быть пустой строкой.")
        self.name = name # Сохраняем название компании
        self.vehicles = [] # Инициализация пустого списка для транспортных средств
        self.clients = [] # Инициализация пустого списка для клиентов

    def add_vehicle(self, vehicle): # Метод для добавления транспортного средства в компанию
        if not isinstance(vehicle, Vehicle): # Проверяем, что добавляемый объект является экземпляром класса Vehicle
            raise ValueError("Транспортное средство должно быть экземпляром класса Vehicle.")
        self.vehicles.append(vehicle) # Добавляем транспортное средство в список

    def list_vehicles(self): # Метод для получения списка транспортных средств
        return self.vehicles # Возвращаем список транспортных средств

    def add_client(self, client): # Метод для добавления клиента в компанию
        if not isinstance(client, Client): # Проверяем, что добавляемый объект является экземпляром класса Client
            raise ValueError("Клиентов нет.")
        self.clients.append(client) # Добавляем клиента в список

    def list_clients(self): # Метод для получения списка клиентов
        return self.clients # Возвращаем список клиентов

    def optimize_cargo_distribution(self): # Метод для оптимизации распределения грузов
        for vehicle in self.vehicles: # Очищаем список загруженных клиентов в каждом транспортном средстве
            vehicle.clients_list.clear()

        vip_clients = [client for client in self.clients if client.is_vip] # Получаем список VIP-клиентов
        simple_clients = [client for client in self.clients if not client.is_vip] # Получаем список обычных клиентов
        
        vip_clients.sort(key=lambda c: c.cargo_weight, reverse=True) # Сортируем VIP-клиентов по весу груза в порядке убывания
        simple_clients.sort(key=lambda c: c.cargo_weight, reverse=True) # Сортируем обычных клиентов по весу груза в порядке убывания
        
        for client in vip_clients: # Проходим по каждому VIP-клиенту
            for vehicle in self.vehicles: # Проходим по каждому транспортному средству
                try:
                    vehicle.load_cargo(client) # Загружаем груз в транспортное средство
                    break
                except ValueError: # Если возникает ошибка из-за недостатка места
                    continue # Переходим к следующему транспортному средству

        for client in simple_clients: # Проходим по каждому обычному клиенту
            for vehicle in self.vehicles: # Проходим по каждому транспортному средству
                try:
                    vehicle.load_cargo(client) # Загружаем груз в транспортное средство
                    break
                except ValueError: # Если возникает ошибка из-за недостатка места
                    continue # Переходим к следующему транспортному средству

    def __str__(self): # Метод для строкового представления объекта TransportCompany
        vehicles_info = ', '.join([str(vehicle) for vehicle in self.vehicles]) # Создаем строку с информацией о всех транспортных средствах
        return f"Компания: {self.name}, Транспортные средства: [{vehicles_info}]" # Возвращаем строку с названием компании и списком транспортных средств