# class Reference
class Reference:
    # constructor
    def __init__(self, title, publisher):
        # setting all the details
        self.title = title
        self.publisher = publisher
        self.published_year = 0 # setting published_year to 0 

    # getDetails method
    def getDetails(self):
        if self.published_year > 0:
            print(f"{self.title} ({self.published_year}) - {self.publisher}")
        else:
            print(f"{self.title} - {self.publisher}")

# Magazine class inherting from Reference class
class Magazine(Reference):
    # constructor
    def __init__(self, title, publisher):
        # calling super constructor with required arguments
        super().__init__(title, publisher)

# Video class inherting from Reference class
class Video(Reference):

    def __init__(self, title, publisher, published_year):
        # calling super constructor with required arguments
        super().__init__(title, publisher)
        # setting published_year to the given year
        self.published_year = published_year

# Book class inherting from Reference class
class Book(Reference):

    def __init__(self, title, publisher, author):
        # calling super constructor with required arguments
        super().__init__(title, publisher)
        # setting author to the given author
        self.author = author
    # getDetails() for Book class
    def getDetails(self):
        print(f"{self.title} by {self.author} published by {self.publisher}")

# AudioBook class inherting from Book class
class AudioBook(Book):

    def __init__(self, title, publisher, author, recording_minutes):
        # calling super constructor with required arguments
        super().__init__(title, publisher, author)
        # setting recording_minutes to the given recording_minutes
        self.recording_minutes = recording_minutes

    # getDetails() for AudioBook class
    def getDetails(self):
        print(f"{self.title} ({self.recording_minutes//60}:{self.recording_minutes%60}) by {self.author} published by {self.publisher}")

# get_catalog() method for getting initial values
def get_catalog():
    library = []  # creating an empty list
    # creating respective type objects with values and appending to list
    library.append(Video("Goonies", "Amblin Entertainment", 1985))
    library.append(Book("Favlehaven", "Shadow Mountain", "Brandon Mull"))
    library.append(AudioBook("Gulliver's Travells", "Shadow Mountain", "Jonathan Swift", 138))
    library.append(Book("Gulliver's Travells", "Dover Publications", "Jonathan Swift"))
    library.append(Magazine("Highlights March 1997", "Stenhouse Publishers"))
    library.append(Reference("ISJ May 14, 2019","Idaho State Journal"))
    # finally returning the list
    return library
