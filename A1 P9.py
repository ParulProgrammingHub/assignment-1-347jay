#Write python program to enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. If percentage is less than 35 print fail else print pass.
total=0
for i in range (5):
    mark = int(input("Enter The Marks of A Subject (out Of 100): "))
    total = total + mark
avg = total/5
print(("Average Marks Is %d")%avg)
percentage = (total/500) * 100

if percentage<35:
    print("Fail")
else:
    print("Pass")
