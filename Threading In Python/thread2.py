from collections.abc import Callable
from threading import Thread
from typing import Any, Iterable, Mapping

class MyThread(Thread):

    def __init__(self, name):
        # when creating a subclass of the Thread class, inside the constructor the Thread class constructor is to be called compulsarily with the `self` as it argument
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(1,6):
            print(i, self.name)

t1 = MyThread('Dhrm')
t1.start()