a = []
b = []
for i in range(3, 99):
    if i % 3 == 0:
        a.append(i)
for j in range(5, 100):
    if j % 5 == 0:
        b.append(j)
print(set(a).intersection(set(b)))