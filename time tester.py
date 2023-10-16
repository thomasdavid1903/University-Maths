import time

start = time.time()

n = 1434324234

for i in range(1000):
    print(i)
    print("    " + str(n/(i+1)))
end = time.time()
print(end-start)