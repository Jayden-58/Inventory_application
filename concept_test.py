
def Welcome():
    print("hello, welcome to inventory manager.")
    print("enter the function you would like to execute.")


def Main_menu():
    print("1.) Enter an item")
    print("2.) Throw away item")
    choice = input()
    if choice == "1":
        print("Enter an item:")
    elif choice == "2":
        print("delete an item:")
    else:
        print("invalid. please try again")
        Main_menu()

    
def Enter_item():
    print("enter item name: ")


Welcome()
Main_menu()