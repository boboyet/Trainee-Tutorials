#import threading

#def function1():
    #for x in range (100):
        #print("OnE!")

#def function2():
    #for x in range (1000):
        #print("TwO!")
   
#t1 = threading.Thread(target=function1)

#t2 = threading.Thread(target=function2)

#t1.start()
#t2.start()


import threading

def function1():
    for x in range (50):
        print ("Hello World")

t1 = threading.Thread(target=function1)
t1.start()

t1.join()

print("Another Transaction")

