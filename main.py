from transport.Client import Client # Импортируем классы
from transport.Ship import Ship
from transport.Truck import Truck
from transport.TransportCompany import TransportCompany

class InputValidator: # Создаем класс InputValidator для валидации пользовательского ввода
    @staticmethod
    def validate_option_number(): # Статический метод для валидации номера операции
        while True:
            value = input("Введите номер желаемой операции: ")
            try:
                int_value = int(value)
                if int_value < 1 or int_value > 3:
                    print("Введенное вами значение должно находиться в диапазоне от 1 до 3. Попробуйте снова.")
                    continue
                return int_value
            except ValueError:
                print("Введенное вами значение не является целым числом. Попробуйте снова.")
   
    @staticmethod
    def validate_positive_float(value): # Статистический метод для валидации положительных дробных чисел
        while True:
            try:
                float_value = float(value)
                if float_value <= 0:
                    value = input("Введенное вами значение должно быть положительным целым или дробным числом. Попробуйте снова: ")
                    continue
                return float_value
            except ValueError:
                value = input("Введенное вами значение не является целым или дробным числом. Попробуйте снова: ")

    @staticmethod
    def validate_positive_int(value):# Статистический метод для валидации положительных целых чисел
        while True:
            try:
                int_value = int(value)
                if int_value <= 0:
                    value = input("Введенное вами значение должно быть положительным целым числом. Попробуйте снова: ")
                    continue
                return int_value
            except ValueError:
                value = input("Введенное вами значение не является целым или дробным числом. Попробуйте снова: ")

    @staticmethod
    def validate_string(value): # Статистический метод для валидации непустых строк
        while True:
            if not isinstance(value, str) or not value.strip():
                value = input("Введенное вами значение должно быть строкой. Попробуйте снова: ")
                continue
            return value
        
    @staticmethod
    def validate_non_empty_string(value): # Статистический метод для валидации непустых строк
        while True:
            if value.strip() == "":
                value = input("Введенное вами значение не может быть пустой строкой. Попробуйте снова: ")
                continue
            return value.strip()

company = TransportCompany("Транспортная Компания") # Создаем экземпляр класса TransportCompany с именем компании

