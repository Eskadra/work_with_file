def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=7):
        if choice==1:
            print(phone_book)
            choice=show_menu()
        elif choice==2:
            last_name=input('Введите фамилию для поиска: ')
            print(find_by_lastname(phone_book, last_name))
            choice=show_menu()
        elif choice==3:
            last_name=input('Введите фамилию: ')
            new_number=input('Введите новый номер телефона: ')
            print (change_number(phone_book, last_name,new_number))
            write_txt('phon.txt', phone_book)
            choice=show_menu()
        elif choice==4:
            lastname=input('Введите фамилию для удаления: ')
            print(delete_by_lastname(phone_book, lastname))
            write_txt('phon.txt', phone_book)
            choice=show_menu()
        elif choice==5:
            phone_number=input('Введите номер телефона для поиска: ')
            print(find_by_number(phone_book, phone_number))
            choice=show_menu()
        elif choice==6:
            user_data=input('Впишите Фамилию, Имя, Телефон, Описание через запятую: ')
            add_user (phone_book, user_data)
            write_txt('phon.txt', phone_book)
            choice=show_menu()

def add_user(phone_book, user_data):
    data = user_data.split(",")
    new_user = {
        'Фамилия': data[0],
        'Имя': data[1],
        'Телефон': data[2],
        'Описание': data[3]
    }
    phone_book.append(new_user)
    print("Запись успешно добавлена.")

#вызов меню
def show_menu():
    print('1. Распечатать справочник'
          '\n2. Найти телефон по фамилии'
          '\n3. Изменить номер телефона'
          '\n4. Удалить запись'
          '\n5. Найти абонента по номеру телефона'
          '\n6. Добавить абонента в справочник'
          '\n7. Закончить работу', sep='\n')
    choice=int(input())
    return choice

#функция чтения
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

#функция изменения
def change_number(phone_book, last_name, new_number):
    found = False
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            contact['Телефон'] = new_number
            found = True
            break
    
    if found:
        return f"Номер телефона для абонента с фамилией {last_name} изменен на {new_number}\n"
    else:
        return f"Абонент с фамилией {last_name} не найден\n"
    
#функция поиск по фамилии
def find_by_lastname(phone_book, last_name):
    found = False
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            found = True
            break

    if found:
        return f"Абонент с фамилией {last_name} найден, номер телефона {contact['Телефон']}\n"
    else:
        return f"Абонент с фамилией {last_name} не найден\n"
    
#функция поиска по номеру телефона
def find_by_number(phone_book, phone_number):
    found = False
    for contact in phone_book:
        if contact['Телефон'] == phone_number:
            found = True
            break
        
    if found:
        return f"номер телефона {phone_number} принадлежит абонент с фамилией {contact['Фамилия']}\n"
    else:
        return f"Абонент с телефонным номером {phone_number} не найден\n"
      
#функция удаления пользователя
def delete_by_lastname(phone_book, lastname):
    deleted = False
    for contact in phone_book:
        if contact['Фамилия'] == lastname:
            phone_book.remove(contact)
            deleted = True
    
    if deleted:
        print(f"Запись с фамилией '{lastname}' успешно удалена.\n")
    else:
        print(f"Запись с фамилией '{lastname}' не найдена.\n")
        
#функция экспорта
def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')

work_with_phonebook()