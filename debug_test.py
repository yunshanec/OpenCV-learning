class Hannnoi(object):
    def __init__(self):
        super().__init__()

    def hannoi(self, n, a, b, c):
        if n == 1:
            print(a, "--->", c)
        else:
            self.hannoi(n - 1, a, c, b)
            self.hannoi(1, a, b, c)
            self.hannoi(n - 1, b, a, c)


if __name__ == "__main__":
    h = Hannnoi()
    h.hannoi(3, "A", "B", "C")
