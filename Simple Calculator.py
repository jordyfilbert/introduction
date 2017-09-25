def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
print ("1.add")
print ("2.Subtract")
print ("3.Multiply")
print ("4.Divide")


selection=int(input("choose selection="))
num1=int(input("Number 1="))
num2=int(input("Number 2="))
if selection == 1:
    print (num1, "+",num2,"=",add(num1,num2))
    x=(num1+num2)
    print (num1, "-",num2,"-",subtract(num1,num2))
elif selection ==2:
    x=(num1-num2)
elif selection ==3:
    print (num1,"*",num2,"*",multiply(num1,num2))
    x=(num1*num2)
elif selection ==4:
    print (num1,"/",num2,"/",divide(num1,num2))
    x=(num1/num2)

if x > 50:
    print ("tinggi bgt bos")
else:
    print ("pendek bgt bos")