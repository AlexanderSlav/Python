import os
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
        '1. Stop': "If you want to stop using our Phone book, you should use this command",
        '2. Add persons': "You can add persons to Phone book",
        '3. Visualisation': "You can see all elements of  Phone book and some more information about it",
        '4. Search' : 'Searching over phone book by one or several fields',
        '5. Get the age of the person': "You can get the actual age of the person",
        '6. Update data': "You can change the name of person",
        '7. Get number': "You can get the phone number of the person",
        '8. Delete person': 'You can delete a record about the person'
        }
    phone_book = {}


    with open("surname_numbers.txt") as file:
        for line in file:
            key, *value = line.split(':')
            phone_book[key] = value[0:len(value)-1]
    # The visualisation of  available commands

    print('Enter the command, please:')
    flag = True
    while flag:
        print('Welcome to our phone book!')
        func.visualisation_of_commands(command_list)
        print("Enter the number of the  command, please:", end=' ')
        command = input()
        if command == '1':
            flag = False
            break

        elif command == '2':
            func.cls()
            print('Enter your data (Name Surname:Number:Date of birth(if you want)')
            print('Date of birth format: XX/XX/XXXX')
            print('Example: Alex Bystov:89100000000:01/04/1999',end = ' ')
            name, number, date = input().replace('\n', ':').split(':')
            while func.number_check(number) == 0:
                print("Please try again, enter only number:", end=' ')
                number = input()
            while func.date_check(date) == 0:
                print("Please try again,enter only date:", end=' ')
                date= input()
            func.add_persons(phone_book,name, number, date)

        elif command == 'Visualisation':
            func.cls()
            func.visualisation(phone_book)

        elif command == 'Search':
            ob1, ob2, ob3, ob4 = input().split()
            func.search(phone_book, ob1, ob2, ob3, ob4)

        elif command == 'Get the age of the person':
            print('Choose the name and surname please: ')
            name = input()
            surname = input()
            print('The actual age of ' + name + ' ' + surname + ' is ' + str(how_many_years(d, name, surname)))

        elif command == 'Change':
            print("Choose the old name please:")
            old_name = input()
            print('Choose the new name please:')
            new_name = input()
            change_name(d, old_name, new_name)

        elif command == 'Change number':
            print('Choose the name please:')
            name = input()
            print('Enter the new phone number:')
            number = input()
            change_ph_number(d, name, number)

        elif command == 'Get number':
            print("Choose the name, which number you want to know please :")
            name = input()
            print("This is number: "+get_ph_number(d, name)+" of "+str(name))

        elif command == 'Delete person':
            name = input()
            del_person(d, name)

    with open('surname_numbers.txt', 'w') as out:
        for key, (number, date) in phone_book.items():
            out.write('{}:{}:{}:\n'.format(key,number,date))


if __name__ == "__main__":
    main()
