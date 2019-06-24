import ListUtilFunctions as W
import time


def merge(left, right):
    arr = []
    leftid, rightid = 0, 0
    while leftid < len(left) and rightid < len(right):
        if left[leftid] <= right[rightid]:
            arr.append(left[leftid])
            leftid += 1
        else:
            arr.append(right[rightid])
            rightid += 1
    if left:
        arr.extend(left[leftid:])
    if right:
        arr.extend(right[rightid:])
    return arr

def imperative_mergesort(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    left = imperative_mergesort(left)
    right = imperative_mergesort(right)
    return list(merge(left, right))

def Run_Test(str):
    print("Beginning of ")
    print(str)
    arr = W.LoadList(str)
    arr = arr[0]
    print("starting array")
    print(arr)
    start = time.time()
    arr = imperative_mergesort(arr)
    end = time.time()
    print("Time Taken: ")
    print(end - start)
    print(" Sorted Array:")
    print(arr)
    print("End of ")
    print(str)




Run_Test("Directory100.csv")
Run_Test("Directory200.csv")
Run_Test("Directory300.csv")
Run_Test("Directory400.csv")
Run_Test("Directory500.csv")
Run_Test("Directory600.csv")
Run_Test("Directory700.csv")
Run_Test("Directory800.csv")
Run_Test("Directory900.csv")
Run_Test("Directory1000.csv")
Run_Test("Directory1100.csv")
Run_Test("Directory1150.csv")
Run_Test("Directory1200.csv")
Run_Test("Directory1300.csv")
Run_Test("Directory1350.csv")
Run_Test("Directory1400.csv")
Run_Test("Directory1450.csv")
Run_Test("Directory1500.csv")
Run_Test("Directory1550.csv")
Run_Test("Directory1600.csv")
Run_Test("Directory1800.csv")
Run_Test("Directory2000.csv")
Run_Test("Directory2200.csv")
Run_Test("Directory2400.csv")
Run_Test("Directory2600.csv")
Run_Test("Directory2800.csv")
Run_Test("Directory3000.csv")
Run_Test("Directory3400.csv")
Run_Test("Directory10000.csv")



















