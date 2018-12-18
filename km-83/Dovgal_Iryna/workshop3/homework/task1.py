def Recursion_Sum(element):
    if isinstance(element, list):
        summa = 0
        for item in element:
            summa = summa + Recursion_Sum(item)

        return summa
    else:
        return element
print(Recursion_Sum([2,[2,[3],[2,2]],4]))
