message = 'HOTTOGO, you can take me hot to go!'
print(message)#the variable stores its assigned value
print('message')#note these are not the same.the "message" is a string that isnt executable
#a variable self updates when changed
#Variable names can contain only letters, numbers, and underscores 


#english gramatical rules dont matter in variables. they just have to be consistent
#variables are labels that you can assign to values. You can also say that a variable references a certain value.
#types of variables

simp_Son = 3#camel Case
simp_son = 4#snake case
Simp_Son = 10# Pascal Case
"""
#python data types
1.strings - collection of characters,anything in "" or ''. or anything inputed by input()
string methods <3:
-changing case
"""
name ="nerdy beri"
print (name.title())#changes string to title case
print(name.upper())#changes to upper case
print(name.lower())#changes to lowercase
#this is mostly used when altering users input in sites to fit a certain format
#A method is an action that Python can perform on a piece of data.
#  The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.
#  Every method is followed by a set of parentheses, because methods often need additional information to do their work.
#  That information is provided inside the parentheses.
#  The title() function doesn’t need any additional information, so its parentheses are empty.

#using variables within a string(makes it simpler to enter data)
#f string type shii(f-format) enables use of variables within a string
print(f"my name is {name}\n"
      f"{message}")

#making output easier to read-by adding tabs,space and end of line charaters(these are simply refered to as whitespace)
print(f"i like chappel\n"
      f"i like melanie\n") #\n inserts a new line into sting

print("\tpython") #adds tab space before python
print("python")

print("\tpretty bitches code\n\ti am a pretty bitch\n")#they can be used in combination
#they reduce the lines of code to be written

#sometimes you have to eliminate whitespace in inputed data for the sake of comparison
#should be used when checking or search 
#to the computer "python" , "python " and "  python" is different 
# to permanently eliminate whitespace,you have to overwrite the original value
fruit = input("please enter fruit")
fruit = fruit.rstrip()#removes whitespace to the right of the string
fruit = fruit.lstrip()#removes whitespace to the left of the string

print(fruit)#fyi fruit.strip eliminates whitespace from bith sides
  
#removing prefixes/sufix - mostly used in browser displays
show ="game hallow knight game"
print(show.removeprefix("game"))
print(show.removesuffix("game"))

#random string errors(syntax errors are vague hence take a while to debbug)
#- avoid using single quote and apostrophe,python cant tell where the sting ends hence produces error

#2. numbers -Numbers are used quite often in programming to keep score in games,
#  represent data in visualizations, store information in web applications, and so on. 
#types of numbers - intergers,float
#integer = whole numbers# operations that can be carried out on integers minus(-),multi(*),add(+),div(/),exponential(**)and modulous(%)
#float - anything with a decimal point-default in results of calculation even in whole number

#instead of commas large numbers zeros are separated by underscores. they be ignored on printing
speed_of_sound =340_000
print(speed_of_sound)

#You can assign values to more than one variable using just a single line of code
x,y,z =12,15,"W rizz"
#You need to separate the variable names with commas, and do the same with the values. 
# As long as the number of values matches the number of variables, Python will match them up correctly.

#python doesnt really have built-in constants but when coding,constants are written in uppercase
GLIZZY ="mines big <3"


# a rant on comments
# its denoted by # ,''',"""
#  The main reason to write comments is to explain what your code is supposed to do and how you are making it work for later reference


