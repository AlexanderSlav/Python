from datetime import date

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


def visualisation_of_commands(command_list):
    print('The command list: ')
    for key, values in command_list.items():
        print(key, ' - ', values)



def date_check(date):
    date = date.split('/')
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
    if int(date[1]) > 12 or int(date[1]) < 0:
        print("Wrong number of month, you can choose digit from 1 to 12 ")
        return 0
    if int(amount_of_days[date[1]]) < int(date[0]):
        print("Wrong amount of days, there is only: " + amount_of_days[date[1]] + " in this month")
        return 0
    if int(date[0]) < 0:
        print("Number of day must be > 0")
    if int(date[2]) <= 0 :
        print("Year can not be lower than zero or equal to it")
        return 0
    return 1


def number_check(number):
    if number[0] == '+':
        number = number.replace('+7','8')
    if len(number) != 11 :
        print("The number must consist of 11 digits")
        return 0
    if number.isdigit() is False:
        print("The number must consist of only digits")
    else :
        return 1

def add_persons(phone_book, name, number, date):
    case = 0
    name_2, number_2, date_2 = '','',''
    for key in phone_book.keys():
        if key.split()[0] == name.split()[0] and key.split()[1] == name.split()[1]:
            print("We already have such person in our Phonebook.\n"
                  "1 - You can change the data about an existing person\n"
                  "2 - Or you can change name or surname of your new record\n"
                  "3 - Back to menu\n")
            print("Choose the number of the command:")
            command_add = input()
            if command_add == "1":
                print('The data about existing person:' , *phone_book[key])
                print('If you want to change number press  1 \n'
                      'If you want to change date of birthday press 2 \n')
                change_n = input()
                if change_n == "1":
                    new_number = input()
                    while number_check(new_number) == 0:
                        print("Phone number must consist of digits only, please try again:",end = ' ')
                        new_number = input()
                    phone_book[key][0] = new_number
                    return 0
                if change_n == "2":
                    new_date = input()
                    phone_book[key][1] = new_date
                    return 0
            if command_add == "2":
                print("Enter new full name, phone number and date of birthday please:")
                name_2 = input()
                number_2 = input()
                while number_check(number_2) == 0:
                    print("Phone number must consist of digits only, please try again:")
                    number_2 = input()
                date_2 = input()
                case = '1'
            if command_add == "3":
                return 0
    if case == '1':
        add_persons(phone_book, name_2, number_2, date_2)
        print('Person was successfully added!')
    else:
        phone_book[name] = [number, date]
        print('Person was successfully added!')



def search(d, ob1 , ob2 , ob3 , ob4  ):  # ob1 - name , ob2 - surname , ob3 - number , ob4 - date
    # SEARCH BY NAME
    if ob1 != "No" and (ob2 == "No" and ob3 == "No" and ob4 == "No"):
       for key, (number, date) in d.items():
           if key.split()[0] == ob1:
              print(key, number, date)

    # SEARCH BY SURNAME
    if ob2 != "No" and (ob1 == "No" and ob3 == "No" and ob4 == "No"):
       for key, (number, date) in d.items():
           if key.split()[1] == ob2:
              print(key, number, date)

    # SEARCH BY PHONE NUMBER
    if ob3 != "No" and (ob1 == "No" and ob2 == "No" and ob4 == "No"):
        for key, (number, date) in d.items():
            if number == ob3:
                print(key, number, date)

    # SEARCH BY DATE OF BIRTHDAY
    if ob4 != "No" and (ob1 == "No" and ob2 == "No" and ob3 == "No"):
        for key, (number, date) in d.items():
            if date == ob4:
                print(key, number, date)

    # SEARCH BY FULL NAME
    if ob1 != "No" and ob2 != "No" and (ob3 == "No" and ob4 == "No"):
        for key, (number, date) in d.items():
            if key.split()[0] == ob1 or key.split()[1] == ob2 :
                print(key, number, date)

    # SEARCH BY DATE AND SURNAME
    if ob4 != "No" and ob2 != "No"  and (ob3 == "No" and ob1 == "No"):
        for key, (number, date) in d.items():
            if key.split()[1] == ob2:
                print(key, number, date)

def visualisation(phone_book):
        print("This is  our phone book")
        print("Output format is Name Surname:Number:Date of birth(if exists)")
        print("Date of birth format: XX/XX/XXXX\n")
        for name, value in phone_book.items():
            if len(value) != 1:
                print(name, value[0], value[1], sep=':')
            else:
                print(name, value[0], sep=':')


def age_of_the_person(phone_book, name):
    if name not in phone_book:
        print("Sorry, we don't have this person in our phone book")
    elif len(phone_book[name]) == 1:
        print("We haven't information about person's birthday")
    else:
        today = date.today()

        split_date = phone_book[name][1].split('/')
        born_year = int(split_date[2])
        born_month = int(split_date[1])
        born_day = int(split_date[0])

        age = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
        print('The age of the person: {} years'.format(age))




def del_person(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print('{} was deleted from your phone book'.format(name))
    else:
        print(color.RED + "We have not person with such name in Phone book"+ color.END)


def get_ph_number(phone_book, name):
    if name in phone_book:
        print("This is number: " + str(phone_book[name][0]) + " of " + str(name))


def change_name(phone_book,full_name):
  if full_name not in phone_book:
      print('Sorry, we have not such person in our Phone book')
  else:
      print('\nPlease, enter new name and surname')
      print('Example: Alex Bystrov')
      print('Input here:', end=' ')
      new_name = input()
      while new_name in phone_book:
          print('Sorry, we already have such person in our Phone book\n')
          print('Please, enter new name and surname')
          print('Example: Alex Bystrov')
          print('Input here:', end=' ')
          new_name = input()

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
        phone_book[name][0] = new_number


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

