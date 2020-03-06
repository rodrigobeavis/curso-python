import time

for c in range(1, 500, 1):
    if(c % 3 == 0):
        print(c)
        time.sleep(0.2)
print('OK')