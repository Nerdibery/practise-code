#create a long list
games =['hollow night','blasphemous','rain world','ori and wisps','hello guest','hello neighbour','dead by daylight']
number = 0 #create a variable tso hold a negative index to access the list from last to first
for i in "bocha":#create a definate loop
    number -=1#increase index
    print(number)
    print(games[number])

#negative index is useful in accessing recent items in a long list

#exercises(wedding simulation)
num =0#
guest_list = ["tobias","constantine","garang","makeba"]
#for i in guest_list leads to errors. to prevent errors use len() and range() function
"""
HOW TO ITERATE IN A LIST
The range() function returns a sequence of numbers starting from 0 ending at the integer passed as a parameter.
 The len() function returns the length of the parameter passed.
 Using these two methods together allows for safe iteration over the list up to its final element
 This ensures that you stay within the valid index range and preventing the IndexError.
 EXAMPLE: for i in range(len(guest_list))
"""
for x in range(len(guest_list)):#for every item in the list do:
    print(f"Dear {guest_list[x].title()},you have been invited to my wedding on june 5")#dont put a number for the index
    #only insert the place holder x in index

#oh no you just heard some guests wont make it :( you have to remove em
busy_guest =guest_list.pop(3)
print(busy_guest,guest_list)
guest_list.insert(3,"gladys")
for i in range(len(guest_list)):#for every item in the list do:
    print(f"Dear {guest_list[i].title()},you have been invited to my wedding")#dont put a number for the index
    #only insert the place holder i in index

#ive found a bigger venue so i will add more guests
guest_list.append("michael")
#guest_list.extend(("June","Stacy"))#enables it to add more than one element at once but must be in brackets
guest_list.insert(0,"velma")#add to beginning of list
guest_list.insert(5,"fred") #add in the middle

print(len(guest_list),"people have been invited")

#more invitations
for i in range(len(guest_list)):#for every item in the list do:
    print(f"Dear {guest_list[i].title()},please come to my wedding")#dont put a number for the index
    #only insert the place holder i in index

#so the table is late only two people can show up
print("apparently i can only invite two people to dinner")
print(len(guest_list))
length =len(guest_list) - 2
print (length)

for y in range(length):
    uninvited = guest_list.pop()
    print(f"Dear {uninvited},you won't be attending the dinner.Toodles <3")

print(f"you are still invited {guest_list[0]}")
print(f"you are still invited {guest_list[1]}")

#make dat list emptyyyy
del guest_list[0]
del guest_list[0]
print (guest_list)

#sight seeing
places_to_visit =["netherlands","zanzibar","mozambique","bali","sweden","iceland","south africa","korea","japan"]#unsorted
print(places_to_visit)

print(sorted(places_to_visit))#doesnt alter original list
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort()#permanently alters
print(places_to_visit)

places_to_visit.sort(reverse=True)#by default reverse is off(false), typing it true turns decending order on
print(places_to_visit)
#you can sort elements based on length .syntax: listname.sort(key=len)

fav_pizzas = ["peperroni","chicken periperi","hawaian"]#defining the list
for pizza in fav_pizzas:#for every pizza in the list,the program prints the pizza
    print(pizza)
    print(f"I like {pizza}")
print(f"i really love pizza\n")

#LIST COMPREHENSIONS EXERCISE
#operation make code shorter >< - no need to append 
#syntax -listname = [expression,loop that feeds expression values] -no colon at end
#counting to twenty
count =[value for value in range(1,21)]#fyi the variable value cant be referenced outside the list
print(count)
#Make a list for numbers from 1-1 mil
One_Mil =[value for value in range(1,1000001)]
#print (One_Mil)
print(sum(One_Mil))
print(min(One_Mil))
print(max(One_Mil))

#odd numbers from 1-20
#only way is to use the step size function in ranges
odd_numbers =[odd_number for odd_number in range(1,20,2)]#NB both the expression and variable should be identical
print(odd_numbers)

#make a list of a multiple of 3's from 3-30
threes =[multiples for multiples in range(3,30,3)]
print(threes)

#cubes for the first 10 cubes
cubes =[number**3 for number in range(1,11)]
print(cubes)

#slices
friends_pizza = fav_pizzas[:]
friends_pizza.append("marshmello")
fav_pizzas.append("salmon")
print(fav_pizzas,friends_pizza)
print(f"my fave pizzas are{fav_pizzas[1:3]}")

#Tuple exercise
resturant_menu =("pasta","lobster","lasagna","porridge","meatloaf")
for item in resturant_menu:
    print(f"{item} is delicious")

#resturant_menu[0] = "peperroni"#error
resturant_menu =("pasta","shrimp","lasagna","salad","meatloaf")
for item in resturant_menu:
    print(f"{item} is delicious")

#additional notes (:
"""
Python styling conventions
1.indentation -4 spaces per indent and set tab key to space not insert tabs
2.Line length -less than 80 characters
3. Blank lines/spacing - to separate/group parts of the program - only affects readability

To edit the styling conventions you must write a PEP(python enhancement proposal)

"""