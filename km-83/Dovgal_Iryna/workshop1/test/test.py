print("Користувач вводить два цілих числа, які визначають діапазон значень."
"Підрахувати кількість непарних чисел у цьому діапазоні.")

list = []
n = int(input())
m = int(input())
count = 0
for i in range(n, m):
    if i % 2 != 0:
        count = 1 + count
        list.append(i)
print(list)
print(count)

def recurse(mass):
    if len(mass) == 0:
        return None
    if len(mass) % 3 == 0:
        print(mass[1])

    return recurse(mass[1:])


print(recurse([1, 2, 3, 6, 5, 3, 6, 9, 9, 0, 0, 8, 7, 8, 9]))
