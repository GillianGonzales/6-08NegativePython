#
# Created By Gillian Gonzales
# Created On April 15
#
# This program will multiply two numbers

print("Multiply two integers")

print("")

print("Integer1: ")

number1 = int(input())

print("Integer2: ")

number2 = int(input())

if (number1 < 0) and (number2 < 0 ) :	
	number1 = str(number1)
	number1 = number1.replace("-","")
	number2 = str(number2)
	number2 = number2.replace("-","")
elif (number1 < 0 ) and (number2 > 0 ) :
	number1 = str(number1)
	number1 = number1.replace("-","")
	number2 = str(number2)
	number2 = number2.replace("","-", 1)
pass

number1 = int(number1)
number2 = int(number2)

one = 1
answer = number2

for loop in range(one,number1):
	answer = answer + number2
pass

print("")

print ("Your answer is:") 
print (answer)

print("")

input("End of program")

