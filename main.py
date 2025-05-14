def simple_shift(text):
    """Каждая буква заменяется на следующую в алфавите"""
    result = ""
    # Ваш код здесь РЕШЕНИЕ БУДЕТ ТУТ
    return result

print(simple_shift("ABC"))  # Должно вернуть "BCD"

def reverse_text(text):
    """Возвращает текст задом наперёд"""
    # Ваш код здесь
    return result

print(reverse_text("hello"))  # "olleh"

def odd_even_encrypt(text):
    """
    Чётные буквы (по позиции) делаем заглавными,
    нечётные — строчными
    """
    result = ""
    # Ваш код здесь
    return result

print(odd_even_encrypt("abcdef"))  # "aBcDeF"

def replace_vowels(text):
    """Все гласные (a,e,i,o,u) заменяются на '*'"""
    vowels = "aeiouAEIOU"
    result = ""
    # Ваш код здесь
    return result

print(replace_vowels("Hello"))  # "H*ll*"

def count_letters(text):
    """Возвращает количество букв в тексте"""
    count = 0
    # Ваш код здесь
    return count

print(count_letters("A1B2C3"))  # 3

def caesar(text, shift):
    """Шифрует текст с заданным сдвигом"""
    result = ""
    # Ваш код здесь
    return result

print(caesar("ABC", 3))  # "DEF"

def caesar_decrypt(text, shift):
    """Дешифрует текст с заданным сдвигом"""
    # Ваш код здесь
    return result

print(caesar_decrypt("DEF", 3))  # "ABC"

def xor_cipher(text, key):
    """Шифрует текст с помощью XOR с одним символом-ключом"""
    result = ""
    # Ваш код здесь
    return result

print(xor_cipher("abc", "k"))  # Пример вывода

def generate_password(length):
    """Генерирует случайный пароль из букв"""
    import random
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Ваш код здесь
    return password

print(generate_password(8))  # Например "ahdjkasy"

def count_words(text):
    """Считает количество слов в тексте (разделены пробелом)"""
    # Ваш код здесь
    return count

print(count_words("Hello world"))  # 2

def check_password(password):
    """
    Проверяет, что пароль:
    - длиннее 8 символов
    - содержит цифру
    - содержит заглавную букву
    """
    # Ваш код здесь
    return is_strong

print(check_password("Pass123"))  # False

def letter_frequency(text):
    """Считает, сколько раз встречается каждая буква"""
    freq = {}
    # Ваш код здесь
    return freq

print(letter_frequency("aabbc"))  # {'a':2, 'b':2, 'c':1}

def substitution_cipher(text, code):
    """
    Заменяет буквы по словарю code.
    Пример: code = {'a':'x', 'b':'y'}, text="ab" → "xy"
    """
    result = ""
    # Ваш код здесь
    return result

code = {'a':'x', 'b':'y'}
print(substitution_cipher("abba", code))  # "xyyx"

def rot13(text):
    """Шифр ROT13 (сдвиг на 13 букв)"""
    # Ваш код здесь
    return result

print(rot13("HELLO"))  # "URYYB"
def break_caesar(ciphertext):
    """Пробует все сдвиги и находит осмысленный текст"""
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        # Ваш код проверки
    return best_guess

print(break_caesar("IFMMP"))  # "HELLO"

def xor_long(text, key):
    """XOR шифрование с ключом любой длины"""
    result = ""
    # Ваш код здесь
    return result

print(xor_long("message", "key"))  # Пример

def get_md5(text):
    """Возвращает MD5 хеш текста"""
    import hashlib
    # Ваш код здесь
    return hash_result

print(get_md5("hello"))  # "5d414..."

def generate_passphrase(words=4):
    """Генерирует пароль из случайных слов (можно использовать список)"""
    word_list = ["apple", "sun", "tree", "cat", ...]  # добавьте больше
    # Ваш код здесь
    return passphrase

print(generate_passphrase())  # "apple-sun-tree-cat"



