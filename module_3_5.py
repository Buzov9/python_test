def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) == 1:
        return int(str_number) if int(str_number) != 0 else 1
    else:
        return int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))


result1 = get_multiplied_digits(40203)
print(result1)
