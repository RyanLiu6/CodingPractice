fibArr = []


def prepareFib(n):
    for i in range(n):
        fibArr.append(-1)

    fibArr[0] = 1
    fibArr[1] = 1

    for i in range(n):
        if i == 0 or i == 1:
            continue
        fibArr[i] = fibArr[i - 1] + fibArr[i - 2]


def fib(n):
    return fibArr[n-1]