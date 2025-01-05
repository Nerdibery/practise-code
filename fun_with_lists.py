#author - Nerdybochaberi
#disclaimer, notes and exercises are derived from python crash course by Eric Matthes 

#application is matrix keypad, randomised gambling game

#A list is a collection of items in a particular order.
#  You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or words
#because lists contain more than one thing, its good to name the list a plural noun like books,cups etc
#In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas

girls =["mary","jane","makeba","janet","bessy"]#the index of the elements starts from zero[0,1,2]
boys =[]#empty list,you can add elements

print(girls)#prints the entire list

#accessing INDIVIDUAL ELEMENTS in lists- its using index
#method 1 - using element index
print(girls[0])#prints the first name in the list. syntax is listname[index/position]
#You can also use the string methods on any element in this list.(.title,upper,lower,strip)
print(girls[1].upper())

index_pos = "position - 1"
#you can access the last item on the list by listname[-1]. [-2]-second last,[3]-third last etc
print(girls[-1])

#using elements in a list -You can use individual values from a list just as you would any other variable
#eg f string
print(f"i love {girls[-1].upper()},she is my bestie")

#altering lists -Most lists you create will be dynamic.
#  meaning you’ll build a list and then add and remove elements from it as your program runs its course.
#an example is a game. when an enemy is shot down, remove an element. Similarly when an enemy appers add element

#to modify an existing element, the following syntax is used: listname[index] = new
girls[0] = "sheila"
print(girls)

'''
You might want to add a new element to a list for many reasons:
 For example, you might want to make new enemies appear in a game,
 add new data to a visualization, or add new users to a website you’ve built.
 Python provides several ways to add new data to existing lists.
'''
#method 1 - append -When you append an item to a list, the new element is added to the end of the list
girls.append("maria")
print(girls[-1])

# you can start with an empty list and then add items to the list using a series of append() calls
boys.append('garang')
boys.append('melvin')
boys.append("max")
boys.append("hesse")
print(boys)

#You can add a new element at any position in your list by using the insert() method.
#syntax is listname.insert(index,'element')
boys.insert(0,"billy")
print(boys)
#This operation shifts every other value in the list one position to the right.

#Often, you’ll want to remove an item or a set of items from a list.
# You can remove an item according to its position in the list or according to its value
#method one - using del statement
#If you know the position of the item you want to remove from a list, you can use the del statement
del boys[0]
print(boys[0].upper())
# you can no longer access the value that was removed from the list after the del statement is used

'''
Sometimes you’ll want to use the value of an item after you remove it from a list.
 For example, you might want to get the x and y position of an enemy that was just killed, so you can draw an explosion at that position.
 The pop() method removes the last item in a list, but it lets you work with that item after removing it.

'''
gone =[]
deleted_boys =boys.pop()#this created variable holds removed elements. you can also append it to another list containing deleted stuff
print(deleted_boys)
gone.append(deleted_boys)#like so. so its important to create a variable when using this method
print(gone)

#You can use pop() to remove an item from any position in a list. 
# This is by including the index of the item you want to remove in parentheses
# when you want to delete an item from a list and not use that item in any way, use the del statement;
#  if you want to use an item as you remove it, use the pop() method.
#syntax :listname.pop(index)
gone_girls =girls.pop(1)
print(gone_girls)

# If you only know the value/name of the item you want to remove, you can use the remove() method
#You can also use the remove() method to work with a value that’s being removed from a list(by creating a variable girl)
traitor ="janet"
girls.remove(traitor)
print(girls,traitor)
#The value 'janet' has been removed from the list but is still accessible through the variable traitor

"""
NOTE;The remove() method deletes only the first occurrence of the value you specify.
 If theres a possibility the value appears more than once in the list,
   youll need to use a loop to make sure all occurrences of the value are removed. 

"""
#organising lists<3
#Often, your lists will be created in an unpredictable order, 
#because you can’t always control the order in which your users provide their data.
#Sometimes you’ll want to preserve the original order of your list.
#other times you’ll want to change the original order
#The sort() method changes the order of the list permanently according to alphabetical order
girls.sort()
print(girls)

#The sorted() function lets you display your list in a particular order,
#but doesn’t affect the actual order of the list.
print(f"here is the original list {boys}")

print(f"here is the new list")
print(sorted(boys))
print(f"here is the original list {boys}")

#To reverse the original order of a list, you can use the reverse() method
#Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:
#The reverse() method changes the order of a list permanently, 
# but you can revert to the original order anytime by applying reverse() to the same list a second time.
girls.reverse()
print (girls)

#You can quickly find the length of a list by using the len() function.
#  The function counts from one unlike indexing
print(len(girls))
"""
You’ll find len() useful when you need to identify the number of enemies that still need to be shot down in a game,
 determine the amount of data you have to manage in a visualization, 
 or figure out the number of registered users on a website, among other tasks
"""
#you can sort elements based on length .syntax: listname.sort(key=len)


#You’ll often want to run through all entries in a list, performing the same task with each item
# For example, in a game you might want to move every element on the screen by the same amount.
# When you want to do the same action with every item in a list, you can use Python’s for loop

