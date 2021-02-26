import threading
import time
def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thread executing")
    print(threading.currentThread().getName())
t=threading.Thread(target=display)
t.start()
begintime=time.time()
print("Begin Time=",begintime)
t.join()
for i in range(1,10):
    time.sleep(2)
    print("main thread is executing")
print(threading.currentThread().getName())
endtime=time.time()
tot_time=endtime-begintime
print("End Time=",endtime)
print("Total time=",tot_time)
#fast context switching is happening