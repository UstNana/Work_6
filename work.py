
input_value = []
try:
  input_value = input("Введите символ и два числа ")
  print(input_value[0], input_value[1])
  assert(input_value[0] in ["-", "+", "/", "*"])
  
  if input_value[3] != " ":
    raise Exception ("Введите только 2 числа")
except IndexError:
  print("Ввод только чисел")
except AssertionError:
  print("Доступны только операции +, -, *, /")


try:
  if input_value[0] == "+":
    int_value_1 = int(input_value[1])
    int_value_2 = int(input_value[2])
    summ = int_value_1 + int_value_2
    print ("Ответ", summ)
  elif input_value[0] == "-":
    int_value_1 = int(input_value[1])
    int_value_2 = int(input_value[2])
    differ = int_value_1 - int_value_2
    print ("Ответ", differ)
  elif input_value[0] == "/":
    int_value_1 = int(input_value[1])
    int_value_2 = int(input_value[2])
    division = int_value_1 / int_value_2
    print ("Ответ", division)
  elif input_value[0]=="*":
    int_value_1 = int(input_value[1])
    int_value_2 = int(input_value[2])
    multi = int_value_1 * int_value_2
    print ("Ответ", multi)
except ValueError:
  print("Пожалуста, пишите без запятых и пробелов")
except ZeroDivisionError:
  print("На ноль делить нельзя")
