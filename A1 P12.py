#Write python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=int(input("Enter The Number: "))

sum = n + (n*n) + (n*n*n)
print(("n+nn+nnn Is %d")%sum)
