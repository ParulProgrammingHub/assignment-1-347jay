#Write python program to enter value in days and convert in form of years, months and days(assuming all months has 30 and year is of 360).
#1year = 360 days
#1month = 30 days

days=int(input("Enter The Days: "))
print(("%d Days Is: ")%days)
year = int(days/360)
days = days-(int(year*360))
month = int(days/30)
days = days-(int(month*30))

print(("%d Year")%year)
print(("%d Month")%month)
print(("%d Days")%days)
