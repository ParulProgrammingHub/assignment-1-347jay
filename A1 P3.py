#Write python program to enter value in centimetre and convert it to meter and kilometre.
cm=int(input("Enter The Length In Centimeter: "))
m=float(cm/100)
km=m/1000
print("Length In Meter Is: %f" %m)
print("Length In Kilometer Is: %f" %km)
