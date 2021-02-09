size=int(input("Enter size of stack:"))
top=0
stk=[]
n=1
def push():
    item=int(input("Enter item:"))
    global top


    if(top<size):
        stk.insert(top,item)
        top+=1
    else:
        print("Stack Overflow")

def pop():
    global top
    top-=1
    if top<0:
        print("stack is empty")
    else:
        print(stk[top],"popped out")
def display():
    for i in range(0,top):
        print(stk[i])
while(n!=0):
    option=int(input("Enter operation press\n 1)PUSH\n 2)POP\n 3)DISPLAY\n"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print("Invalid option")
    n=int(input("do you want to continue press 0 for exit"))