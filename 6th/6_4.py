class A:
    def call(self):
        print("Inside the class A.")

class B(A):
    def call(self):
        super().call()
        print("Inside the class B.")

class C(A):
    def call(self):
        super().call()
        print("Inside the class C.")

class D(B, C):
    def call(self):
        super().call()
        print("Inside the class D.")

d1 = D()#braces are very necessary
d1.call()