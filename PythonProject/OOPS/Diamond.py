class A:
    def show(self):
        print("A")
class B(A):
    def show (self):
        print("B")
class C (A):
    def show(self):
        print("C")
class D (C, B):
    pass
    print("D")

d = D()
d.show()
print(D.mro())

