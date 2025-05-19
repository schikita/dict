=======
def create_dict(keys, values):
    """Создает словарь из списка ключей и значений"""
    # Твоя реализация здесь

def get_value(d, key):
    """Возвращает значение по ключу или None, если ключ не найден"""
    user = {
        'name': 'Roman',
        'surname': 'shuranov',
        'age': 16,
        'city': 'Orsha',
        'school': '№9',
        'countre': 'Беларусь'

    }
    print(user)

def add_to_dict(d, key, value):
    """Добавляет пару ключ-значение в словарь"""
    user = {
        'name': 'Roman',
        'surname': 'shuranov',
        'age': 16,
        'city': 'Orsha',
    }
    user['city'] = ('orsha')
    print(user)

def remove_from_dict(d, key):
    """Удаляет ключ из словаря"""
user = {
        'name': 'Roman',
        'surname': 'shuranov',
        'age': 16,
        'city': 'Orsha',
}
print(user)
del user['age']
print(user)

def merge_dicts(d1, d2):
    """Объединяет два словаря"""
'd1' == {1}
'd2' == {2}
print(dict.update('d1','d2'))

def check_key(d, key):
    """Проверяет, есть ли ключ в словаре"""
user = {
    'name': 'Roman',
    'surname': 'shuranov',
    'age': 16,
    'city': 'Orsha',
}
print = (user.keys())

def print_dict(d):
    """Выводит все ключи и значения словаря"""
keys = ['name', 'old', 'surname', 'city']
values = ['Roman', 18, 'shuranov', 'orsha']
user = dict(zip(keys, values))

print(user)

def sum_values(d):
    """Возвращает сумму всех значений в словаре"""
    # Твоя реализация здесь

def max_value(d):
    """Возвращает максимальное значение в словаре"""
d = {
    'one': 2,
    'two': 5,
    'three': 4,
}
print(max('one', 'two', 'three'))


def str_to_dict(s):
    """Создает словарь, где ключи — символы строки, а значения — их количество"""
    # Твоя реализация здесь
