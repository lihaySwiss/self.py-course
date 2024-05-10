message = input("Please enter a string: ")
middle_index = len(message)//2
print(message[:middle_index:].lower() + message[middle_index::].upper())