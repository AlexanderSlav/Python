import functions as func

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


def main():
    command_list = {
        '1. Stop': 'If you want to stop using our Phone book, you should use this command',
        '2. Add persons': 'You can add persons to Phone book',
        '3. Visualisation': 'You can see all elements of  Phone book and some information about it',
        '4. Search': 'Searching over phone book by one or several fields',
        '5. Get the age of the person': 'You can get the actual age of the person',
        '6. Change data': 'You can change the information about existing person',
        '7. Get number': 'You can get the phone number of the person',
        '8. Delete person': 'You can delete a record about the person',
        '9. Compare age of persons': 'You can find out how many people are younger/older/equal than/to N years old.'
                                     'You should enter the parameter N',
        '10. Clear screen': 'You can clear screen if you want'
        }
    phone_book = {}

    with open("surname_numbers.txt") as file:
        for line in file:
            key, *value = line.replace('\n', ':').split(':')
            phone_book[key] = value[:-1]

    while True:
        print('Welcome to our phone book!')
        func.visualisation_of_commands(command_list)
        print("Enter the number of the  command, please:", end=' ')
        command = input()
        if command == '1':
            break

        elif command == '2':
            print('Enter your data about person.The format of data is ' + color.BOLD +
                  'Name Surname:Number:Date of birth(if you want)' + color.END)
            print('Date of birth format: XX/XX/XXXX')
            print('Example: Alex Bystrov:89100000000:01/04/1999', end=' ')
            data = input().replace('\n', ':').split(':')
            while len(data) < 2:
                print('Wrong, format. You should enter at least full name and phone number.')
                print('Example: Alex Bystov:89100000000:01/04/1999')
                print('Please, try again here:', end=' ')
                data = input().replace('\n', ':').split(':')
            name, *value = data
            if len(value) > 1:
                number = value[0]
                date = value[1]
            else:
                number = value[0]
                date = ''

            while func.number_check(number) == 0:
                print("Please try again, enter only number:", end=' ')
                number = input()
            while func.date_check(date) == 0:
                print("Please try again,enter only date:", end=' ')
                date = input()
            while func.name_check(name) == 0:
                print("Please try again,enter name and surname:", end=' ')
                name = input()
            name = name.title()
            if number[0] == '+' and number[1] == '7':
                number = number.replace('+7', '8', 1)
            func.add_persons(phone_book, name, number, date)

        elif command == '3':
            func.visualisation(phone_book)

        elif command == '4':
            print("Hy! Let's search for someone. You have 4 parameters to search \n"
                  "Name Surname Number Date \n" 
                  "1. You can search by Name, you should enter: Name _ _ _ \n"
                  "2. You can search by Surname, you should enter: _ Surname _ _\n"
                  "3. You can search by Number, you should enter: _ _ Number _\n"
                  "4. You can search by Birth Date, you should enter: _ _ _ Date\n"
                  "5. You can search by Birth Date and Surname at the same time, you should enter: _ Surname _ Date\n"
                  "6. You can search by Name and Surname at the same time, you should enter: Name Surname _ _\n")
            print('Example: Petr _ _ _')
            print('Enter your data:', end=' ')
            data = input().split()
            while len(data) != 4:
                print('Wrong, format. You should search by 4 parameters.')
                print('Example: Petr _ _ _  or _ Slavutin _ _ _')
                print('Please, try again here:', end=' ')
                data = input().split()
            ob1, ob2, ob3, ob4 = data[0], data[1], data[2], data[3]
            func.search(phone_book, ob1, ob2, ob3, ob4)

        elif command == '5':
            print('Choose the name and surname please.')
            print('Example: Alex Bystov', end=' ')
            name = input()
            while func.name_check(name) == 0:
                print("Please try again, enter name and surname:", end=' ')
                name = input()
            name = name.title()
            func.age_of_the_person(phone_book, name, 0)

        elif command == '6':
            print('What data do you want to change?')
            print('1. Name and surname')
            print('2. Number')
            print('3. Birth date')
            print('Enter the number of the command here:', end=' ')
            choice = input()
            if choice == '1':
                print('Choose the name and surname, which you want to change.')
                print('Example: Alex Bystov.')
                print('Enter your data here:', end=' ')
                name = input()
                while func.name_check(name) == 0:
                    print("Please try again,enter name and surname:", end=' ')
                    name = input()
                name = name.title()
                func.change_name(phone_book, name)
            if choice == '2':
                print('Choose the name and surname, which number you want to change.')
                print('Example: Alex Bystov.')
                print('Enter your data here:', end=' ')
                name = input()
                while func.name_check(name) == 0:
                    print("Please try again,enter name and surname:", end=' ')
                    name = input()
                name = name.title()
                func.change_number(phone_book, name)
            if choice == '3':
                print('Choose the name and surname, which birth date you want to change.')
                print('Example: Alex Bystov.')
                print('Enter your data here:', end=' ')
                name = input()
                while func.name_check(name) == 0:
                    print("Please try again,enter name and surname:", end=' ')
                    name = input()
                name = name.title()
                func.change_date(phone_book, name)

        elif command == '7':
            print('Choose the name and surname, which number you want to know please.')
            print('Example: Alex Bystov.')
            print('Enter your data here:', end=' ')
            name = input()
            while func.name_check(name) == 0:
                print("Please try again,enter name and surname:", end=' ')
                name = input()
            name = name.title()
            func.get_ph_number(phone_book, name)

        elif command == '8':
            print("Choose the name and surname, which  you want to delete please.")
            print('Example: Alex Bystov.')
            print('Enter your data here:', end=' ')
            name = input()
            while func.name_check(name) == 0:
                print("Please try again,enter name and surname:", end=' ')
                name = input()
            name = name.title()
            func.del_person(phone_book, name)
        elif command == '9':
            print('Please enter the age with that you want compare persons age in Phone book (N):', end=' ')
            comparison_number = input()
            while func.comparison_number_check(comparison_number) == 0:
                print('Wrong input format, please try again:', end='')
                comparison_number = input()
            print('Do you want to watch people younger(enter 1), older(enter 2) '
                  'or equal(enter 3) than {}'.format(comparison_number))
            print('Enter data here', end=' ')
            parameter = input()
            while parameter != '1' and parameter != '2' and parameter != '3':
                print('Wrong input format, you should enter 1 or 2 or 3 ')
                print('Example: 1')
                print('Enter your parameter here:', end=' ')
                parameter = input()
            func.compare_by_age(phone_book, comparison_number, parameter)
        elif command == '10':
            func.cls()

    with open('surname_numbers.txt', 'w') as out:
        for key, value in phone_book.items():
            out.write('{}:{}:{}\n'.format(key, *value))
    print('Thank you for using our Phone book!')
    print('We hope, we will see you again! Good Lick!')


if __name__ == "__main__":
    main()
