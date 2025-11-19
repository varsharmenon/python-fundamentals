word = str(input("Enter Word:"))
vow = "aeiouAEIOU" 
sum = 0
for i in range (0, len(word)):
    if word[i] in vow:
        sum+=1
print(f"The number of vowels in {word} is:", sum)