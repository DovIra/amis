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