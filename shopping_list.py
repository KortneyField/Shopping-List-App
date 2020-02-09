
shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("Added: {} to thte list".format(len(shopping_list)))

def show_help():
    print("Enter 'DONE' to stop the program")
    print("Enter 'HELP' to display help")
    print("Enter 'SHOW' to display your shopping list")
    print("What should we pick up from the store? ")

def show_list():
    print("YOUR SHOPPING LIST:")
    for item in shopping_list:
        print (item)

show_help()
while True:
    new_item = input(":::  ")
    if new_item == "DONE":
        break;
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)
