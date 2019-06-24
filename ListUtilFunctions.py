import random as ran
import csv



def IsinList(arr, x):
    for i in arr:
        if i == x:
            return True
    return False


def random(l, h):
    return ran.randint(l, h)


def createRandomList(n, h):
    arr = []
    for i in range(1, n):
        r = random(0, h)
        if not IsinList(arr, r):
            arr.append(r)
    return arr


def LoadList(str):
    with open(str, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def savelist(arr, file):
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow(arr)


def CreateNewFile(str, Highest, amount):
    with open(str, 'w') as file:
        savelist(createRandomList(amount, Highest), file)
    file.close()