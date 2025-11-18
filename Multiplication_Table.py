# MULTIPLICATION TABLE

num = int(input("Enter Number:"))
start = int(input("Enter start value:"))
end = int(input("Enter end value:"))
for i in range(start, end+1):
	print(num, "*", i, "=", num*i)