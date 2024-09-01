from threading import Thread

def displayname(name):
    print("Hey, ", name)

t1 = Thread(target=displayname, args=('Dharm',))
t1.start()
t1.join()
