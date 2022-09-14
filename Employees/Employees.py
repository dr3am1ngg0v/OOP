import sqlite3 as sl
import os

os.system('cls')

con = sl.connect('employees.db')

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            'name' TEXT PRIMARY KEY,
            'age' INTEGER,
            'date' TEXT,
            'fee' INTEGER
        );
    """)

print('Добро пожаловать! Выберите функцию:')
print("")
    
def add():
    os.system('cls')
    name = str(input("ФИО сотрудника: "))
    age = int(input("Возраст сотрудника: "))
    date = str(input('Дата рождения сотрудника (пример: 01/01/1991): '))
    fee = int(input('Зарплата сотрудника: '))

    con.execute("INSERT INTO EMPLOYEES VALUES(?, ?, ?, ?)", 
                (name, age, date, fee)
    )
        
    print("Сотрудник успешно добавлен!")
    print(" ")
    ch()

def ch():
    choice = int(input("Желаете ли добавить еще одного сотрудника? (Да - 1, Нет - 2): "))
    if choice == 1:
        os.system('cls')
        add()
    if choice == 2:
        os.system('cls')
        check()
    else:
        print('Данной команды не существует. Повторите ввод.')
        print (' ')
        ch()
 
def change(name):
            data = con.execute("SELECT * FROM Employees WHERE name = ?", 
                    (name,)
            )
            os.system('cls') 
            print("Данные сотрудника:")
            print(" ")
            for row in data:
                print("ФИО: ", row[0])
                print('Возраст: ', row[1])
                print('Дата рождения: ', row[2])
                print('Заработная плата: ', row[3])
                print("")
            select = int(input("Выберите тип данных для изменения (ФИО - 1, Возраст - 2, Дата рождения - 3, Заработная плата - 4): "))   
            if select == 1:
                new_name = str(input("Введите новое ФИО сотрудника: "))
                con.execute("UPDATE Employees SET name = ? WHERE name = ?",
                            (new_name, name)    
                )
                name = new_name
            if select == 2:
                new_age = int(input("Введите новый возраст сотрудника: "))
                con.execute("UPDATE Employees SET age = ? WHERE name = ?",
                            (new_age, name)
                )
            if select == 3:
                new_date = str(input("Введите новую дату рождения сотрудника (пример: 01/01/1991): "))
                con.execute("UPDATE Employees SET date = ? WHERE name = ?",
                            (new_date, name)
                )
            if select == 4:
                new_fee = int(input("Введите новую заработную плату сотрудника: "))
                con.execute("UPDATE Employees SET fee = ? WHERE name = ?",
                            (new_fee, name)
                )
            os.system('cls')
            print("Изменение данных сотрудника успешно выполнено!")
            print(' ')
            data = con.execute("SELECT * FROM Employees WHERE name = ?",
                            (name,)
            )
            for row in data:
                print("ФИО: ", row[0])
                print('Возраст: ', row[1])
                print('Дата рождения: ', row[2])
                print('Заработная плата: ', row[3])
                print(' ')    
            def check2():
                new_sel = int(input("Изменить другие данные? (Да - 1, Нет - 2): "))
                if new_sel == 1:
                   change(name)
                if new_sel == 2:
                    os.system('cls')
                    check()
                else:
                    print("Данной команды не существует! Попробуйте еще раз!")
                    check2()
            check2()       

def check():
    progchoice = str(input('Просмотреть текущую базу данных - 1, Добавить нового сотрудника - 2, Изменить данные сотрудника - 3, Удалить данные о сотруднике - 4, Выход из программы - "Выход":'))

    if progchoice == '1':
        os.system('cls')
        with con:
            data = con.execute("SELECT * FROM Employees Order by name")
            for row in data:
                print('ФИО: ', row[0])
                print('Возраст: ', row[1])
                print('Дата рождения: ', row[2])
                print('Заработная плата: ', row[3])
                print(' ')
        check()
        
    if progchoice == '2':
        add()
        
    if progchoice == '3':
        name = str(input("Введите ФИО сотрудника, данные которого необходимо изменить: "))        
        change(name)
        
    if progchoice == '4':
        name = str(input("Введите ФИО сотрудника, которого необходимо удалить: "))
        con.execute("DELETE FROM Employees WHERE name = ?",
                    (name,)
        )
        os.system('cls')
        print("Сотрудник успешно удален!")
        check()
    
    if progchoice == 'Выход' or 'выход':
        os.system('cls')
        print("Спасибо за использование нашей программы! Удачного дня!")
        print("")
    else:
        os.system('cls')
        print("Данной команды не существует! Попробуйте еще раз!")
        print('')
        check()
        
    # Объяснение, почему для команды выхода используется фраза "Выход", а не цифра 5, например
    # В данном коде существует баг, который проявляется примерно так:
    #    Если на главном меню ввести команду 5 для выхода (конечно же присвоив фразу к команде)
    # то программа закончит работу
    #   Но если перед этим ввести команду 1 для просмотра таблицы и в далее в этом меню ввести команду 5 для выхода
    # то вместо выхода код выведет о "не существующей команде", которая должна выводиться только в том случае,
    # когда переменная выбора пункта не равна ни одному пункту из меню (то есть ни 1, ни 2, ни 3, ни 4, ни 5)
    # Я решил данную проблему путем изменения команды выхода из программы из числа в фразу
    #   Я не знаю, почему происходит этот баг, я пытался его исправить, и у меня ничего не вышло
    #   Если вы сможете решить эту проблему и при этом не сломать код, напишите мне
    
    # Программа сделана студентом УрФУ группы Фт-210007 Митрофановым Иваном Олеговичем
    
check()