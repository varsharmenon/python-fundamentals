word = str(input("Enter string to be reversed:"))
print("The reversed string is:", word[-1:-(len(word)+1):-1])