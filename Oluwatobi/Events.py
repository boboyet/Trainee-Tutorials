import threading

event = threading.Event()

def myfunction():
    print("Waiting for event to trigger...\n")
    event.wait()
    print("Peforming....")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want event to trigger..(y/n)\n")
if x == "y":
    event.set()
