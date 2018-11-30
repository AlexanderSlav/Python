from datetime import date
import os


class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Проверка числа для сравнения всех записей словаря по возрасту
def comparison_number_check(comparison_number):
    if comparison_number == '':
        print('Nothing was entered.The age number must contain at least one digit')
        return 0
    if comparison_number.isdigit() is False:
        print('Ops, the age number must be a digit, it should not contain symbols')
        return 0
    if int(comparison_number) < 0:
        print('The age number should be >= 0')
        return 0
    return 1


# Специальная проверка имени для функции поиска
def name_check_search(ob1):
    punctuation_marks = ['!', '.', ',', '/', ';', ':', '-', '(', ')', '?', '>', '<', '[', ']', '{', '}']
    for x in punctuation_marks:
        if x in ob1:
            print('Name should not contain punctuation marks')
            return 0
    if ob1 == '':
        print('Nothing was entered.Name  must contain at least one symbol')
        return 0
    if ob1.isdigit() is True:
        print('Name must contain at least one letter')
        return 0
    return 1


# Специальная проверка фамилии для функции поиска
def surname_check_search(ob2):
    punctuation_marks = ['!', '.', ',', '/', ';', ':', '-', '(', ')', '?', '>', '<', '[', ']', '{', '}']
    for x in punctuation_marks:
        if x in ob2:
            print('Surname should not contain punctuation marks')
            return 0
    if ob2 == '':
        print('Nothing was entered.Surname must contain at least one symbol')
        return 0
    if ob2.isdigit() is True:
        print('Surname must contain at least one letter')
        return 0
    return 1


# Проверка полного имени (Имя,Фамилия) на корректность
def name_check(name):
    punctuation_marks = ['!', '.', ',', '/', ';', ':', '-', '(', ')', '?', '>', '<', '[', ']', '{', '}', '_']
    if len(name.split()) != 2:
        print('The wrong format of full name, you should enter Name and Surname.')
        print('Example: Alex Bystov')
        return 0
    if name.split()[0].isdigit() is True or name.split()[1].isdigit() is True:
        print('Name and surname must contain at least one letter')
        return 0
    if not (name.split()[0][0].isalpha() and name.split()[1][0].isalpha()):
        print('Name and Surname input mistake!')
        print('The first symbols of Name and Surname should be letters!')
        return 0
    for x in punctuation_marks:
        if x in name:
            print('Name and surname should not contain punctuation marks')
            return 0
    return 1


def date_check(date):
    amount_of_days = {
        '01': '31',
        '02': '28',
        '03': '31',
        '04': '30',
        '05': '31',
        '06': '30',
        '07': '31',
        '08': '31',
        '09': '30',
        '10': '31',
        '11': '30',
        '12': '31',
    }
    if date == '':
        return 1

    date = date.split('/')
    if len(date) != 3:
        print('The wrong format of date, please try again')
        print('Example: Alex Bystov:89100000000:01/04/1999')
        return 0
    if date[0].isdigit() is False or date[1].isdigit() is False or date[2].isdigit() is False:
        print('Wrong format of date, date must contain digits only,  please try again')
        print('Date of birth format: XX/XX/XXXX')
        return 0
    if len(date[0]) != 2 or len(date[1]) != 2:
        print('Wrong format of date, please try again')
        print('Date of birth format: XX/XX/XXXX')
        return 0
    if int(date[1]) > 12 or int(date[1]) <= 0:
        print("Wrong number of month, you can choose digit from 1 to 12 ")
        return 0
    if int(amount_of_days[date[1]]) < int(date[0]):
        print("Wrong amount of days, there is only: " + amount_of_days[date[1]] + " in this month")
        return 0
    if int(date[0]) <= 0:
        print("Number of day must be > 0")
        return 0
    if int(date[2]) <= 0:
        print("Year can not be lower than zero or equal to it")
        return 0
    return 1


def number_check(number):
    if number[0] == '+' and number[1] == '7':
        number = number.replace('+7', '8', 1)
    if number.isdigit() is False:
        print("The number must not contain letters or symbols")
        return 0
    if len(number) != 11:
        print("The number must consist of 11 digits")
        return 0
    else:
        return 1


def visualisation_of_commands(command_list):
    print('The command list: ')
    for key, values in command_list.items():
        print(key, ' - ', values)


