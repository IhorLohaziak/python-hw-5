# Завдання 1
# Файл: `popularity.py`
# Оцінка: 60
# Створіть функцію `def popularity(text)` яка приймає текст `text` і повертає унікальний массив строк відсортований за популярністью.
# Уявіть що вам надсилають текст роману чи вірша і хочуть побачити найбільш популярні слова які зустрічаються у цьому тексті.
# - Для початку ви повинні розбити текст на слова. Слова розділені звичайними пробілами.
# - В тексті не будуть використовуватись точки або коми.
# - Регістр слів не повинен мати значення. Тобто 'Apple' і 'aPPle' - одне слово.
# - При формуванні результуючого массива слово повинно бути конвертовано в нижній регістр (lovercase). 
# - Сортування повинно бути виконано від найпопулярніших слів до найменш популярних.
# - Якщо слова мають однакову популярність, сортування повинно бути виконано за абеткою.
# Приклади:
# - `popularity('apple kiwi pineapple kiwi apple kiwi')` -> ['kiwi', 'apple', 'pineapple']
# - `popularity('aPPle pine Apple kiwi Apple kiwi')` -> ['apple', 'kiwi', 'pine']
# - `popularity('aPPle pine Apple kiwi Apple kiwi')` -> ['apple', 'kiwi', 'pine']
# - `popularity('aab aaa aac aab aac aaa x')` -> ['aaa', 'aab', 'aac', 'x']


# text  = 'apple kiwi pineapple kiwi apple kiwi apple'
# text  = 'aPPle pine Apple kiwi Apple kiwi'
# text  = 'aPPle pine Apple kiwi Apple kiwi'
# text  = 'aab aaa aac aab aac aaa x' 
# text  = 'apple kiwi pineapple apple kiwi apple apple kiwi kiwi kiwi apple'
import sys
def popularity(text):
    words = text.lower().split()   # в нижній регістр і ризбиває на списки
    word_dic = {}
    for word in words:
        try:
            word_dic[word] = word_dic[word] + 1
        except KeyError:
            word_dic[word] = 1
        sorted([(value, key) for (key,value) in word_dic.items()])[-3:] [::-1] # сортуємо словник
    list_sort = sorted(word_dic.keys(), key = lambda item: word_dic[item], reverse = True) # сортуємо список
    list_sort.sort() # сортуємо по алфавіту
    return list_sort
# print(popularity(text))