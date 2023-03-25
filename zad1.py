list = [int(i) for i in input("Podaj liczby ").split(",")]
print(list)
max = list[0]
min = list[0]
for i in list:
    if max < i:
        max = i
    if min > i:
        min = i
print(min)
print(max)