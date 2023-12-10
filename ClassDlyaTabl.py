import sqlite3
from typing import List


# Как сделать проверку на уникальность в базе данных + норм ваще иду или не

class Kredit:
    while True:
        try:
            def __init__(self):
                self.conn = sqlite3.connect("database.db")
                self.cu = self.conn.cursor()
                self.sozdanie()

            def sozdanie(self):
                self.cu.execute('''
                        CREATE TABLE IF NOT EXISTS Credit(
                        Credit_id INTEGER PRIMARY KEY,
                        CreditSubject TEXT NOT NULL,
                        Suma TEXT NOT NULL,
                        Percent TEXT NOT NULL,
                        Godikioplati INTEGER NOT NULL,
                        UNIQUE(CreditSubject, Suma, Percent, Godikioplati)
                        )
                    ''')
                self.conn.commit()

            def dobkredit(self, CreditSubject, Suma, Percent, Godikioplati):
                self.cu.execute("INSERT INTO Credit(CreditSubject, Suma, Percent, Godikioplati) VALUES (?,?,?,?)",
                                (CreditSubject, Suma, Percent, Godikioplati))
                self.conn.commit()
                self.cu.execute('SELECT * FROM Credit')
                rows = self.cu.fetchall()
                print("ВСЕ ВАШИ КРЕДИТЫ")
                for row in rows:
                    Suma = str(row[2])
                    Percent = str(row[3])
                    Godikioplati = str(row[4])
                    CreditSubject = str(row[1])
                    id = str(row[0])
                    print(
                        "--------------------------------------------------------------------------------------------------------------------------|")
                    print(
                        f"ID: {id} | Наименование: {CreditSubject} | Сумма: {Suma} | Процент кредита: {Percent} | На сколько лет выдан: {Godikioplati}")

            def trash(self):
                while True:
                    self.cu.execute("SELECT * FROM Credit")
                    value = self.cu.fetchall()
                    pamagite = input(
                        'Какой раз добавляете?\n\t1. Первый\n\t2. Второй\n\t3. Отказываюсь, хочу продолжить\n')
                    if pamagite == '1':
                        if not value:
                            self.cu.executemany(
                                "INSERT INTO Credit (CreditSubject,Suma,Percent,Godikioplati) VALUES (?,?,?,?)",
                                [('Квартира', '20 000 000,00 ₽', '5.5%', 20),
                                 ('Машина', '6 500 000,00 ₽', '16,40%', 5),
                                 ('Машина', '6 500 000,00 ₽', '14,10%', 7),
                                 ('Отпуск', '500 000,00 ₽', '12,50%', 1),
                                 ('Ремонт', '100 000,00 ₽', '6,70%', 1),
                                 ('Бытовая техника', '40 000,00 ₽', '101,40%', 1)])
                            CreditSubject = input('Введите наименование кредита: ')
                            Suma = input('Введите сумму: ')
                            Percent = input('Введите процент выдачи кредита: ')
                            Godikioplati = input('Введите на сколько лет выдается кредит: ')
                            self.dobkredit(CreditSubject, Suma, Percent, Godikioplati)
                        else:
                            print("Врать не норм")
                            continue
                    if pamagite == '2':
                        CreditSubject = input('Введите наименование кредита: ')
                        Suma = input('Введите сумму: ')
                        Percent = input('Введите процент выдачи кредита: ')
                        Godikioplati = input('Введите на сколько лет выдается кредит: ')
                        self.dobkredit(CreditSubject, Suma, Percent, Godikioplati)
                    if pamagite == '3':
                        break

            def ydalenie(self):
                value = self.cu.fetchall()
                if not value:
                    self.cu.execute("SELECT * FROM Credit")
                    self.conn.commit()
                    rows = self.cu.fetchall()
                    print("ВСЕ ВАШИ КРЕДИТЫ")
                    for row in rows:
                        suma = str(row[2])
                        percent = str(row[3])
                        godikioplati = str(row[4])
                        credit_subject = str(row[1])
                        id = str(row[0])
                        print(
                            "--------------------------------------------------------------------------------------------------------------------------|")
                        print(
                            f"ID: {id} | Наименование: {credit_subject} | Сумма: {suma} | Процент кредита: {percent} | На сколько лет выдан: {godikioplati}")
                    idydal = input('Введите ID кредита для удаления: ')
                    self.cu.execute("DELETE FROM Credit WHERE id = ?", (idydal,))
                    self.conn.commit()
                    print(f"Кредит с ID {idydal} делитнут")
                else:
                    print("Нечего удалять")

            def chtenie(self):
                while True:
                    self.conn.commit()
                    self.cu.execute('SELECT * FROM Credit')
                    rows = self.cu.fetchall()
                    print("ВСЕ ВАШИ КРЕДИТЫ")
                    for row in rows:
                        Suma = str(row[2])
                        Percent = str(row[3])
                        Godikioplati = str(row[4])
                        CreditSubject = str(row[1])
                        id = str(row[0])
                        print(
                            "--------------------------------------------------------------------------------------------------------------------------|")
                        print(
                            f"ID: {id} | Наименование: {CreditSubject} | Сумма: {Suma} | Процент кредита: {Percent} | На сколько лет выдан: {Godikioplati}")
                    break

            def izmenenie(self):
                while True:
                    value = self.cu.fetchall()
                    if not value:
                        self.cu.execute("SELECT * FROM Credit")
                        self.conn.commit()
                        rows = self.cu.fetchall()
                        print("ВСЕ ВАШИ КРЕДИТЫ")
                        for row in rows:
                            suma = str(row[2])
                            percent = str(row[3])
                            godikioplati = str(row[4])
                            creditsubject = str(row[1])
                            id = str(row[0])
                            print("--------------------------------------------------------")
                            print(
                                f"ID: {id} | Наименование: {creditsubject} | Сумма: {suma} | Процент кредита: {percent} | На сколько лет выдан: {godikioplati}")

                        idyizmen = input('Введите ID кредита для изменения: ')
                        self.cu.execute("SELECT * FROM Credit WHERE id = ?", (idyizmen,))
                        v = self.cu.fetchone()
                        print(v)
                        b = input(
                            "Что конкретно вы хотите изменить?\n\t1. Наименование \n\t2. Сумму\n\t3. Процент\n\t4. Время выдачи\n\t5. Все вместе\n\t6. Мисс кликнул, теперь назад\n")

                        if b == '1':
                            CreditSubject = input('Введите новое наименование: ')
                            self.cu.execute("UPDATE Credit SET CreditSubject = ? WHERE id = ?",
                                            (CreditSubject, idyizmen))
                            continue
                        elif b == '2':
                            Suma = input('Введите новую сумму: ')
                            self.cu.execute("UPDATE Credit SET Suma = ? WHERE id = ?", (Suma, idyizmen))
                            continue
                        elif b == '3':
                            Percent = input('Введите новый процент: ')
                            self.cu.execute("UPDATE Credit SET Percent = ? WHERE id = ?", (Percent, idyizmen))
                            continue
                        elif b == '4':
                            Godikioplati = input('Введите новое время выдачи: ')
                            self.cu.execute("UPDATE Credit SET Godikioplati = ? WHERE id = ?", (Godikioplati, idyizmen))
                            continue
                        elif b == '5':
                            CreditSubject = input('Введите новое наименование: ')
                            Suma = input('Введите новую сумму: ')
                            Percent = input('Введите новый процент: ')
                            Godikioplati = input('Введите новое время выдачи: ')
                            self.cu.execute(
                                "UPDATE Credit SET CreditSubject = ?, Suma = ?, Percent = ?, Godikioplati = ? WHERE id = ?",
                                (CreditSubject, Suma, Percent, Godikioplati, idyizmen))
                            continue
                        elif b == '6':
                            break

                        self.conn.commit()
                        self.conn.close()
                        print(f"Кредит с ID {idyizmen} изменен")
                        break
                    else:
                        print('Нечего тут делать.')
        except:
            print('Ошибка')
        continue


while True:
    choice = input(
        "Вы можете:\n\t1. Посмотреть список всех кредитов\n\t2. Добавить кредит\n\t3. Удалить кредит\n\t4. Изменить кредит\n\t5. Откзываюсь, хочу продолжить\nВаш выбор:\n")
    if choice == '1':
        kredit = Kredit()
        kredit.chtenie()
    elif choice == '2':
        kredit = Kredit()
        kredit.trash()
    elif choice == '3':
        kredit = Kredit()
        kredit.ydalenie()
    elif choice == '4':
        kredit = Kredit()
        kredit.izmenenie()
    elif choice == '5':
        break
    else:
        print("Такой функции нет")