musicians = ["laufey","melanie","olivia"]#define a list
for i in musicians:#loops for every element (represented by i) in the list
    print(i)#i is a placeholder/variable for an element -tho its better to use a meaningful variable
#ngl this is a simpler method than what i was using

#types of errors
#1. syntax - indentation,incorrect spelling, wrong use of words
#logical - program runs but doesnt deliver expected resulsts

#Some errors are much harder to resolve, even when the eventual fix only involves a single character.
#Don’t feel bad when a small fix takes a long time to find; you are absolutely not alone in this experience.


#Lists are ideal for storing sets of numbers(game scores,data)
#tools for using lists
#1 range function
#Python’s range() function makes it easy to generate a series of numbers

for value in range(1,5):#range term is specifically for numerical values
    print(value)#python only prints 1-4 due to its off by one behaviour
    #python terminates before the second number in the range function 
#therefore to print 1-5 the function is range(1,6)

#You can also pass range() only one argument, and it will start the sequence of numbers at 0.
for value in range(6):
    print (value)

#We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to 
# range(), Python uses that value as a step size when generating numbers.
for i in (range(2,11,2)):#2 is the step size - this prints even numbers from 1-10
    print (i)
for value in range(3,13,3):#3 is the step size and this prints multiples of 3
    print(value)

#making a list of squares
squares =[] #make an empty list
for value in range(2,11):#from 2-10
    #can just do squares.append(value**2) to ommit the last 2 steps
    value = value**2 #square each number from 2-10 and overwrite the original value
    squares.append(value)#add each square value to the list
print(squares)#after the loop is done running it prints the list

#SIMPLE STATISTICS WITH LISTS <3
#you can use functions to find min max in lists
digits = []
for value in range(1,11):
    digits.append(value)
print(min(digits))#prints the smallest digit in the list
print(max(digits))#prints the largest digit in the list
#sort can be used to perform median no?
print(sum(digits))#outputs the sum of the digits in the list
#works for lists of all sizes

#list comprehensions (compresses code to be shorter(:))
#components of list comprehensions(for loop)
#sample, the squares list but SHORTER
squares =[value**2 for value in range(1,11)]
print(squares)
#SYNTAX - name of list =[expression of values to be stored in list(value**2)loop for values you wanna feed into the expression]
#this is basically assigning the current value in the for loop to the list
#NB_ NO COLON IS USED AT THE END OF THE FOR STATEMENT


#WORKING WITH PART OF A LIST -index always

#slice - specific group of items in a list SYMBOL - listname[:]
#To make a slice, you specify the index of the first and last elements you want to work with
#Python stops one item before the second index you specify

#Example
players =["sam","melissa","samba","kuromi","kitty"]
print(players[0:3])#0:3 is 0-3 and only prints 3 indexes
print(players[1:4])
print(players[:4])#same as printing from 0-4. Starts from the first index
print(players[2:])#prints from index two to the last item
print(players[-3:])#prints the last 3 things on the list

# : is good for long lists
#if you want a step number,just put 3 variables
print(players[0:4:2])#skips numbers by 2

#looping through a slice
#You can use a slice in a for loop if you want to loop through a subset of the elements in a list

for player in players[:3]:
    print (player)

#uses of slices -when you’re creating a game, you could add a
#player’s final score to a list every time that player finishes
#playing. You could then get a player’s top three scores by
#sorting the list in decreasing order and taking a slice that
#includes just the first three scores

#copying a list*****
"""
 making an entirely new list based on the first list.
 To copy a list, you can make a slice that includes the
entire original list by omitting the first index and the second
index ([:]). This tells Python to make a slice that starts at
the first item and ends with the last item, producing a copy
of the entire list.
"""
thislist = ["apple", "banana", "cherry"]
my_list =thislist[:]#slice operator method
my_list.append("candy")
thislist.append("jello")
print(thislist,my_list)

#functions method
thelist = ["meth", "weed", "juice","coke"]
mylist = thelist.copy()
print(mylist)

thylist = ["app", "ban", "che"]
MyList = list(thylist)
print(MyList)

#TUPLES
#difference btwn a tuple and a list?
#lists store data that changes/modified during program excecution 
#lists use []
#Tuples contain data that stays constant/immutable 
# - cant be changed but can be overwritten
#Tuples use ()

#Once you define a tuple, you can access individual elements 
# by using each item’s index, just as you would for a list
#use cases: the size of a rectangle
dimentions =(200,50)#example of a tuple
print(dimentions[0])#acessing an element
print(dimentions[1])
#dimentions[0]=250 #returns error coz tuples cant be changed

"""
Tuples are technically defined by the presence of a
comma; the parentheses make them look neater and
more readable. If you want to define a tuple with one
element, you need to include a trailing comma:
 my_t = (3,)
It doesnt often make sense to build a tuple with one
element, but this can happen when tuples are
generated automatically.

"""
#looping through values in a tuple
for value in dimentions:
    print (value) 

#writing over a tuple, since we cant add,remove or change existing data
for value in dimentions:
    print(f"original dimention {value}")

dimentions =(100,2000)
for value in dimentions:
    print(f"new dimention {value}")

#NB:tuples are simpler data structures than list
