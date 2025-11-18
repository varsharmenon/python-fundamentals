# DIGITS OF A NUMBER
num = int(input("Enter a number:"))
copy = num
while num>0:
	digit = num % 10
	num = num//10
	print(digit, end = ',')
