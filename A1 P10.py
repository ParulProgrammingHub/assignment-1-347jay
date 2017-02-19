#Write python program to enter principal amount, time and interest rate. Create simple_interest(principle,time,rate) function to calculate simple interest.
def simple_interest(principal, time, rate):
    return (principal*time*rate)/100

principal=float(input("Enter The principal Amount: "))
time=float(input("Enter The Time: "))
rate=float(input("Enter The Interest: "))

interest=simple_interest(principal,time,rate)

print(("Simple Interest Is %d")%interest)

