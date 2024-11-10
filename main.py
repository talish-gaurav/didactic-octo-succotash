
mean1 = int(input("Enter the incorrect mean"))
num1 = int(input("Enter the incorrect number"))
num2 = int(input("Enter the correct number"))
tot = int(input("Enter your total of all the numbers"))

sum = mean1*tot
cor_tot = sum- num1 + num2
cor_mean= cor_tot//tot
print(cor_mean, "is the correct mean")
