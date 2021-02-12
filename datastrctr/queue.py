size=int(input("Enter size of queue:"))
frnt=-1
rear=-1
que=[]
n=1
def q_insert():
    global rear
    global frnt
    if (rear>=(size-1)):
        print("Queue is Full")
    elif frnt==-1:
        frnt=0
    elif rear<size:
        item =int(input("Enter item:"))
        que.insert(rear,item)
        rear += 1
    else:
        pass


def q_delete():
    global rear
    global frnt
    if ((frnt==rear)|(frnt>rear)):
        print("Queue is empty")
    else:
        rear-=1
        print(que[frnt],"popped out")
        frnt+=1

def display():

        for i in range(frnt,rear):
            print(que[i])

while(n!=0):
    option=int(input("Enter operation press\n 1)INSERT\n 2)DELETE\n 3)DISPLAY\n"))
    if option==1:
        q_insert()
    elif option==2:
        q_delete()
    elif option==3:
        display()
    else:
        print("Invalid option")
    n=int(input("do you want to continue press 0 for exit"))