from threading import Thread

class MyThread:

    def __init__(self, str):
        self.str = str

    def display(self, x, y):
        print(self.str)
        print("Args: ", x, y)

o1 = MyThread('Hello')
t1 = Thread(target=o1.display, args=(1,2))

t1.start()
t1.join()