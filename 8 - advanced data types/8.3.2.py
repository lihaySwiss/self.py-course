id = {'first_name' : 'Mariah', 'last_Name' : 'Carey', 'birth_date' : '27.03.1970', 'hobbies' : ['Sing', 'Compose', 'Act']}

choice = int(input("Enter a choice from 1 - 7: "))
if choice == 1:
    print(id['last_Name'])
elif choice == 2:
    print(id['birth_date'][3:5])
elif choice == 3:
    print(len(id['hobbies']))
elif choice == 4:
     print(id['hobbies'][-1])
elif choice == 5:
    id['hobbies'].append('Cooking')
elif choice == 6:
    temp = id['birth_date'].split('.')
    id['birth_date'] = tuple([int(temp[0]), int(temp[1]), int(temp[2])])
    print(id['birth_date'])
elif choice == 7:
    id['age'] = 50
    print(id['age'])