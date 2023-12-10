import sqlite3
from typing import List

conn = sqlite3.connect("database.db")
cu = conn.cursor()


def klientyra():
    while True:
            try:
                h = input(
                    'Что вы хотите сделать?\n\t1. Посмотреть варианты кредитов\n\t2. Выбрать кредит\n\t3. Забыл свой id\n')
                if h == '1':
                    conn.commit()
                    cu.execute('SELECT * FROM Credit')
                    rows = cu.fetchall()
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
                if h == '2':
                    cu.execute('SELECT * FROM Credit')
                    rows = cu.fetchall()
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
                    print('Если вас нет еще в таблице..Обратитесь к сотруднику банка и попросите выдать вам ID')
                    client_id = int(input("Введите ваш ID: "))
                    credit_id = int(input("Введите ID выбранного кредита: "))
                    cu.execute("UPDATE Clients SET Credit_id = ? WHERE id_clients = ?", (credit_id, client_id))
                    conn.commit()
                    print('Кредит добавлен')
                    print('Выберите сотрудника, который будет вам помогать!')
                    cu.execute('SELECT * FROM Rabotniki')
                    rows = cu.fetchall()
                    print("ВСЕ НАШИ СОТРУДНИКИ")
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
                    rab_id = int(input("Введите ID выбранного сотрудника: "))
                    print('Отличный выбор!')
                    cu.execute("UPDATE Clients SET Rab_id = ? WHERE id_clients = ?", (rab_id, client_id))
                    conn.commit()
                if h == '3':
                    last_name = input("Введите фамилию пользователя: ")  # Введите фамилию пользователя
                    cu.execute("SELECT id_clients Surname FROM Clients WHERE Surname=?", (last_name,))
                    user = cu.fetchone()
                    if user:
                        print(f"Найден пользователь с ID {user[0]}")
                    else:
                        print("Пользователь с указанной фамилией не найден")
            except:
                print('Ошибка')
            continue



klientyra()
