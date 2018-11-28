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
        '6. Change data': "You can change the information about existing person",
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

    while True:
        print('Welcome to our phone book!')
        func.visualisation_of_commands(command_list)
        print("Enter the number of the  command, please:", end=' ')
        command = input()
        if command == '1':
            break

        elif command == '2':
            print('Enter your data about person. The format of data is ' + color.BOLD +
                  'Name Surname:Number:Date of birth(if you want)'+ color.END)
            print('Date of birth format: XX/XX/XXXX')
            print('Example: Alex Bystov:89100000000:01/04/1999',end=' ')
            name, number, date = input().replace('\n', ':').split(':')
            while func.number_check(number) == 0:
                print("Please try again, enter only number:", end=' ')
                number = input()
            while func.date_check(date) == 0:
                print("Please try again,enter only date:", end=' ')
                date= input()
            func.add_persons(phone_book,name, number, date)

        elif command == '3':
            func.visualisation(phone_book)

        elif command == '4':
            print("The format of search is simple, you have 4 parameters to search \n"
                  "Name Surname Number Date \n" 
                  "1. You can search by name, you should enter: Name _ _ _ \n"
                  "2. You can search by surname, you should enter: _ Surname _ _\n"
                  "3. You can search by number, you should enter: _ _ Number _\n"
                  "4. You can search by date, you should enter: _ _ _ Date\n")
            ob1, ob2, ob3, ob4 = input().split()
            func.search(phone_book, ob1, ob2, ob3, ob4)

        elif command == '5':
            print('Choose the name and surname please.')
            print('Example: Alex Bystov', end=' ')
            name = input()
            func.age_of_the_person(phone_book, name)


        elif command == '6':
            print('What data do you want to change?')
            print('1. Name and surname')
            print('2. Number')
            print('3. Date of birthday')
            print('Enter the number of the command here:', end=' ')
            choice = input()
            if choice == '1':
                print('Choose the name and surname, which you want to change.')
                print('Example: Alex Bystov.')
                print('Enter your data here:', end=' ')
                name = input()
                func.change_name(phone_book, name)
            if choice =='2':
                pass


        elif command == '7':
            print('Choose the name and surname, which number you want to know please.')
            print('Example: Alex Bystov.')
            print('Enter your data here:', end=' ')
            name = input()
            func.get_ph_number(phone_book, name)

        elif command == '8':
            print("Choose the name and surname, which  you want to delete please.")
            print('Example: Alex Bystov.')
            print('Enter your data here:', end=' ')
            name = input()
            func.del_person(phone_book, name)

    with open('surname_numbers.txt', 'w') as out:
        for key, (number, date) in phone_book.items():
            out.write('{}:{}:{}:\n'.format(key,number,date))


if __name__ == "__main__":
    main()
