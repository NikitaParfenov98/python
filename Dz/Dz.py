test = 'test.csv'
phonebook = 'phonebook.csv'
def show_menu():
    print('1. Распечатать справочник'
          '2. Найти телефон по фамилии'
          '3. Изменить номер телефона'
          '4. Удалить запись'
          '5. Найти абонента по номеру телефона'
          '6. Добавить абонента в справочник'
          '7. Закончить работу', sep = '\n')
    choice = int(input('Введите номер меню'))
    return choice

def read_csv(phonebook):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(phonebook, 'r', encoding='utf-8') as php:
        for line in php:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def write_csv(phonebook, phone_book):
    with open(test, 'w', encoding='utf=8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v+','
            phout.write(f'{s[:-1]}\n')


def find_by_Lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            return item['Телефон']
    return 'Не найдено'

def find_by_number(phone_book, number):
    for item in phone_book:
        if number == item['Фамилия']:
            return item.values()
    return 'Не найдено'
    
def add_user(phone_book, user_data):
    phone_book.append(user_data)
    write_csv(phonebook, phone_book)
    return 'Абонент' + user_data['Имя'] + ' ' + user_data['Фамилия'] + 'добавлен'

def change_number(phone_book, last_name, new_number):
    newitem = {}
    for item in phone_book:
        if last_name == item['Фамилия']:
            newitem = item
            newitem['Телефон'] = new_number
            phone_book.remove(item).append(newitem)
            write_csv(phonebook, phone_book)
            return 'Номер телефона' + newitem['имя'] + ' ' + newitem['фамилия'] + 'изменен'
    return 'Не найдено'

def delete_by_Lastname(phone_book, last_name):
    for item in phone_book:
        if last_name == item['Фамилия']:
            phone_book.remove(item)
            write_csv(phonebook, phone_book)
            return 'Абонент' + item['Имя'] + ' ' + item['Фамилиия'] + 'удален'
    return 'Не найдено'


def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')
    while (choice != 7):
        if choice == 1:
            print(phone_book)
        elif choice == 2:
            last_name = input('Lastname')
            print(find_by_Lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Lastname')
            new_number = input('New namber')
            print(change_number(phone_book,  last_name, new_number))
        elif choice == 4:
            Lastname = input('Lastname')
            print(delete_by_Lastname(phone_book, Lastname))
        elif choice == 5:
            number = input('Number')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
            user_data = {}
            for item in fields:
                inputstr = input('Ведите' + item + ': ')
                if len(inputstr) == 0:
                    inputstr = input('Ведите' + item + ': ')
                user_data[item] = inputstr
            print(add_user(phone_book, user_data))
        elif choice == 7:
         choice = show_menu

work_with_phonebook()