import sqlite3
from typing import List


# Как сделать проверку на уникальность в базе данных + норм ваще иду или не

class Rabotniki:
    while True:
        try:
            def __init__(self):
                self.conn = sqlite3.connect("database.db")
                self.cu = self.conn.cursor()
                self.sozdanie()

            def sozdanie(self):
                self.cu.execute('''
                        CREATE TABLE IF NOT EXISTS Rabotniki(
                        Rab_id INTEGER PRIMARY KEY,
                        Surname TEXT NOT NULL,
                        Namee TEXT NOT NULL,
                        MiddleName TEXT,
                        NumberOfCreditIssued INTEGER NOT NULL,
                        Dolznost TEXT NOT NULL
                        )
                    ''')
                self.conn.commit()

            def dobrab(self, Surname, Namee, MiddleName, NumberOfCreditIssued, Dolznost):
                self.cu.execute(
                    "INSERT INTO Rabotniki(Surname, Namee, MiddleName, NumberOfCreditIssued,Dolznost) VALUES (?,?,?,?,?)",
                    (Surname, Namee, MiddleName, NumberOfCreditIssued, Dolznost))
                self.conn.commit()
                self.cu.execute('SELECT * FROM Rabotniki')
                rows = self.cu.fetchall()
                print("ВСЕ ВАШИ РАБЫ")
                for row in rows:
                    id = str(row[0])
                    Surname = str(row[1])
                    Namee = str(row[2])
                    MiddleName = str(row[3])
                    NumberOfCreditIssued = str(row[4])
                    Dolznost = str(row[5])
                    print(
                        "-------------------------------------------------------------------------------------------------------------------------------------------|")
                    print(
                        f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Кол-во выданных кредитов: {NumberOfCreditIssued} | Должность: {Dolznost}")

            def mda(self):
                while True:
                    self.cu.execute("SELECT * FROM Rabotniki")
                    value = self.cu.fetchall()
                    pamagite = input(
                        'Какой раз добавляете?\n\t1. Первый\n\t2. Второй\n\t3. Отказываюсь, хочу продолжить\n')
                    if pamagite == '1':
                        if not value:
                            self.cu.executemany(
                                "INSERT INTO Rabotniki(Surname, Namee, MiddleName, NumberOfCreditIssued,Dolznost) VALUES (?,?,?,?,?)",
                                [('Данилов', 'Аким', 'Авксентьевич', 2, 'Специалист по кредитам'),
                                 ('Кулаков', 'Ефим', 'Тарасович', 1, 'Консультант'),
                                 ('Константинов', 'Арсений', 'Никитьевич', 2, 'Кредитный работник'),
                                 ('Колесников', 'Пантелей', 'Петрович', 2, 'Специалист по кредитам'),
                                 ('Мамонтова', 'Олеся', 'Егоровна', 1, 'Кредитный работник'),
                                 ('Селезнёва', 'Залина', 'Олеговна', 1, 'Специалист по кредитам'),
                                 ('Архипова', 'Нега', 'Анатольевна', 1, 'Консультант')])
                            Surname = input('Введите фамилию раба: ')
                            Namee = input('Введите имя раба: ')
                            MiddleName = input('Введите отчество раба(если оно есть): ')
                            NumberOfCreditIssued = input('Введите сколько кредитов выдал раб: ')
                            Dolznost = input('Введите должность раба: ')
                            self.dobrab(Surname, Namee, MiddleName, NumberOfCreditIssued, Dolznost)
                        else:
                            print("Врать не норм")
                            continue
                    if pamagite == '2':
                        Surname = input('Введите фамилию раба: ')
                        Namee = input('Введите имя раба: ')
                        MiddleName = input('Введите отчество раба(если оно есть): ')
                        NumberOfCreditIssued = input('Введите сколько кредитов выдал раб: ')
                        Dolznost = input('Введите должность раба: ')
                        self.dobrab(Surname, Namee, MiddleName, NumberOfCreditIssued, Dolznost)
                    if pamagite == '3':
                        break

            def ydalenie(self):
                value = self.cu.fetchall()
                if not value:
                    self.cu.execute("SELECT * FROM Rabotniki")
                    self.conn.commit()
                    rows = self.cu.fetchall()
                    print("ВСЕ ВАШИ РАБЫ")
                    for row in rows:
                        id = str(row[0])
                        Surname = str(row[1])
                        Namee = str(row[2])
                        MiddleName = str(row[3])
                        NumberOfCreditIssued = str(row[4])
                        Dolznost = str(row[5])
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------|")
                        print(
                            f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Кол-во выданных кредитов: {NumberOfCreditIssued} | Должность: {Dolznost}")
                    idydal = input('Введите ID раба для удаления: ')
                    self.cu.execute("DELETE FROM Rabotniki WHERE id = ?", (idydal,))
                    self.conn.commit()
                    print(f"Раб с ID {idydal} делитнут")
                else:
                    print("Нечего удалять")

            def chtenie(self):
                while True:
                    self.conn.commit()
                    self.cu.execute('SELECT * FROM Rabotniki')
                    rows = self.cu.fetchall()
                    print("ВСЕ ВАШИ РАБЫ")
                    for row in rows:
                        id = str(row[0])
                        Surname = str(row[1])
                        Namee = str(row[2])
                        MiddleName = str(row[3])
                        NumberOfCreditIssued = str(row[4])
                        Dolznost = str(row[5])
                        print(
                            "-------------------------------------------------------------------------------------------------------------------------------------------|")
                        print(
                            f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Кол-во выданных кредитов: {NumberOfCreditIssued} | Должность: {Dolznost}")
                    break

            def izmenenie(self):
                while True:
                    value = self.cu.fetchall()
                    if not value:
                        self.cu.execute("SELECT * FROM Rabotniki")
                        self.conn.commit()
                        rows = self.cu.fetchall()
                        print("ВСЕ ВАШИ РАБЫ")
                        for row in rows:
                            id = str(row[0])
                            Surname = str(row[1])
                            Namee = str(row[2])
                            MiddleName = str(row[3])
                            NumberOfCreditIssued = str(row[4])
                            Dolznost = str(row[5])
                            print(
                                "-------------------------------------------------------------------------------------------------------------------------------------------|")
                            print(
                                f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Кол-во выданных кредитов: {NumberOfCreditIssued} | Должность: {Dolznost}")

                        idyizmen = input('Введите ID работника для изменения: ')
                        self.cu.execute("SELECT * FROM Credit WHERE id = ?", (idyizmen,))
                        v = self.cu.fetchone()
                        print(v)
                        b = input(
                            "Что конкретно вы хотите изменить?\n\t1. Фамилия\n\t2. Имя\n\t3. Отчество(если есть)\n\t4. Кол-во кредитов\n\t5. Должность\n\t6. Все вместе\n\t7. Мисс кликнул, теперь назад\n")

                        if b == '1':
                            Surname = input('Введите новую фамилию сотрудника: ')
                            self.cu.execute("UPDATE Rabotniki SET Surname = ? WHERE id = ?", (Surname, idyizmen))
                            continue
                        elif b == '2':
                            Namee = input('Введите новое имя: ')
                            self.cu.execute("UPDATE Rabotniki SET Namee = ? WHERE id = ?", (Namee, idyizmen))
                            continue
                        elif b == '3':
                            MiddleName = input('Введите новое отчество сотрудника(если оно есть): ')
                            self.cu.execute("UPDATE Rabotniki SET MiddleName = ? WHERE id = ?", (MiddleName, idyizmen))
                            continue
                        elif b == '4':
                            NumberOfCreditIssued = input('Введите обновленное кол-во кредитов выданных сотрудником: ')
                            self.cu.execute("UPDATE Rabotniki SET NumberOfCreditIssued = ? WHERE id = ?",
                                            (NumberOfCreditIssued, idyizmen))
                            continue
                        elif b == '5':
                            Dolznost = input('Введите новую должность сотрудника: ')
                            self.cu.execute("UPDATE Rabotniki SET Dolznost = ? WHERE id = ?", (Dolznost, idyizmen))
                            continue
                        elif b == '6':
                            Surname = input('Введите новую фамилию сотрудника: ')
                            Namee = input('Введите новое имя сотрудника: ')
                            MiddleName = input('Введите новое отчество сотрудника(если оно есть): ')
                            NumberOfCreditIssued = input('Введите обновленное кол-во кредитов выданных сотрудником: ')
                            Dolznost = input('Введите новую должность сотрудника: ')
                            self.cu.execute(
                                "UPDATE Credit SET Surname = ?, Namee = ?, MiddleName = ?, NumberOfCreditIssued = ?, Dolznost = ? WHERE id = ?",
                                (Surname, Namee, MiddleName, NumberOfCreditIssued, Dolznost))
                            continue
                        elif b == '7':
                            break

                        self.conn.commit()
                        self.conn.close()
                        print(f"Раб с ID {idyizmen} изменен")
                        break
                    else:
                        print('Нечего тут делать.')
        except:
            print('Ошибка')
        continue


while True:
    choice = input(
        "Вы можете:\n\t1. Посмотреть список всех рабов\n\t2. Добавить раба\n\t3. Удалить раба\n\t4. Изменить раба\n\t5. Откзываюсь, хочу продолжить\nВаш выбор:\n")
    if choice == '1':
        rab = Rabotniki()
        rab.chtenie()
    elif choice == '2':
        rab = Rabotniki()
        rab.mda()
    elif choice == '3':
        rab = Rabotniki()
        rab.ydalenie()
    elif choice == '4':
        rab = Rabotniki()
        rab.izmenenie()
    elif choice == '5':
        break
    else:
        print("Такой функции нет")