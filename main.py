input_string1 = input("Введіть перше число: ")
input_string2 = input("Введіть друге число: ")
try:
    number1 = int(input_string1)
    number2 = int(input_string2)
    print("Ви ввели числа: ", number1, " та ", number2)

except ValueError:
    print("Неправильно введено формат числа! ")





