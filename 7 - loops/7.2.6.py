shopping_list = input("Enter shopping list: ").split(',')
exit = False
while not exit:
    choice = int(input("""Choose one of the following
1 - Print shopping list
2 - print number of items in shopping list
3 - Product search
4 - Product count
5 - Product delete
6 - Product add
7 - Print all invalid products
8 - Remove duplicates
9 - Exit
Your choice here: """))
    if choice == 1:
        print(shopping_list)
    elif choice == 2:
        print(len(shopping_list))
    elif choice == 3:
        product = input("Enter product name: ")
        if product in shopping_list:
            print("True")
        else:
            print("False")
    elif choice == 4:
        product = input("Enter product name: ")
        print(shopping_list.count(product))
    elif choice == 5:
        product = input("Enter product name: ")
        shopping_list.remove(product)
    elif choice == 6:
        product = input("Enter product name: ")
        shopping_list.append(product)
    elif choice == 7:
        for product in shopping_list:
            if len(str(product)) < 3 or not str(product).isalpha():
                print(product)
    elif choice == 8:
        for product in shopping_list:
            if shopping_list.count(product) > 1:
                shopping_list.remove(product)
            
    elif choice == 9:
        exit = True
    