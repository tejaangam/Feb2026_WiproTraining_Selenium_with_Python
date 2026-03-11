# operator polymorphism means -- the same operator behaves differently for diff data types or the objects


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    def __sub__(self, other):
        return self.value - other.value
    def __mul__(self, other):
        return self.value * other.value
    def __truediv__(self, other):
        return self.value / other.value
    def __floordiv__(self, other):
        return self.value // other.value
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value

n1 = Number(10)
n2 = Number(5)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 == n2)
print(n1 < n2)
print(n1 > n2)
