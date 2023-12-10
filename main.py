import os
import sqlite3


def sozdaniefaila():
    if not os.path.exists('users.txt'):
        with open('users.txt', 'w'):
            pass


def addrabotnika(login: str, password: str):
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()
    for user in users:
        razdel = user.split(':')
        if login == razdel[0]:
            return False

    with open('users.txt', 'a') as f:
        f.write(f'{login}:{password}\n')
    return True


def getrabotnik(login: str, password: str):
    with open('users.txt', 'r') as f:
        users = f.read().splitlines()

    for user in users:
        razdel = user.split(':')
        if login == razdel[0] and password == razdel[1]:
            return True
    return False


sozdaniefaila()


def main():
    while True:
        try:
            print('''Добро пожаловать! Выберите пункт меню:
                1. Вход
                2. Регистрация
                3. Выход''')

            polzovatel = input()
            if polzovatel == '1':
                print('Введите логин:')
                login = input()

                print('Введите пароль:')
                password = input()

                result = getrabotnik(login, password)

                if result:
                    ktoti = int(input("Выберите за кого вы хотите авторизоваться?\n"
                                      "\t1. Клиент\n"
                                      "\t2. Работник\n"
                                      "\t3. Администратор\n"))
                    if ktoti == 1:
                        print('Вы вошли в систему, как клиент')
                        vibor = int(input("Вы в системе что вы хотите сделать:\n"
                                          "\t1. Выбрать кредит\n"
                                          "\t2. Выйти\n"))
                        if vibor == 1:
                            from DeiKlientov import klientyra
                        if vibor == 2:
                            print("Спасибо, что выбрали наш банк! Самый надожный банк в мире))))")
                            break
                        if vibor == 1:
                            print('j')
                    if ktoti == 2:
                        specpassword = int(input('Введите код работника: '))
                        while True:
                            if specpassword == 0000:
                                print('Вы вошли в систему, как работник')
                                vibor = input("Вы в системе что вы хотите сделать:\n"
                                              "\t1. Добавить/удалить/изменить/просмотреть клиентов\n"
                                              "\t2. Добавить/удалить/изменить/просмотреть кредиты\n"
                                              "\t4. Выйти\n")
                                if vibor == '1':
                                    from ClassDlyaKlientiv import Clients
                                if vibor == '2':
                                    from ClassDlyaTabl import Kredit
                            else:
                                print('Вы ввели не верный пароль. Попробуйте снова')
                    if ktoti == 3:
                        specpassword = int(input('Введите код администратора: '))
                        while True:
                            if specpassword == 560037:
                                print('Вы вошли в систему, как администратор')
                                vibor = input("Вы в системе что вы хотите сделать:\n"
                                              "\t1. Добавить/удалить/изменить/просмотреть кредиты\n"
                                              "\t2. Добавить/удалить/изменить/просмотреть сотрудников\n"
                                              "\t3. Добавить/удалить/изменить/просмотреть клиентов\n"
                                              "\t3. Изменить свои данные по фану\n"
                                              "\t5. Выйти\n")
                                if vibor == '1':
                                    from ClassDlyaTabl import Kredit
                                if vibor == '2':
                                    from ClassDlyaRabov import Rabotniki
                                if vibor == '3':
                                    from ClassDlyaKlientiv import Clients
                                if vibor == '3':
                                    from ClassAdm import Adm
                                if vibor == '5':
                                    break
                            else:
                                print('Вы ввели не верный пароль. Попробуйте снова')
                                break
                else:
                    print('Неверный логин или пароль')
            elif polzovatel == '2':
                print('Введите логин:')
                login = input()

                print('Введите пароль:')
                password = input()

                print('Повторите пароль:')
                password_repeat = input()

                if password != password_repeat:
                    print('Пароли не совпадают!')
                    continue

                result = addrabotnika(login, password)

                if not result:
                    print('Пользователь с таким логином уже существует')
                else:
                    print('Регистрация прошла успешно!')

            elif polzovatel == '3':
                print('Завершение работы')
                break
        except:
            print('Ошибка')
            continue

print("\U0001F31F" * 20)
main()