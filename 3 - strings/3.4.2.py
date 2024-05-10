message = input("Please enter a string: ")
first_letter = message[0]
message = message[1:]
print(first_letter + message.replace(message[0], "e"))
