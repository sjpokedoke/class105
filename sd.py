import csv
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]

#find mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

#squaring and getting the values
squaredlist = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    squaredlist.append(a)

#getting sum
sum = 0
for i in squaredlist:
    sum = sum+i

#divide by n-1
result = sum/(len(data)-1)

#getting the standard deviation
sd = math.sqrt(result)
print("Standard deviation is: " + str(sd))