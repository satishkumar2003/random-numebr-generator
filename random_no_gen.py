from datetime import *
import time
print("This program is able to print a random number in the range (0 to 999) both inclusive")
n = int(input("Enter the number of random integers you want: "))
limit = int(input("Do you want to keep a higher limit (if not enter -1): "))
if limit==-1:
    for i in range(n):
        random = int(str(datetime.now())[-1:-4:-1])
        print(random)
        time.sleep(0.0001)
else:
    for i in range(n):
        random = int(str(datetime.now())[-1:-4:-1])
        while random > limit:
            random = int(str(datetime.now())[-1:-4:-1])
        print(random)