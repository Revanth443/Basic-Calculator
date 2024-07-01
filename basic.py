a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=input("enter the operator")
if c=="+":
    d=a+b
    print(d)
elif c=="-":
    d=a-b
    print(d)
elif c=="*":
    d=a*b
    print(d)
elif c=="/":
    d=a/b
    print(d)
else:
    print("error")