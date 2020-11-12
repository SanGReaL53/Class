class Balance:

    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, amount):
        self.right += amount

    def add_left(self, amount):
        self.left += amount

    def result(self):
        if self.left == self.right:
            print('=')
        elif self.left > self.right:
            print('L')
        else:
            print('R')
