filePath='tel/phonebook.txt'
def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt(filePath)

    while (choice!=7):
        if choice==1:
            print(*phone_book,sep='\n')
        elif choice==2:
            last_name=input('Фамилия: ')
            print(f'Номер телефона абонента {last_name}: {find_by_lastname(phone_book,last_name)}')
        elif choice==3:
            last_name=input('Фамилия: ')
            new_number=input('Новый номер: ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('Фамилия: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('Номер: ')
            print(f'Абонент с номером телефона {number}: {find_by_number(phone_book,number)}')
        elif choice==6:
            fields=['Фамилия','Имя','Телефон','Описание']
            user_data={}
            for i in fields:
                inputStr=input(f'Введите  {i} : ')
                if len(inputStr)==0:
                    inputStr=input(f'Введите  {i} : ')
                user_data[i]=inputStr
            print(add_user(phone_book,user_data))
        choice=show_menu()
def show_menu():
    print(
        '1.Распечатать справочник\n'
        '2.Найти телефон по фамилии\n'
        '3.Изменить номер телефона\n'
        '4.Удалить запись\n'
        '5.Найти абонента по номеру телефона\n'
        '6.Добавить абонента в справочник\n'
        '7.Закончить работу',sep='\n'
    )
    choice=int(input('Введите номер меню: '))
    return choice
def read_txt(filePath):
    phone_book=[]
    fields=['Фамилия','Имя','Телефон','Описание']
    with open(filePath, 'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line[:-1].split(',')))
            phone_book.append(record)
    return phone_book
def write_txt(filePath,phone_book):
    with open(filePath,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')
def find_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия']==last_name:
            return i['Телефон']
    return 'Фамилия не найдена'
def find_by_number(phone_book,number):
    for i in phone_book:
        if i['Телефон']==number:
            return i['Фамилия']
    return 'Телефон не найден'
def add_user(phone_book,user_data):
    phone_book.append(user_data)
    write_txt(filePath,phone_book)
    return 'Абонент успешно добавлен'
def delete_by_lastname(phone_book,last_name):    
    for i in phone_book:
        if i['Фамилия']==last_name:
            phone_book.remove(i)
            write_txt(filePath,phone_book)
            return 'Фамилия '+last_name+' удалена'
    return 'Фамилия не найдена'
    
def change_number(phone_book,last_name,new_number):
    new_item={}
    for i in phone_book:
        if i['Фамилия']==last_name:
            new_item=i
            new_item['Телефон']=new_number
            phone_book.remove(i)
            phone_book.append(new_item)
            write_txt(filePath,phone_book)
            return 'Номер телефона изменен'
work_with_phonebook()