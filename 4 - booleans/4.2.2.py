palindrome = input("Enter a word: ").lower()
palindrome = palindrome.replace(" ","")
if(palindrome == palindrome[::-1]):
    print("OK")
else:
    print("NOT")