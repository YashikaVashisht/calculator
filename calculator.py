print("WELCOME TO YASHIKA's CALCULATOR")
def start(a):
    total=0
    while(True):

        o = input("enter the operator:")
        b = int(input("enter the number:"))
        if(o=='+'):
            add(a,b)
        elif(o=='-'):
            sub(a,b)
        elif (o == '*'):
            mul(a,b)
        elif (o == '/'):
            div(a,b)
        else:
            break
def add(a,b):
    total=a+b
    a=total
    print(total)
    #return a
    start(a)
def sub(a,b):
    total=a-b
    a=total
    print(total)
    #return a
    start(a)
def mul(a,b):
    total=a*b
    a=total
    print(total)
    #return a
    start(a)
def div(a,b):
    total=a/b
    a=total
    print(total)
    #return a
    start(a)

a = int(input("enter the number:"))
start(a)
