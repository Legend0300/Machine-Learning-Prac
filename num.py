import numpy as np
a = np.array([[[176  ,2567, 366] , [53, 64, 47]] , [[17  ,26 , 35] , [67 , 675 , 5676]]])

print(a[: , 0 , -1])


b = np.full((2 , 2) ,9 , dtype=int)
print(b)


new = np.full_like(a , 4)

print(new)


random_array = np.random.randint(7 , 100 , size=a.shape)
print(random_array)


np.identity(2)

#repeat an array:
initial = np.array([[1,2,3]])
repeat = np.repeat(initial , 3 , axis=0)
print(repeat)


#prac

solution = np.ones((5,5) , dtype=int)
solution[1:4 , 1: 4].fill(0)
solution[2 , 2] = 9


sol2 = solution.copy()
print(sol2)

np.sin(sol2)


c = np.identity(3)
np.linalg.det(c)

print(int(np.linalg.det(c)))





