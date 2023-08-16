# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def add(v1, v2):
    return v1 + v2


def main():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome to PyCalculator')
    print('What action do you want to take?')
    print('1. Add')

    while True:
        option = input('Enter option #: ')

        try:
            value_one = float(input('Enter first number: '))
            value_two = float(input('Enter second number: '))
        except ValueError:
            print('One of the numbers entered was invalid')
            continue

        if option == '1':
            print('{} added to {} is {}'.format(value_one, value_two, add(value_one, value_two)))

        if input('Another calculation (y/n)?') == 'n':
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
