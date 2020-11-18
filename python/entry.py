from library import *   # importing all the classes and functions from library
import sys              # importing sys module for exit() function

# getting initial catalog using get_catalog() defined in library
catalog = get_catalog()

# function to add Book
def addBook():
    # getting details from user
    title = input("What is the title of the Book ? ")
    publisher = input("Who publised the Book ? ")
    author = input("Who wrote the Book? ")
    # creating Book object and appending to the catalog
    catalog.append(Book(title, publisher, author))

# function to add AudioBook
def addAudioBook():
    # getting details from user
    title = input("What is the title of the Book ? ")
    publisher = input("Who publised the Book ? ")
    author = input("Who wrote the Book? ")
    recording = int(input("How Long it the recording ? "))
    # creating AudioBook object and appending to catalog
    catalog.append(AudioBook(title, publisher, author, recording))

# function to add Magazine
def addMagazine():
    # getting details from user
    title = input("What is the title of the Book ? ")
    publisher = input("Who publised the Book ? ")
    # creating Magazine object and appending to catalog
    catalog.append(Magazine(title, publisher))

# function to add Video
def addVideo():
    # getting details from user
    title = input("What is the title of the Book ? ")
    publisher = input("Who publised the Book ? ")
    year = int(input("When was it published ? "))
    # creating Video object and appending to catalog
    catalog.append(Video(title, publisher, year))

# function to add OtherReference
def addOtherReference():
    # getting details from user
    title = input("What is the title of the Book ? ")
    publisher = input("Who publised the Book ? ")
    # creating OtherReference object and appending to catalog
    catalog.append(Refernce(title, publisher))

# function to show all the catalog
def show_catalog():
    print("\n--------- Library Catalog ---------")
    # iterating though catalog and calling getDetails()
    for x in catalog:
        x.getDetails()

# printing menu and all other things
# making infinite loop
while True:
    # printing menu
    print("What Would you like to do ?")
    print("\tAdd (b)ook")
    print("\tAdd (a)udio Book")
    print("\tAdd (m)agazine")
    print("\tAdd (v)ideo")
    print("\tAdd (o)ther Reference")
    print("\t(l)ist item in catalogue")
    print("\te(x)it")
    # taking user input
    choice = input().strip().lower()
    # using if elif calling resective functions
    if choice == 'b':
        addBook()
    elif choice == 'a':
        addAudioBook()
    elif choice == 'm':
        addMagazine()
    elif choice == 'v':
        addVideo()
    elif choice == 'o':
        addOtherReference()
    elif choice == 'l':
        show_catalog()
    elif choice == 'x':
        # if choice is 'x' the calling exit()
        print("Good bye !")
        sys.exit()
    else:
        print("Sorry ! I could not understand.")
    print("\n")
