"""
Возьмите любую из задач с прошлых семинаров (например сериализация данных), 
которые вы уже решали. Превратите функции в методы класса, а параметры в 
свойства. Задачи должны решаться через вызов методов экземпляра.
"""

import json

class DataSerializer:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def serialize_to_json(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def deserialize_from_json(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data


# Создаем экземпляр класса
serializer = DataSerializer(data={'name': 'John', 'age': 30}, filename='data.json')

# Вызываем метод для сериализации данных в JSON
serializer.serialize_to_json()

# Вызываем метод для десериализации данных из JSON
deserialized_data = serializer.deserialize_from_json()

# Выводим десериализованные данные
print(deserialized_data)
