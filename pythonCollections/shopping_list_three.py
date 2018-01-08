import os
shopping_list = []

def clear_screen():
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')


def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    # NOTICE THE THREE QUOTES HERE!
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show available commands.
Enter 'SHOW' to see your current list. 
""")


def show_list():
    clear_screen()
    print("Heres your list:")
    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

    print("-"*10)

def add_new_item(item):
    show_list()
    if len(shopping_list):
        position =  input("Where should I add {}?\n"
                            "Press ENTER to the end of the list\n"
                            "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)
    
    show_list()

# show_list()
show_help()

while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    add_new_item(new_item)
   