import math
h = []
for i in range(0,10000):
    h.append(i)

for i in h:
    if ( math.floor(math.floor(i/3)/2) != math.floor (i/6) ):
        print(i)


print("done")