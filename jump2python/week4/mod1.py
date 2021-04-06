class FourCal:
    defaultvalue = 0
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        try:
            return self.first / self.second
        except ZeroDivisionError as e:
            print(f"ERROR: {e}")
            return 0
        
    def __str__(self):
        return f'first: {self.first}, second: {self.second}'
        
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second

class safeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


if __name__ == "__main__":
    a = FourCal(1,2)
    print(a.first)
    print(a.add())
    print(a.mul())
    print(a.sub())
    print(a.div())

    b = MoreFourCal(4,2)
    print(b.pow())

    c = FourCal(4,0)
    print(c.div())
    print(c.defaultvalue)