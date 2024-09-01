from threading import Thread

def printName(name):
    print("Hey, ", name)

t1 = Thread(target=printName, args=('dharm',))
t1.start()
t1.join()