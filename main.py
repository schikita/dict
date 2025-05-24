=======
def create_dict(keys, values):
    """Создает словарь из списка ключей и значений"""
user = {
    'name': 'Roman',
    'surname': 'shuranov',
    'age': 16,
    'city': 'Orsha',
    'school': '№9',
    'countre': 'Беларусь'

}
print(user)

def get_value(d, key):
    """Возвращает значение по ключу или None, если ключ не найден"""
user = {
    'name': 'Roman',
    'surname': 'shuranov',
    'age': 16,
    'city': 'Orsha',
}
print(user)
print(user.get('name'))

def add_to_dict(d, key, value):
    """Добавляет пару ключ-значение в словарь"""
user = {
    'name': 'Roman',
    'surname': 'shuranov',
    'age': 16,
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
d1 = {
    'd1': 1
}
d2 = {
    'd2': 1
}

dict.update(d1, d2)
print(d1)

def check_key(d, key):
    """Проверяет, есть ли ключ в словаре"""
    return key in d
user = {
        'name': 'Roman',
        'surname': 'shuranov',
        'age': 16,
        'city': 'Orsha',
}
print(check_key(user, 'name'))

def print_dict(d):
    """Выводит все ключи и значения словаря"""
    print(user.keys())
    print(user.values())

keys = ['name', 'old', 'surname', 'city']
values = ['Roman', 18, 'shuranov', 'orsha']
user = dict(zip(keys, values))

print_dict(user)

def sum_values(d):
    """Возвращает сумму всех значений в словаре"""
    return sum(value for value in d.values() if isinstance(value, (int, float)))
user = {
        'name': 100,
        'surname': 'shuranov',
        'age': 16,
        'city': 'Orsha',
}

print(sum_values(user))
def max_value(d):
    """Возвращает максимальное значение в словаре"""
    return max(d.values())

d = {
    'one': 2,
    'two': 5,
    'three': 4,
}
print(max_value(d))

def str_to_dict(s):
    """Создает словарь, где ключи — символы строки, а значения — их количество"""
    return {char: s.count(char) for char in set(s)}

s = "Hello"

result = str_to_dict(s)

print(result)