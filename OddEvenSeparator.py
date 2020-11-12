class OddEvenSeparator:
    def __init__(self):
        self._odd = []
        self._even = []

    def add_number(self, num):
        if num % 2 == 1:
            self._odd.append(num)
        else:
            self._even.append(num)

    def even(self):
        print(self._even)

    def odd(self):
        print(self._odd)

o = OddEvenSeparator()
o.add_number(4)
o.add_number(1)
o.add_number(2)
o.even()
o.odd()
