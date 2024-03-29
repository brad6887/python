
class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)

a = CountFromBy()
b = CountFromBy()
c = CountFromBy()
d = CountFromBy(100)

c.increase()
print(a.val)
print(c)