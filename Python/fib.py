class Fib:
    def __init__(self, maxSize):
        self.size = maxSize
        self.fibArr = []
        self.fibArr.append(0)
        self.fibArr.append(1)

        for i in range(2, maxSize):
            self.fibArr.append(self.fibArr[i - 2] + self.fibArr[i - 1])

    def prepFib(self, n):
        for i in range(self.size, n + 1):
            self.fibArr.append(self.fibArr[i - 2] + self.fibArr[i - 1])

    def getFib(self, n):
        if n < self.size:
            return self.fibArr[n]
        else:
            self.prepFib(n)
            return self.fibArr[n]
