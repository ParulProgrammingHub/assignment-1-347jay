#Write python program to enter radius of circle and calculate area and circumference of circle.
import math
radius=float(input("Enter The Radius: "))
area=math.pi *(radius**2)
circumference=2*math.pi*radius
print("Area Is: %d" %area)
print("Circumference Is: %d" %circumference)
