# Задача №49. 

# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
#   текстовом файле
# 3. Пользователь может ввести одну из
#   характеристик для поиска определенной
#   записи(Например имя или фамилию
#   человека)
# 4. Использование функций. Ваша программа
#   не должна быть линейной


def prime():
    menu()
    logic(input_cmd())

def menu():
    print('Команды для работы со справочником, \n lst - показать весь список контактов, \n edit - редактировать контакт, \n add - добавить контакт, \n del - удалить контакт,\n find - найти контакт,\n exit - для выхода из меню:')

def input_cmd():
    return input('Введите желаемую команду: ')

def logic(text):
    if text == 'lst':
        full_list_print()
    elif text == 'add':
        add_data()
    elif text =='find':
        find_cont()
    elif text == 'del':
        delete_cont()
    elif text == 'edit':
        edit_cont()
    else:
        text ==  'exit'
        exit()

def full_list_print():
    data = open('dict.txt', 'r', encoding='utf-8')
    
    while True:
        line = data.readline()
        if not line:
            break
        print(line.strip())
        data.close
   
def add_data():
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write('\n'+ contact)
                           
def find_cont():
    find_info = input('Уточните параметры поиска (Фамилия, Имя или номер телефона)? ')
    with open('dict.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if find_info.upper() in line.upper().split():
                print(line, end = '')        

def delete_cont():
    del_info = input('Введите данные контакта (Фамилия, Имя или номер)')
    upload_list = []
    with open('dict.txt', 'r', encoding='utf-8') as data:
        upload_list = data.readlines()
        for line in range(len(upload_list)):
            if del_info.upper() in upload_list[line].upper().split():
                upload_list[line] = ''
    with open('dict.txt', 'w', encoding='utf-8') as data:
        for i in upload_list:
            data.write(i)

def edit_cont():
	delete_cont()
	contact = input('Введите Фамилию Имя Отчество Номер, используя пробел: ')
	with open('dict.txt', 'a', encoding='utf-8') as data:
		data.write(contact)

prime()
