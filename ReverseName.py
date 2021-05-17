def inputData():
    global firstName, lastName
    firstName = str(input('Enter your First Name: '))
    lastName = str(input('Enter your Last Name : '))


def printData():
    print("The name in reverse order is " + str(lastName) + " " + str(firstName))


def main():
    print('Reverse Name Program')
    print('This program is designed to accepts the user\'s first and last name and print them in reverse order with a '
          'space between them.')
    inputData()
    printData()


main()
