a=float(input("enter first number: "))
b=float(input("enter second number: "))
op=input("enter an valid operator(+,-,/,%,**,//): ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="%":
    print(a%b)
elif op=="**":
    print(a**b)
elif op=="//":
    print(a//b)
else:
    print("Invalid operator")
