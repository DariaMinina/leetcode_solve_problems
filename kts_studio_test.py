# Есть 2 отсортированных массива. Требуется объединить их в один.
# Вход:
a = [-1, 0, 5, 7]
b = [2, 8]
# Результат:
# [-1, 0, 2, 5, 7, 8]

res = []
i = 0
j = 0

while len(res) != len(a) + len(b) and (i <= len(a) - 1 or j <= len(b) - 1):
    if a[i] > b[j]:
        res.append(b[j])
        j += 1
    else:
        res.append(a[i])
        i += 1

if i > len(a) - 1:
    res.append(b[j:])
else:
    res.append(a[i:])
