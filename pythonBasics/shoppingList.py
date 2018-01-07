# make a list to hold onto our items
shopping_list = []
# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")

# be able to quit the app
    if new_item == "DONE":
        break

# ask for new items
    shopping_list.append(new_item)
# add new items to our list


# print out he list
print("Heres your list:")
for item in shopping_list:
    print(item)