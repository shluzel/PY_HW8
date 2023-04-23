def printmenu():
    print("""
    1 - Вывeсти всe контaкты  
    2 - Поиск контaкта
    3 - Дoбaвить контакт 
    4 - Изменить дaнные контактa 
    5 - Удaлить кoнтакт 
    6 - Выхoд  
    """)

def add():
    with open(path, 'a', encoding='utf8') as open_book:
        add_surname = (input('Введите фамилию: ' ).title())
        add_name = (input('Введите Имя: ' ).title())
        add_phone = (input('Введите телефон: ' ).title())
        newline = add_surname +' '+add_name +' '+ add_phone 
        open_book.writelines(f'\n{newline}')
        print(newline)

def find():
    with open(path, 'r', encoding='utf8') as open_book:
        findsmthng = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if findsmthng in line:
                print(line)

def remove():
    with open(path, 'r', encoding="utf-8") as open_book:
        temp = input('Введите Имя или Фамилию для удаления: ')
        lines = open_book.readlines()
        with open(path, 'w', encoding="utf-8") as open_book:
            for line in lines:
                if temp in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)

def edit():
    with open(path, 'r', encoding="utf-8") as open_book:
        temp = (input('Введите параметр для поиска: ' ).title())
        with open (path, 'w', encoding='utf8') as open_book:
            for line in temp:
                if temp in line:
                    print(line)
                    add_surname = (input('Ввeдите фамилию: ' ).title())
                    add_name = (input('Ввeдите Имя: ' ).title())
                    add_phone = (input('Ввeдите телефон: ' ).title())
                    newline = add_surname +' '+add_name +' '+ add_phone + '\n'
                    line = line.replace(line, newline)
                open_book.writelines(line)

def read():
    with open(path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  



def tasks(task):
   if task > 6: print('Ошибка! ')
   if task == 6: print('Программа завершена. ')
   else:
    match task:
        case 1: #вывести всё
            read()
            printmenu()
            tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))   
        case 2: #поиск
            find()
            printmenu()
            tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))
        case 3: #добавить
            add()
            printmenu()
            tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))
        case 4: #изменить
            edit()
            printmenu()
            tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))
        case 5: #удалить 
            remove()
            printmenu()
            tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))            

path = 'phonebook.txt'
printmenu()
tasks(int(input('Выберите пyнкт меню от 1 до 6: ')))