def sum_n(n):
    if n == 0:
        return 0
    return n+sum_n(n-1)

print(sum_n(3))


print("Довгаль Ірина\n КМ-83\nвариант 4")
print(" Функція - Parse(s,t). "
      "Призначення - поділ рядка s на дві частини: до першого входження символу t і після нього. \n\n")
a =input("введіть рядок")
b =input("введіть літеру")
def Parse(s, t):
    print(s[0:s.find(t)])
    print(s[s.find(t):])
    return "finish"

if b in a:
    Parse(a,b)
else:
    print("символу немає у рядку")


##
