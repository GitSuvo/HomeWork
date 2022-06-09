# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:


def translate(n):
    print(dictionary.get(n))


def translate_adv(n):
    if n.istitle() and n.lower() in dictionary:
        low_n = (n.lower())
        print(dictionary.get(low_n).capitalize())
    else:
        print(dictionary.get(n))

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей
# буквы.

def theasurus(*args):
    dict_name = {}
    for name in sorted(args):
        dict_name.setdefault(name[0], []).append(name)
    return dict_name


# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

def theasurus_adv(*args):
    dict_lstname = {}
    for n in (args):
        name_1, name_2 = n.split(' ')
        val = dict_lstname.setdefault(name_2[0], {}).setdefault(name_1[0], []).append(n)

    print(dict_lstname)


# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):


from random import choice

def get_jokes(count, flag=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for c in range(count):
        joke_lst = []
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = ('{} {} {}'.format(noun, adverb, adjective))
        joke_lst.append(joke)
        print(joke_lst)
        joke_lst2 = []
        if flag == True:
            joke_lst2 = joke.split()
            for elem1 in nouns:
                for elem in joke_lst2:
                    if elem1 == elem:
                        nouns.remove(elem1)
        for elem2 in adverbs:
            for elem in joke_lst2:
                if elem2 == elem:
                    adverbs.remove(elem2)
        for elem3 in adjectives:
            for elem in joke_lst2:
                if elem3 == elem:
                    adjectives.remove(elem3)


get_jokes(count=6, flag=False)