status = True # Устанавливаем переменную состояния в True для начала основного цикла
while status: # Начинаем основной цикл программы
    print("--------------------------------")
    print("--------------Меню--------------")
    print("-----1. Клиенты компании--------")
    print("-----2. Транспортное средство---")
    print("-----3. Распределение грузов----")
    print("-----4. Выход-------------------")
    print("--------------------------------")
    b = input("Введите номер желаемой операции: ")
    try:
        a = int(b)
        if a < 1 or a > 4:
            print("Введенное вами значение должно находиться в диапазоне от 1 до 4. Попробуйте снова.")
            continue
    except ValueError:
        print("Введенное вами значение не является целым числом. Попробуйте снова.")
        continue

    if a == 1: # Если выбрана 1 операция (Клиенты компании)
        while True: # Начинаем внутренний цикл для работы с клиентами
            print("---------------------------------------------------------")
            print("-------Какую именно операцию Вы бы хотели совершить?-----")
            print("--1. Создание клиента(ов)--------------------------------")
            print("--2. Просмотреть информацию о уже существующих клиентах--")
            print("--3. Назад к главному меню-------------------------------")
            print("---------------------------------------------------------")
            c = InputValidator.validate_option_number() # Запрашиваем номер операции с помощью валидатора

            if c == 1: # Если выбрана операция 1 (Создание клиента)
                clients_data = [] # Обнуляем список клиентов перед добавлением новых
                e = InputValidator.validate_positive_int(input("Введите количество клиентов, которых Вы бы хотели создать: ")) # Запрашиваем количество клиентов и валидируем ввод
                for i in range(e): # Проходим по количеству клиентов, которых нужно создать
                    name = InputValidator.validate_non_empty_string(input(f"Введите имя клиента {i + 1}: ")) # Запрашиваем имя клиента и валидируем, чтобы оно не было пустым
                    cargo_weight = InputValidator.validate_positive_float(input(f"Введите вес груза {i + 1} клиента: ")) # запрашиваем вес груза и валидируем, чтобы он был положительным
                    while True: # Бесконечный цикл для проверки VIP-статуса
                        is_vip = input(f"Есть ли у {i + 1} клиента VIP-статус? (True/False): ")
                        if is_vip.lower() in ['true', 'false']: # Проверяем, введено ли корректное значение (True или False)
                            is_vip_bool = is_vip.lower() == 'true' # Преобразуем строку в булевое значение
                            break
                        else:
                            print("Введите корректный VIP-статус (True/False). Попробуйте снова.")
                            
                    try:
                        client = Client(name, cargo_weight, is_vip_bool) # Создаем экземпляр клиента с введенными данными
                        company.add_client(client) # Добавляем клиента в компанию
                        clients_data.append(client.__dict__) # Добавляем данные клиента в список clients_data
                        print(f"Клиент {name} добавлен.")
                    except ValueError as e:
                        print(f"Произошла ошибка: {e}")

            elif c == 2: # Если выбрана операция 2 (Просмотр информации о клиентах)
                if not company.clients: # Проверяем, есть ли клиенты в компании
                    print("В данный момент нет клиентов.")
                else:
                    print("Список клиентов:")
                    for client in clients_data: # Проходим по каждому клиенту в списке данных 
                        print(f"Имя клиента: {client['name']}, Вес груза: {client['cargo_weight']}, VIP-статус: {client['is_vip']}")

            elif c == 3: # Если выбрана операция 3 (Назад к главному меню)
                break # Выходим из внутреннего цикла для работы с клиентами и возвращаемся в главное меню

    elif a == 2: # Если выбрана операция 2 (Транспортные средства)
        while True: # Начинаем внутренний цикл для работы с транспортными средствами
            print("----------------------------------------------")
            print("--Выберите транспорт для указания параметров--")
            print("----------1. Грузовик-------------------------")
            print("----------2. Судно----------------------------")
            print("----------3. Назад к главному меню------------")
            print("----------------------------------------------")
            e = InputValidator.validate_option_number()

            if e == 1: # Если выбрана операция 1 (Грузовик)
                while True: # Начинаем внутренний цикл для работы с грузовиками
                    print("---------------------------------------------------------")
                    print("-------Какую именно операцию Вы бы хотели совершить?-----")
                    print("-1. Зарегистрировать грузовик----------------------------")
                    print("-2. Просмотреть информацию о уже существующих грузовиках-")
                    print("-3. Назад------------------------------------------------")
                    print("---------------------------------------------------------")
                    n = InputValidator.validate_option_number()

                    if n == 1: # Если выбрана опция 1 (Регистрация грузовика)
                        w = InputValidator.validate_positive_int(input("Введите количество грузовиков, которых Вы хотите создать: "))
                        for i in range(w): # Проходим по количеству грузовиков, которые нужно создать
                            capacity_float = InputValidator.validate_positive_float(input(f"Введите грузоподъемность {i + 1} грузовика (в тоннах): "))
                            color = InputValidator.validate_non_empty_string(input(f"Введите цвет {i + 1} грузовика: "))
                            try:
                                truck = Truck(capacity_float, color) # Создаем экземпляр грузовика с введенными данными
                                company.add_vehicle(truck) # Добавляем грузовик в компанию
                                print(f"Грузовик {color} с грузоподъемностью {capacity_float} тонн добавлен.")
                            except ValueError as e:
                                print(f"Произошла ошибка при добавлении грузовика: {e}")

                    elif n == 2: # Если выбрана опция 2 (Просмотр информации о грузовиках)
                        print("Список грузовиков:")
                        if not company.vehicles:
                            print("В данный момент нет транспортных средств")
                        else:
                            trucks_found = False # Флаг для отслеживания наличия грузовиков
                            for vehicle in company.list_vehicles():
                                if isinstance(vehicle, Truck): # Проверяем, является ли транспортное средство грузовиком
                                    print(vehicle) # Выводим информацию о грузовике
                                    trucks_found = True

                            if not trucks_found: # Если грузовики не найдены
                                print("В данный момент нет грузовиков.")

                    elif n == 3:  # Если выбрана опция 3 (Назад)
                        break # Выходим из внутреннего цикла для работы с грузовиками

            elif e == 2: # Если выбрана операция 2 (Судно)
                while True: # Начинаем внутренний цикл для работы с суднами
                    print("---------------------------------------------------------")
                    print("-------Какую именно операцию Вы бы хотели совершить?-----")
                    print("-1. Зарегистрировать судно-------------------------------")
                    print("-2. Просмотреть информацию о уже существующих суднах----")
                    print("-3. Назад------------------------------------------------")
                    print("---------------------------------------------------------")
                    u = InputValidator.validate_option_number()

                    if u == 1: # Если выбрана операция 1 (Регистрация судна)
                        w = InputValidator.validate_positive_int(input("Введите количество суден, которые Вы хотите создать: "))
                        for i in range(w):
                            capacity_float = InputValidator.validate_positive_float(input(f"Введите грузоподъемность {i + 1} судна (в тоннах): "))
                            name_ship = InputValidator.validate_string(input(f"Введите назвение {i + 1} судна: "))
                            try:
                                ship = Ship(capacity_float, name_ship) # Создаем экземпляр судна с введенными данными
                                company.add_vehicle(ship)
                                print(f"Судно с грузоподъемностью {capacity_float} тонн и названием {name_ship} добавлено.")
                            except ValueError as e:
                                print(f"Произошла ошибка при добавлении судна: {e}")

                    elif u == 2:  # Если выбрана опция 2 (Просмотр информации о суднах)
                        print("Список суден:")
                        if not company.vehicles:
                            print("В данный момент нет транспортных средств.")
                        else:
                            ships_found = False  # Инициализация флага для отслеживания наличия суден
                            for vehicle in company.list_vehicles():
                                if isinstance(vehicle, Ship):  # Проверяем, является ли транспортное средство судном
                                    print(vehicle)  # Выводим информацию о судне
                                    ships_found = True  # Устанавливаем флаг, что судно найдено

                            if not ships_found:  # Если судна не найдены
                                print("В данный момент нет суден.")

                    elif u == 3: # Если выбрана операция 3 (Назад)
                        break # Выходим из внутреннего цикла для работы с суднами

            elif e == 3: # Если выбрана операция 3 (Назад к главному меню)
                break # Выходим из внутреннего цикла для работы с транспортными средствами и возвращаемся в главное меню

    elif a == 3: # Если выбрана операция 3 (Распределение грузов)
        if not company.clients and not company.vehicles:
            print("В данный момент нет клиентов и транспортных средств для распределения грузов.")
            continue
        elif not company.clients:
            print("В данный момент нет клиентов для распределения грузов.")
            continue
        elif not company.vehicles:
            print("В данный момент нет транспортных средств для распределения грузов.")
            continue

        company.optimize_cargo_distribution() # Вызываем метод для оптимизации распределения грузов
        print("Распределение грузов выполнено:")
        for vehicle in company.list_vehicles(): # Проходим по каждому транспортному средству в компании
            print(vehicle) # Выводим информацию о транспортном средстве
            if vehicle.clients_list: # Проверяем, есть ли загруженные клиенты у транспортного средства
                print("Загруженные клиенты:")
                for client in vehicle.clients_list: # Проходим по каждому загруженному клиенту
                    print(f" - Имя: {client.name}, Вес груза: {client.cargo_weight}, VIP-статус: {client.is_vip}")
            else:
                print(" - Не загружено ни одного клиента. Не хватает грузоподьемности или все клиенты уже загружены в другие транспортные средства :( ")

    elif a == 4: # Если выбрана операция 4 (Выход)
        status = False # Меняем статус на False, чтобы выйти из основного цикла
print("Выход из программы.")
