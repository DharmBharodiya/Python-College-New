from threading import Thread
import time

class NewThread(Thread):

    def run(self):
        print("The thread is started.")
        time.sleep(2)
        print("The thread is stopped.")

class NewThread2(Thread):

    def run(self):
        print("The daemon thread is started.")
        print("The daemon thread is ending.")
# t2 = NewThread2()
# t2.setDaemon()
t1 = NewThread()
t1.start()
print(f"{t1.ident}")
t1.join()




