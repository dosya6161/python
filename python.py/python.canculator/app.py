name1 = int(input("Enter num1: "))
name2 = int(input("Enter num2: "))
main = str(input("choose action: Add(+),Sub(-), Mult(*) Div(d) : "))

print("The result is ",end="")
if main == "+":
    print(name1+name2)
elif main == "-":
    print(name1-name2)
elif main == "*":
    print(name1*name2)    
else:
    print(name1/name2)