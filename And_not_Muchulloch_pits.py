import numpy as np

weights = np.array([], dtype=float)
for i in range(1,3):
    x = float(input(f"Enter Weight W{i} "))
    weights = np.append(weights, x)

threshold = float(input("Enter Threshold value between 0 and 1 : "))

x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))
# print(x1, x2)

weighted_sum = np.dot(weights, [x1,x2])
if weighted_sum >= threshold:
    print(1)
else:
    print(0)






