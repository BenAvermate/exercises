import time
t0 = time.time()
for i in range(1,100001):
    print(i)
t1 = time.time()
total1 = t1-t0

t0 = time.time()
for i in range(0,10000):
    print(i+1)
t1 = time.time()
total2 = t1-t0

print("1: " + str(total1))
print("2: " + str(total2))