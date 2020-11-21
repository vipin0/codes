class Circle:
    """
    class Circle
    """
    def __init__(self,_r,_h,_k):
        """
        constructor
        Parameters:
        _r : radius of the Circle
        _h : x coordinate of the center of Circle
        _k : y coordinate of the center of Circle
        """
        self._rad = _r
        self._h = _h;
        self._k = _k
    
    def inSide(self,xC,yC):
        """
        To check the given point is inside the circle of not
        Parameters:
            xC : x coordinate 
            yC : y coordinate 
        Returns:
            if point is inSide then returns True, otherwise False
        """

        # Calculating distance of point from the center of the circle
        d = ((self._h - xC)**2 + (self._k - yC)**2)**.5
        
        # if distance is less than the radius then return true
        if d<self._rad:
            return True
        # otherwise return False
        else:
            return False

    # overriding __str__ method to print the circle in expected form
    def __str__(self):
        return(f"(x - {self._h})^2 + (y - {self._k})^2 = {self._rad**2}")

# creating the circle object
my_circ = Circle(3,4,2)
# getting x and y coordinate from user
myX = float(input("Enter an x-coordinate: "))
myY = float(input("Enter an y-coordinate: "))

# calling isSide method using myX and myY as arguments 
is_inside = my_circ.inSide(myX,myY)

# if is_inside is True printing Inside! to console
if is_inside:
    print("Inside!")
# otherwise printing Not Inside 
else:
    print("Not Inside!")

# creating Circle object
my_circ = Circle(5,3,2)
# printing circle object
print(my_circ)
