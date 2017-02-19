#Write python program to enter principal amount, time and interest rate. Create compound_interest(principle,time,rate) function to calculate compound interest.
def compound_interest(principal, time, rate):
    return (principal*(1+rate/(100*12))**(12*time))-principal

principal=float(input("Enter The principal Amount: "))
time=float(input("Enter The Time: "))
rate=float(input("Enter The Interest: "))

interest=compound_interest(principal,time,rate)

print(("Compound Interest Is %d")%interest)


