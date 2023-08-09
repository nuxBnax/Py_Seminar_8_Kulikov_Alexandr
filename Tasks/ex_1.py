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
    print('Команды для работы со справочником,')
    print('lst - показать весь список контактов,')
    print('add - добавить контакт,')
    print('del - удалить контакт,')
    print('find - найти контакт:')

def input_cmd():
    return input('Введите желаемую команду: ')

def logic(text):
    if text == 'lst':
        full_list_print()
    elif text == 'add':
        add_data()
    # elif text == 'del':
    #     # функция удаление контакта из справочника
    # else text == 'find':
    #     # функция поиска контакта по справочнику

def full_list_print():
    path = 'dict.txt'
    data = open(path, 'r', encoding='utf-8')
    
    while True:
        line = data.readline()
        if not line:
            break
        print(line.strip())
        data.close

def add_data():
    print('Введите Фимилию Имя отчество Номер как в примере, используя пробел: ')
    new_data = input('Иванов Иван Иванович 80123456789: ').split()
    # print(new_data)   
    
    data = open('dict.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
    data.writelines(str('\n'))
    data.writelines(new_data) # разделителей не будет
    data.close()
    # text = s.splitlines()
    # for i in range(len(text)):
    #     text[i] = f"{i} {text[i]}"
    # s = '\n'.join(text)

prime()