def add_persons(phone_book, name, number, date):
    if name in phone_book:
            print("We already have such person in our Phonebook.\n"
                  "1 - You can change the data about an existing person\n"
                  "2 - Or you can change name or surname of your new record\n"
                  "3 - Back to menu\n")
            print("Choose the number of the command:", end=' ')
            command_add = input()
            if command_add == "1":
                print('The data about existing person:', *phone_book[name])
                print('If you want to change number press: 1 \n'
                      'If you want to change date of birthday press: 2 \n')
                print('Enter the command, please:', end='')
                change_n = input()
                if change_n == "1":
                    print('Please enter new number here:', end=' ')
                    new_number = input()
                    while number_check(new_number) == 0:
                            print("Please try again, enter new number:", end=' ')
                            new_number = input()
                    if new_number[0] == '+' and new_number[1] == '7':
                        new_number = new_number.replace('+7', '8')
                    phone_book[name][0] = new_number
                    print('The phone number of {}  was successfully changed'.format(name))
                    return 0
                if change_n == "2":
                    print('Please enter new date of birth here:', end=' ')
                    new_date = input()
                    while date_check(new_date) == 0:
                        print("Please try again,enter new date:", end=' ')
                        new_date = input()
                    phone_book[name][1] = new_date
                    return 0
            if command_add == "2":
                print("Enter new full name.Example: Alex Bystov")
                new_name = input()
                while name_check(new_name) == 0:
                        print("Please try again,enter name and surname:", end=' ')
                        new_name = input()
                new_name = new_name.title()
                add_persons(phone_book, new_name, number, date)
            if command_add == "3":
                return 0
    else:
        phone_book[name] = [number, date]
        print('Person was successfully added!')


def search(phone_book, ob1, ob2, ob3, ob4):  # ob1 - name , ob2 - surname , ob3 - number , ob4 - date
    flag = False
    # SEARCH BY NAME
    if ob1 != "_" and (ob2 == "_" and ob3 == "_" and ob4 == "_"):
        while name_check_search(ob1) == 0:
            print("Please try again")
            print("To search by Name, you should enter only Name", end=' ')
            ob1 = input()
            while len(ob1.split()) != 1:
                print('Wrong input, you should enter only Name ')
                ob1 = input('Please try again')
        ob1 = ob1.title()
        for key, value in phone_book.items():
            if key.split()[0] == ob1:
                print(key, *value)
                flag = True

    # SEARCH BY SURNAME
    if ob2 != "_" and (ob1 == "_" and ob3 == "_" and ob4 == "_"):
        while name_check_search(ob2) == 0:
            print("Please try again")
            print("To search by Surname, you should enter only Surname ", end=' ')
            ob2 = input()
            while len(ob2.split()) != 1:
                print('Wrong input, you should enter only Surname ')
                ob2 = input('Please try again')
        ob2 = ob2.title()
        for key, value in phone_book.items():
            if key.split()[1] == ob2:
                print(key, *value)
                flag = True
    # SEARCH BY PHONE NUMBER
    if ob3 != "_" and (ob1 == "_" and ob2 == "_" and ob4 == "_"):
        while number_check(ob3) == 0:
            print("Please try again")
            print("To search by Number, you should enter only Number", end=' ')
            ob3 = input()
            while len(ob3.split()) != 1:
                print('Wrong input, you should enter only Number ')
                ob3 = input('Please try again')
        if ob3[0] == '+' and ob3[1] == '7':
            ob3 = ob3.replace('+7', '8', 1)
        for key, value in phone_book.items():
            if value[0] == ob3:
                print(key, *value)
                flag = True

    # SEARCH BY DATE OF BIRTHDAY
    if ob4 != "_" and (ob1 == "_" and ob2 == "_" and ob3 == "_"):
        while date_check(ob4) == 0:
            print("Please try again")
            print("To search by Date, you should enter only Date", end=' ')
            ob4 = input()
            while len(ob4.split()) != 1:
                print('Wrong input, you should enter only Date ')
                ob4 = input('Please try again')

            for key, value in phone_book.items():
                if len(value) > 1:
                    if value[1] == ob4:
                        print(key, *value)
                        flag = True

    # SEARCH BY FULL NAME
    if ob1 != "_" and ob2 != "_" and (ob3 == "_" and ob4 == "_"):
        while name_check_search(ob1) == 0:
            print("Please try again")
            print("To search by Name, you should enter only  Name", end=' ')
            ob1 = input()
            while len(ob1.split()) != 1:
                print('Wrong input, you should enter only Name ')
                ob1 = input('Please try again')
        ob1 = ob1.title()
        while name_check_search(ob2) == 0:
            print("Please try again")
            print("To search by Surname, you should enter only Surname", end=' ')
            ob2 = input()
            while len(ob2.split()) != 1:
                print('Wrong input, you should enter only Surname ')
                ob2 = input('Please try again')
        ob2 = ob2.title()
        for key, value in phone_book.items():
            if key.split()[0] == ob1 and key.split()[1] == ob2:
                print(key, *value)
                flag = True

    # SEARCH BY DATE AND SURNAME
    if ob4 != "_" and ob2 != "_" and (ob3 == "_" and ob1 == "_"):
        while date_check(ob4) == 0:
            print("Please try again")
            print("To search by Date, you should enter only Date", end=' ')
            ob4 = input()
            while len(ob4.split()) != 1:
                print('Wrong input, you should enter only Date ')
                ob4 = input('Please try again')
        while name_check_search(ob2) == 0:
            print("Please try again")
            print("To search by Surname, you should enter only Surname ", end=' ')
            ob2 = input()
            while len(ob2.split()) != 1:
                print('Wrong input, you should enter only Surname ')
                ob2 = input('Please try again')
        ob2 = ob2.title()
        for key, value in phone_book.items():
            if len(value) > 1:
                if value[1] == ob4 and key.split()[1] == ob2:
                    print(key, *value)
                    flag = True
    if not flag:
        print('Sorry, Nothing was found')


