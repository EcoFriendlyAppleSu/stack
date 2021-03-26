def menu():
    show_thing = '''
    ------------------------------
    1. Does the Stack empty?
    2. Push Number into Stack
    3. Pop Number in Stack
    4. Show Stack index
    5. System Exit
    ------------------------------
    '''
    print(show_thing)

def isEmpty(stack_list):
    if len(stack_list) == 0:
        print('\tStack is Empty')
    else:
        print('\tStack is not Empty')

def push(stack_list):
    
    while True:
        push_number = input('\tPress input number in Stack :  ')
        if push_number.isdigit() == True:
            push_number = int(push_number)
            stack_list.append(push_number)
            break
        else:
            print("\tUser input isn't digit. Input Right integer number")

def pop(stack_list):
    
    # stack_list.pop(len(stack_list)-1)
    del stack_list[-1]

def show_stack_list(stack_list):
    print("\t",stack_list)

def stack():
    stack_list = [] # start stack list (Is empty now)
    user_choice_list = [1,2,3,4,5] # User menu list. when user input number in this list then program will start
    time_flag = 0 # When people input wrong number over 5 times the system will down
    
    while True:
        menu()
        user_choice = input('\tPress one number 1 to 4 : ')
        if user_choice.isdigit() == True:
            user_choice = int(user_choice)
            if user_choice not in user_choice_list:
                time_flag += 1
                print("\tYou should input right number 1 to 4. If you input wrong number over 5 times the system is going to be down. Current Worng Number : {}".format(time_flag))
                if time_flag == 5:
                    print("\tSystem End")
                    break
            else:
                time_flag = 0
                if user_choice == 1:
                    isEmpty(stack_list)
                elif user_choice == 2:
                    push(stack_list)
                elif user_choice == 3:
                    pop(stack_list)
                elif user_choice == 4:
                    show_stack_list(stack_list)
                else:
                    print('\tSystem Exit. Bye Bye')
                    break
        else:
            print('\tPlease input right number.')
            time_flag += 1
            print("\tYou should input right number 1 to 4. If you input wrong number over 5 times the system is going to be down. Current Worng Number : {}".format(time_flag))
            if time_flag == 5:
                print("\tSystem End")
                break
def main():
    stack()

if __name__ == '__main__':
    main()    