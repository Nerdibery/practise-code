#IF STATEMENTS - conditional tests 
#If statement allows you to examine the current state of a program as it runs  
#and respond approriately to that state 
#This enables you to write for loops
#example - cars are supposed to be in title case 
# except bmw which is in all caps
cars = ["bmw","subaru","toyota","audi"]
for car in cars:#loop through every element in list
    if car == "bmw":
        print(car.upper())

newlist =[car.upper()for car in cars]
print (newlist)
#the expression can overwrite items in the list 
newrlist=["skibidi" for car in cars ]#changes all items in the list to skibidi
print(newrlist)
#basically set the values in the new list to upper case

#SYNTAX - name of list =[expression to be executed on items in the list(car.upper)loop for values you wanna feed into the expression]

#the expression is like a storage location.The expression is the current item in the iteration, 
# but it is also the outcome, which you can manipulate before it ends up like a list item in the new list
#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

#Example
#Return "orange" instead of "banana":
#newlist = [x if x != "banana" else "orange"(expression ends here) for x in fruits]
#syntax changes depending on the type of value btw

#CONDITONAL TESTS
#it is an expression that evaluates True or False in an if statement.
#python uses true or false to det if a program should be executed
#true  python executes False - python ignores

#examples of conditional operators (==),(!=),(value in list),(value not in list)

#CHECKING FOR EQUALITY
#Most conditional tests compare the current value of a
#variable to a specific value of interest
status = "rizz"#creating a variable to hold rizz
status == "rizz"#checks if the variable holds any rizz
#its basically shorted to be "rizz" = "rizz"
#This equality (==)operator returns True 
# if the values on the left and right side of the operator match,
# and False if they don’t match - in this case it returns true
# this operator is case sensitive 

#if case matters, especially if its user input convert to lower
status = "Sigma"
status.lower() =="sigma"#checks if the lowercase of input is equal to sigma
#.lower() doesnt change value of initial variable

#CHECKING FOR INEQUALITY 
#When you want to determine whether two values are not equal,
#you can use the inequality operator (!=)
giovanni = "no bitches"
if giovanni != "rizzmaster":
    print (f"this bro is bitch repelant."
           f" i love you tho gang")
#the code compares the reality of gio having no bitches 
# to the value rizz master.since the values dont match 
#it returns true and the print statement is executed
#these conditional tests apply to numbers too

#CHECKING MULTIPLE CONDITIONS AT THE SAME TIME
# key words and and or - if you want both or one condition true
age_1 = 20#define the two ages
age_2 =14
age_1 >= 18 and age_2 <= 14 #youre 20? no one has to know bbg
#both conditions have to be true for the operand to return true 

age_1 >= 18 or age_2 >= 21#true is returned
age_1 <= 14 or age_2 >= 21#false is returned

#checking for values in a list 
#The word in tells python to check for an item in list
brainrot =["sigma","mango","skibidi","ohio"]
"gyatt" in brainrot #returns false 
"sigma" in brainrot #returns true

#checking if value is not a list
#use key word NOT - use case - checking if some users are allowed to comment
Banned_Word=["niggas","incels","monkey"]
word ="cvnt"
if word not in Banned_Word:#
    print (f"{word} can be posted")

#booleen expressions- another name for conditional test
#a booleen value is either true or false
#booleen conditions are used to keep track of certain conditions
#eg, whether a game is running or a user can edit content on a website
game_active = True
can_edit = False

#IF STATEMENTS 
#simple if statements - tests one condition only
age = 19
if age >= 18: 
    print("you can vote now")
# All indented lines after an if statement will be
#executed if the test passes, and the entire block of indented
#lines will be ignored if the test does not pass.

#if-else- statements 
#else statement allows you to
#define an action or set of actions that are executed 
#when the conditional test fails.
#only needs the program to pass one test.
else:
    print("no too young")

#nested if 
do_you ="love me"    
#answer = input("do you like me?")
answer = "no"
if answer.lower() == "yes":
    print("yipee")
elif answer.lower() == "no":
    print("oh!umm sorry")
else:
    print("thats not what i asked")

#you dont always need am else block
#Python does not require an else block at the end 
# of an if-elif chain. Sometimes, an else block is useful
#example
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print (f"your admission cost is ${price}")
"""
ommiting the else block isn for precision
when you ommit the else statement, every block of code
must pass a specific test in order to be execute.
Therefore your code will only run under correct conditions
The else block is a catchall statement. It matches any
condition that wasnt matched by a specific if or elif tes
and that can sometimes include invalid or even malicious
data. 
"""
#testing multiple conditions - so the data has to pass all
#This technique makes sense when more than one condition
# could be True,and you want to act on every condition that is True.
requested_toppings =["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print("adding mushrooms")

if "pepperoni" not in requested_toppings:
    print("dont put pepperoni")

if "extra cheese" in requested_toppings:#checks list regardless of previous result
    print("adding extra cheese")

print("\nFinished making your pizza")
#almost forgot about python functions
def sigma():
    print("eren was right")

sigma()