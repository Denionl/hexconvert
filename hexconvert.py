def info_display(): # Display welcome and instruction info of the program
    welcome_information = ("Welcome to smart conversion!\n")
    instruction_infomation = ('Instruction: 1) b stands for Binary 2) d stands for Demical 3) hex stands for Hexadecimal\n') 
    print(welcome_information)
    print(instruction_infomation)


def converse(): # Main function of the prgram which include I/O and caculation of value
    user_input_value_type = str(input('Pleas input the type of the value you want to converse from: '))
    user_input_value = (input('Pleas input the value you want to converse: '))
    targaret_type = str(input('Pleas input the typel of the value you want to converse to: '))
    if user_input_value_type == 'd' and targaret_type == 'b':
        user_input_value = int(user_input_value)
        print(f'Binary value is: {user_input_value:08b}')
    elif user_input_value_type == 'b' and targaret_type == 'd':
        try:
            user_input_value = int(user_input_value,2)
        except ValueError:
            print("You did not enter a binary number!")
        print(f'Binary value is: {user_input_value:d}')





def main():
    info_display()
    converse()
    print("Hello")



if __name__ == '__main__': main()


