#  ............................................Get 4 number from user and print greater number....................................................
print("ENter numbers to find greatest number\n")
num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
num3 = int(input("Enter 3rd number = "))
num4 = int(input("Enter 4th number = "))

greatest = num1
if num2 > greatest:
    greatest =num2
if num3 > greatest:
    greatest =num3
if num4 > greatest:
    greatest = num4
print(greatest,"is greatest number")        
        
#.............. .................................get value from user and set in list ........................
print("Enter number to set in list i sorted form\n")
a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
c = int(input("Enter 3rd number = "))
numbers = [a, b, c]
numbers.sort()
print(numbers)

#.............................................get marks from user and print Grade.......................................................

marks=int(input("enter marks to check Grade= "))
if marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print("Fail")

# ............................Get marks of subject and take average and and print pass or fail...............................................

urdu = int(input("Enter urdu marks = "))
math = int(input("Enter math marks = "))
eng = int(input("Enter eng marks = "))
avg= (eng + math + urdu) / 3
if(urdu<33 or math<33 or eng<33):
    print("fail its less than 33")
elif(avg<40):
    print("Fail")
else:
    print("You are pass")

# ...............................Get names from user and match name is found in lis or not...............................
names =  ["Hamood", "Tanveer", "Zeeshan"]
namein_list = input("Enter name to find from list= ")
if namein_list in names:
    print("Name found in list")
else:
    print("Name not found in list")