def visualisation(phone_book):
        print("This is  our phone book")
        print("Output format is Name Surname:Number:Date of birth(if exists)")
        print("Date of birth format: XX/XX/XXXX\n")
        for name, value in phone_book.items():
            if len(value) != 1:
                print(name, value[0], value[1], sep=':')
            else:
                print(name, value[0], sep=':')


def age_of_the_person(phone_book, name, flag):
    if name not in phone_book:
        print("Sorry, we don't have this person in our phone book")
        return -1
    elif phone_book[name][1] == '':
        if flag == 0:
            print("We haven't information about person's birthday")
        return -1
    else:
        today = date.today()

        split_date = phone_book[name][1].split('/')
        born_year = int(split_date[2])
        born_month = int(split_date[1])
        born_day = int(split_date[0])

        age = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
        if flag == 0:
            print('The age of the person: {} years'.format(age))
        return age


def del_person(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print('{} was deleted from your phone book'.format(name))
    else:
        print(color.RED + "We have not person with such name in Phone book" + color.END)


def get_ph_number(phone_book, name):
    if name in phone_book:
        print("This is number: " + str(phone_book[name][0]) + " of " + name)


def change_name(phone_book, full_name):
    if full_name not in phone_book:
        print('Sorry, we have not such person in our Phone book')
    else:
        print('\nPlease, enter new name and surname')
        print('Example: Alex Bystrov')
        print('Input here:', end=' ')
        new_name = input()
        while name_check(new_name) == 0:
            print("Please try again,enter name and surname:", end=' ')
            new_name = input()
        new_name = new_name.title()
        while new_name in phone_book:
            print('Sorry, we already have such person in our Phone book\n')
            print('Please, enter new name and surname')
            print('Example: Alex Bystrov')
            print('Input here:', end=' ')
            new_name = input()
            while name_check(new_name) == 0:
                print("Please try again,enter name and surname:", end=' ')
                new_name = input()
            new_name = new_name.title()

        phone_book[new_name] = phone_book.pop(full_name)
        print('The name was successfully changed!')


def change_number(phone_book, name):
    if name not in phone_book:
        print('Sorry, we have not such person in our Phone book')
    else:
        print('Please, enter new number')
        print('Example: 89101418745')
        print('Write it here:', end=' ')
        new_number = input()
        while number_check(new_number) == 0:
            print("Please try again, enter only number:", end=' ')
            new_number = input()
        if new_number[0] == '+' and new_number[1] == '7':
            new_number = new_number.replace('+7', '8')
        phone_book[name][0] = new_number
        print('The number was successfully changed!')


def change_date(phone_book, name):
    if name not in phone_book:
        print('Sorry, we have not such person in our Phone book')
    else:
        print('Please, enter new date of birthday')
        print('Example: 12/11/1987')
        print('Write it here:', end=' ')
        new_date = input()
        while date_check(new_date) == 0:
            print("Please try again,enter only date:", end=' ')
            new_date = input()
        phone_book[name][1] = new_date
        print('The date was successfully changed!')


def compare_by_age(phone_book, comparison_number, parameter):
    flag = False
    for person in phone_book:
        if age_of_the_person(phone_book, person, 1) != -1:
            if parameter == '1':
                if age_of_the_person(phone_book, person, 1) < int(comparison_number):
                    flag = True
                    print(person, *phone_book[person])
            if parameter == '2':
                if age_of_the_person(phone_book, person, 1) > int(comparison_number):
                    flag = True
                    print(person, *phone_book[person])
            if parameter == '3':
                if age_of_the_person(phone_book, person, 1) == int(comparison_number):
                    flag = True
                    print(person, *phone_book[person])
    if not flag:
        print('Sorry,nothing was found')


