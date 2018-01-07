# Have a help
# have a show

shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    # NOTICE THE THREE QUOTES HERE!
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to show available commands.
Enter 'SHOW' to see your current list. 
""")


def show_list():
    print("Heres your list:")
    for item in shopping_list:
        print(item)

def add_new_item(item):
     shopping_list.append(new_item)
     print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_new_item(new_item)
   