from random import randint

class Person:
    user_name = 'Стас'
    email = f'stas.dko@yandex.ru'
    password = f'645890St'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'
