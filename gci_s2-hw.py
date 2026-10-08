import numpy as np

def homework(a):
    # Write your answer here
    result = []
    for x in a:
        if x % 5 == 0 and x % 2 == 1:
            result.append(x)
    my_result = np.array(result)
    return my_result

a = np.array([1, 5, 10, 3, 4, 25, 30])
print(homework(a))
