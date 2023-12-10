import sqlite3
from typing import List


# Как сделать проверку на уникальность в базе данных + норм ваще иду или не

class Adm:
    while True:
        try:
            def __init__(self):
                self.conn = sqlite3.connect("database.db")
                self.cu = self.conn.cursor()
                self.sozdanie()

            def sozdanie(self):
                self.cu.execute('''
                            CREATE TABLE IF NOT EXISTS Adm(
                            id INTEGER PRIMARY KEY,
                            Surname TEXT NOT NULL,
                            Namee TEXT NOT NULL,
                            MiddleName TEXT NOT NULL,
                            zp INTEGER NOT NULL
                            )
                        ''')
                #        self.cu.executemany(
                #        "INSERT INTO Adm (Surname,Namee,MiddleName,zp) VALUES (?,?,?,?)",
                #            [('Иванова', 'Юлия', 'Викторовна', 4949390340)])

                self.conn.commit()

            def izmenenie(self):
                while True:
                        value = self.cu.fetchall()
                        if not value:
                            self.cu.execute("SELECT * FROM Adm")
                            self.conn.commit()
                            rows = self.cu.fetchall()
                            print("АДМИНЫ")
                            for row in rows:
                                Namee = str(row[2])
                                MiddleName = str(row[3])
                                zp = str(row[4])
                                Surname = str(row[1])
                                id = str(row[0])
                                print("--------------------------------------------------------")
                                print(
                                    f"ID: {id} | Фамилия: {Surname} | Имя: {Namee} | Отчество: {MiddleName} | Зарплата: {zp}")

                            idyizmen = input('Введите ваш ID для изменения: ')
                            self.cu.execute("SELECT * FROM Adm WHERE id = ?", (idyizmen,))
                            v = self.cu.fetchone()
                            print(v)
                            b = input(
                                "Что конкретно вы хотите изменить?\n\t1. Фамилию \n\t2. Имя\n\t3. Отчество\n\t4. Зпэшка\n\t5. Все вместе\n\t6. Мисс кликнул, теперь назад\n")

                            if b == '1':
                                Surname = input('Введите новую фамилию: ')
                                self.cu.execute("UPDATE Adm SET Surname = ? WHERE id = ?", (Surname, idyizmen))
                                continue
                            elif b == '2':
                                Namee = input('Введите новое имя: ')
                                self.cu.execute("UPDATE Adm SET Suma = ? Namee id = ?", (Namee, idyizmen))
                                continue
                            elif b == '3':
                                MiddleName = input('Введите новое отчество: ')
                                self.cu.execute("UPDATE Adm SET MiddleName = ? WHERE id = ?", (MiddleName, idyizmen))
                                continue
                            elif b == '4':
                                zp = input('Введите новую зп: ')
                                self.cu.execute("UPDATE Adm SET zp = ? WHERE id = ?", (zp, idyizmen))
                                continue
                            elif b == '5':
                                Surname = input('Введите новую фамилию: ')
                                Namee = input('Введите новое имя: ')
                                MiddleName = input('Введите новое отчество: ')
                                zp = input('Введите новую зп: ')
                                self.cu.execute(
                                    "UPDATE Adm SET Surname = ?, Suma = ?, Percent = ?, Godikioplati = ? WHERE id = ?",
                                    (Surname, Namee, MiddleName, zp, idyizmen))
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
        "Вы можете:\n\t1. Изменить свое фио\n\t2. Выйти\nВаш выбор:\n")
    if choice == '1':
        adm = Adm()
        adm.izmenenie()
    elif choice == '2':
        break
    else:
        print("Такой функции нет")
