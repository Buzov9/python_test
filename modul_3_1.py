calls = 0


def count_calls():
    #     подсчёт вызовов остальных функций
    global calls
    calls += 1



def string_info(string):
    #     длина строки/строка в верхнем регистре/строка в нижнем регистре
    count_calls()
    string = str(string)
    count = len(string)
    str_up = string.upper()
    str_low = string.lower()
    return count, str_up, str_low

def is_contains(string, list_to_search):
    # True, если есть в списке
    count_calls()
    string = str(string)
    list_to_search = list(list_to_search)
    string = string.lower()

    for i in list_to_search:
        if string == i.lower():
            return True
    return False

print(string_info('GALA_JRAT'))
print(string_info('GAmburG'))
print(is_contains('John', ['Jora', 'Ann', 'Ban', 'pale']))
print(is_contains('BAn', ['dgh', 'kdfo', 'BAN', 'ton']))
print(calls)
