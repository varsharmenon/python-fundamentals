word = str(input("Enter string:"))
reverse = word[-1:-(len(word)+1):-1]
if word.upper() == reverse.upper():
    print(f"{word} is a palindrome!")
else:
     print(f"{word} is not a palindrome!")