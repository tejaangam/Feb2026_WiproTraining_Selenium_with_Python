class A:
    def show(self):
        print("A")
class B(A):
    def show (self):
        super().show()
        print("B")
class C (A):
    def show(self):
        super().show()
        print("C")
class D (C, B):
    def show(self):
        pass
        print("D")

d = D()
d.show()
print(D.mro())

