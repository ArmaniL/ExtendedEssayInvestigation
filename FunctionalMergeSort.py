import time
import ListUtilFunctions as W

def merge(left, right):
    if len(left) == 0:
        return right
    elif len(right) == 0:
        return left
    elif left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def functional_mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        h = len(arr) // 2
        return merge(functional_mergesort(arr[:h]), functional_mergesort(arr[h:]))

def Run_Test(str):
    print("Beginning of ")
    print(str)
    arr=W.LoadList(str)
    arr=arr[0]
    print("starting array")
    print(arr)
    start=time.time()
    arr=functional_mergesort(arr)
    end=time.time()
    print("Time Taken: ")
    print(end-start)
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
