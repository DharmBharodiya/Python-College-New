from threading import Thread
import time as t

def backgroundTask():
    while True:
        print("background task is running")
        t.sleep(2)

daemonThread = Thread(target=backgroundTask)

daemonThread.daemon = True #the .daemon takes and boolean to set the particular thread as a Daemon or not

daemonThread.start()

for i in range(3):
    print("Main thread is running.")
    t.sleep(2)

print("The main thread ends here, and eventually the daemon thread will be stopped automatically.")