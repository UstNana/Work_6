documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006"}
      ]


directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def people():
  numb_2 = 0
  numb_1 = input("Введите число")
  for mens in documents:
    if numb_1 == mens["number"]:
      numb_2 = mens["name"]
  print(numb_2)
  return 

#p = function()


def list_of_people():
  numb_3 = 0
  for people in documents:
    numb_2 = people["number"]
    numb_3 = people["name"]
    print("passport {} {}".format(numb_2, numb_3)) 

#l =list()

def add():
  type_input = input("Введите тип документа")
  number_input = input("Введитеномер документа")
  name_input = input("Введите имя")
  shelf_input = input("Ваш номер полки")
  documents.append({"type": type_input, "number": number_input, "name": name_input})
  print(documents)
  if shelf_input in directories.keys():
    directories[shelf_input].append(number_input)
  else:  
    directories.setdefault(shelf_input,name_input)
  print(directories)
 


def ssshelf():
  user_input = input("Номер паспорта:")
  for shelf, docs in directories.items():
    if user_input in docs:
      print(shelf) 
      return    
    else:
      print("Ошибка ввода") 
      return 

      
def name():
  try:
    for file in documents:
      if file["name"] != "":
        print ("dfff")
      else:
        print ("gggggggggg")
    return 
  except KeyError:
    print ("У документа нет имени")


def main():
  while True:
    main_input = input("Введите команду p,l,s, n или a:")
    if main_input == " ":
      print("Попробуйте ещё раз ввести команду")
    elif main_input == "l":
      list_of_people()
    elif main_input == "s":
      ssshelf()
    elif main_input == "a":
      add()
    elif main_input == "p":
      people()
    elif main_input == "n":
      name()
    else:
     print("Введите верную команду")
  return

do = main()
