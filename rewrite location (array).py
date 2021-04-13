z = 1
i = 0
j = 0
x, y = (5, 5)
CourtArray = [[],[],[],[],[]]
for i in range(y):
    for j in range(x):
        j = j + 1
        CourtArray[i].append(z)
        z = z + 1
    i = i + 1

for i in CourtArray:
    print(i)
    print(CourtArray[1][3])

#CourtArray[0][0]