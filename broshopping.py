books = []
prices= []
year_of_publication = []
total = 0

while True:
    book = input("enter a book to buy(q to quit)")
    if book.lower() == "q":#this function makes it lower case if capital is typed
        break
    else:
        price=float(input(f'input {book}price:ksh'))
        books.append(book)
        prices.append(price)
        year_of_publication=input("year of pub?")

print ("~~~~~~~YOUR CART~~~~~~~")
for book in books:
    print(book)


for price in prices:
    total +=price 

print ()
print (f"your total is {total}")
        


    