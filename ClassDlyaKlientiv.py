import sqlite3
from typing import List


# Как сделать проверку на уникальность в базе данных + норм ваще иду или не

class Clients:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cu = self.conn.cursor()
        self.sozdanie()

    def sozdanie(self):
        self.cu.execute('''
                CREATE TABLE IF NOT EXISTS Clients(
                id_clients INTEGER PRIMARY KEY,
                Surname TEXT NOT NULL,
                Namee TEXT NOT NULL,
                MiddleName TEXT,
                PassportS INTEGER NOT NULL,
                PassportN INTEGER NOT NULL,
                Credit_id INTEGER,
                Rab_id INTEGER,
                UNIQUE(PassportS, PassportN),
                FOREIGN KEY (Credit_id) REFERENCES Credit(Credit_id),
                FOREIGN KEY(Rab_id) REFERENCES Rabotniki(Rab_id)
                )
            ''')
        self.conn.commit()

    def dobkredit(self, Surname, Namee, MiddleName, PassportS, PassportN):
        self.cu.execute("INSERT INTO Clients(Surname, Namee, MiddleName, PassportS, PassportN) VALUES (?,?,?,?,?)",
                        (Surname, Namee, MiddleName, PassportS, PassportN))
        self.conn.commit()
        self.cu.execute('SELECT * FROM Clients')
        rows = self.cu.fetchall()
        print("ВСЕ КЛИЕНТЫ")
        for row in rows:
            Namee = str(row[2])
            MiddleName = str(row[3])
            PassportS = str(row[4])
            PassportN = str(row[5])
            Surname = str(row[1])
            id = str(row[0])
            print(
                "--------------------------------------------------------------------------------------------------------------------------|")
            print(
                f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Серия паспорта: {PassportS} | Номер паспорта: {PassportN}")

    def trash(self):
        while True:
            self.cu.execute("SELECT * FROM Clients")
            value = self.cu.fetchall()
            pamagite = input('Какой раз добавляете?\n\t1. Первый\n\t2. Второй\n\t3. Отказываюсь, хочу продолжить\n')
            if pamagite == '1':
                if not value:
                    try:
                        self.cu.executemany(
                            "INSERT INTO Clients (Surname,Namee,MiddleName,PassportS,PassportN) VALUES (?,?,?,?,?)",
                            [('Лыткина', 'Ирэн', 'Тимуровна', 6578, 678456),
                             ('Горбачёва', 'Татьяна', 'Валерьевна', 7654, 675483),
                             ('Цветкова', 'Руслана', 'Валерьевна', 5647, 895738),
                             ('Трофимов', 'Трофим', 'Юрьевич', 6742, 789420),
                             ('Мухин', 'Архип', 'Георгьевич', 6934, 821921),
                             ('Елисеев', 'Елисей', 'Гордеевич', 4356, 786543),
                             ('Прохоров', 'Парамон', 'Станиславович', 6843, 293820),
                             ('Филатов', 'Макар', 'Матвеевич', 5463, 754839),
                             ('Федотов', 'Мартын', 'Агафонович', 7654, 754883),
                             ('Мухин', 'Архип', 'Георгьевич', 8949, 78659)])

                        Surname = input('Введите фамилию: ')
                        Namee = input('Введите имя: ')
                        MiddleName = input('Введите отчество(если оно есть): ')
                        PassportS = int(input('Введите серию паспорта: '))
                        PassportN = int(input('Введите номер паспорта: '))
                        self.dobkredit(Surname, Namee, MiddleName, PassportS, PassportN)
                    except:
                        print('Ошибка')
                        continue
                else:
                    print("Врать не норм")
                    continue
            if pamagite == '2':
                try:
                    Surname = input('Введите фамилию: ')
                    Namee = input('Введите имя: ')
                    MiddleName = input('Введите отчество(если оно есть): ')
                    PassportS = int(input('Введите серию паспорта: '))
                    PassportN = int(input('Введите номер паспорта: '))
                    self.dobkredit(Surname, Namee, MiddleName, PassportS, PassportN)
                except:
                    print('Ошибка')
                continue
            if pamagite == '3':
                break

    def ydalenie(self):
        value = self.cu.fetchall()
        if not value:
            self.cu.execute("SELECT * FROM Clients")
            self.conn.commit()
            rows = self.cu.fetchall()
            print("ВСЕ ВАШИ КЛИЕНТЫ")
            for row in rows:
                Namee = str(row[2])
                MiddleName = str(row[3])
                PassportS = str(row[4])
                PassportN = str(row[5])
                Surname = str(row[1])
                id = str(row[0])
                print(
                    "--------------------------------------------------------------------------------------------------------------------------|")
                print(
                    f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Серия паспорта: {PassportS} | Номер паспорта: {PassportN}")
            idydal = input('Введите ID клиента для удаления: ')
            self.cu.execute("DELETE FROM Clients WHERE id = ?", (idydal,))
            self.conn.commit()
            print(f"Клиент с ID {idydal} делитнут")
        else:
            print("Нечего удалять")

    def chtenie(self):
        while True:
            self.conn.commit()
            self.cu.execute('SELECT * FROM Clients')
            rows = self.cu.fetchall()
            print("ВСЕ ВАШИ КЛИЕНТЫ")
            for row in rows:
                Namee = str(row[2])
                MiddleName = str(row[3])
                PassportS = str(row[4])
                PassportN = str(row[5])
                Surname = str(row[1])
                id = str(row[0])
                print(
                    "--------------------------------------------------------------------------------------------------------------------------|")
                print(
                    f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Серия паспорта: {PassportS} | Номер паспорта: {PassportN}")
            break

    def izmenenie(self):
        while True:
            value = self.cu.fetchall()
            if not value:
                self.cu.execute("SELECT * FROM Clients")
                self.conn.commit()
                rows = self.cu.fetchall()
                print("ВСЕ ВАШИ КРЕДИТЫ")
                for row in rows:
                    Namee = str(row[2])
                    MiddleName = str(row[3])
                    PassportS = str(row[4])
                    PassportN = str(row[5])
                    Surname = str(row[1])
                    id = str(row[0])
                    print(
                        "--------------------------------------------------------------------------------------------------------------------------|")
                    print(
                        f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Серия паспорта: {PassportS} | Номер паспорта: {PassportN}")

                idyizmen = input('Введите ID кредита для изменения: ')
                self.cu.execute("SELECT * FROM Clients WHERE id = ?", (idyizmen,))
                v = self.cu.fetchone()
                print(v)
                b = input(
                    "Что конкретно вы хотите изменить?\n\t1. Фамилию \n\t2. Имя\n\t3. Отчество(если есть)\n\t4. Номер пасспорта\n\t5. Серия паспорта\n\t6. Все вместе\n\t7. Мисс кликнул, теперь назад\n")

                if b == '1':
                    Surname = input('Введите новую фамилию: ')
                    self.cu.execute("UPDATE Clients SET Surname = ? WHERE id = ?", (Surname, idyizmen))
                    continue
                elif b == '2':
                    Namee = input('Введите новую имя: ')
                    self.cu.execute("UPDATE Clients SET Namee = ? WHERE id = ?", (Namee, idyizmen))
                    continue
                elif b == '3':
                    MiddleName = input('Введите новое отчество: ')
                    self.cu.execute("UPDATE Clients SET MiddleName = ? WHERE id = ?", (MiddleName, idyizmen))
                    continue
                elif b == '4':
                    try:
                        PassportS = int(input('Введите новую серию паспорта: '))
                        self.cu.execute("UPDATE Clients SET PassportS = ? WHERE id = ?", (PassportS, idyizmen))
                        continue
                    except:
                        print('Ошибка')
                        continue
                elif b == '5':
                    try:
                        PassportN = int(input('Введите новый номер паспорта: '))
                        self.cu.execute("UPDATE Clients SET PassportN = ? WHERE id = ?", (PassportN, idyizmen))
                        continue
                    except:
                        print('Ошибка')
                        continue
                elif b == '6':
                    try:
                        Surname = input('Введите новую фамилию: ')
                        Namee = input('Введите новое имя: ')
                        MiddleName = input('Введите новое отчество: ')
                        PassportS = int(input('Введите новую серию паспорта: '))
                        PassportN = int(input('Введите новый номер паспорта: '))
                        self.cu.execute(
                          "UPDATE Clients SET Surname = ?, Namee = ?, MiddleName = ?, PassportS = ?, PassportN = ? WHERE id = ?",
                        (Surname, Namee, MiddleName, PassportS, PassportN, idyizmen))
                        continue
                    except:
                        print('Ошибка')
                        continue
                elif b == '7':
                    break

                self.conn.commit()
                self.conn.close()
                print(f"Клиент с ID {idyizmen} изменен")
                break
            else:
                print('Нечего тут делать.')


while True:
    choice = input(
        "Вы можете:\n\t1. Посмотреть список всех клиентов\n\t2. Добавить клиента\n\t3. Удалить клиента\n\t4. Изменить клиента\n\t5. Откзываюсь, хочу продолжить\nВаш выбор:\n")
    if choice == '1':
        client = Clients()
        client.chtenie()
    elif choice == '2':
        client = Clients()
        client.trash()
    elif choice == '3':
        client = Clients()
        client.ydalenie()
    elif choice == '4':
        client = Clients()
        client.izmenenie()
    elif choice == '5':
        break
    else:
        print("Такой функции нет")
