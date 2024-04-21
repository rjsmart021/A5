#Lesson 5:Assignments ] Python Functions
#1.The Calculator App
d1a = input('Do you want to find the sum, diference, multiply, or divide?')
if d1a == "sum":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        print(num1 + num2,"The sum of the numbers!")
elif d1a == "diference":
        dif1 = int(input("Enter an integer: "))
        dif2 = int(input("Enter an integer: "))
        print(dif1 - dif2,"The diference of the numbers!")
elif d1a == "multiply":
        Mult1 = int(input("Enter an integer: "))
        Mult2 = int(input("Enter an integer: "))
        print(Mult1 * Mult2, "The product is!")
elif d1a =="divide":
    Div1 = int(input("Enter an integer: "))
    Div2 = int(input("Enter an integer: "))
    if Div2 == 0:
         print("Denominator is zero")
    else:
        print(Div1 / Div2, "the quotient!")
#2. The Shopping List Maker
#Task 1
# use a fuction we can call in it use while loop to ask what we want to add to get users input their input add to my list by apend is the best way to add
#add it to back of the list let them continue to add things
Shoping_list = ['Ice cream', 'jello', 'gummies', 'life savers']
print("lets go shopping")
action = input("go, add,remove, or stop")
print(Shoping_list)
if action == "go":
    print("Shoping is a go")
elif action == "add":
     print("add an item to the shoping list")
     Shoping_list.append(input("Enter an item"))
     print(Shoping_list)
elif action=="remove":
    print("remove an item from the shoping list")
    Shoping_list.remove(input("Enter an item to remove"))
    print(Shoping_list)
else:
    action == "stop"
    print("Shoping Complete")
#Remove an item from the list
#3
#Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
def Average(grades):
    return sum(grades)/ len(grades)
print("Average of the grades =")
print(Average(grades))
#Task 2 

def low(grades):
    return min(grades)
print("Lowest grade =")
print(min(grades))
#BONUS
for grade in grades:
    if grade >= 90:
        print("Your Grade is an A")
    elif grade  >=80:
        print("Your grade is a B")
    else:
        print("Your grade is a C")