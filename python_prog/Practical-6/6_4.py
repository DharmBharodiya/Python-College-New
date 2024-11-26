# Create a base class A with 2 children B and C. class D having 2 parents B and C. Create a
# method named “Call” in every class. Use super in a way that a single call to method of class
# D execute “Call” method of every class.

class A:
    def call(self):
        print("A class method is called.")

class B(A):
    def call(self):
        super().call()
        print("B class method is called.")


class C(A):
    def call(self):
        super().call()
        print("C class method is called.")

class D(B,C):
    def call(self):
        super().call()
        print("D class method is called.")

d1 = D()
d1.call()