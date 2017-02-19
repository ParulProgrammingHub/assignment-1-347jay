#Write python program to enter 2 angles and using function thirdangle(angle1,angle2) calculate third angle.

def calculate(a, b):
    return (180-a-b)

angle1=int(input("Enter A Angle: "))
angle2=int(input("Enter Another Angle: "))

angle3=calculate(angle1,angle2)
print(("Third Angle Is %d ")%angle3)
