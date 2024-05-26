import numpy as np 

arr_tp = np.array((1,3,4,5,6,70))
arr_tp2 = np.array(34) # 0-d
arr = np.array([1,3,4,5,6,7]) # 1-d
arr2 = np.array([[1,3,4,5,6], [23,13,25,8,9]]) # 2-d
#arr2 = np.array([[1, 2, 3], [4, 5, 6, 9]])
arr_3d = np.array([[[1,2,3,4,5],[7,8,9,10,11]],[[5,6,7,8,9],[10,11,12,13,20]]]) # 3-d

arr_ndim = np.array([1,2,3,4], ndmin=5)
'''
print(arr2[0,2])
print(arr2[1,2:4])
print(arr_tp)
print(type(arr))
print(arr_3d.ndim)
print(arr_3d[1,1,3])
print(arr_3d[-1,-1,-2])
print(arr_3d[1,0,1:4])
print(arr_ndim)
print(arr_ndim.ndim)
print(arr[1], arr[4])
'''
data_arr = np.array(['Anord', 'Alex', 'Mtegeki'])
data_copy = data_arr.copy()
data_view = data_arr.view()
data_arr[0] = "Anjelina"
data_view[2] = "Diana"
print(data_copy)
print(data_view)
print(data_copy)
print(arr_3d.shape)
print(data_view.base)
print(data_arr)
print(data_arr.dtype)

arr_shape = np.array([1,2,3,4,6,7,8,9])
arr_reshape = arr_shape.reshape(2,2,2)
newarr = arr_shape.reshape(2, 2, -1)
print(newarr)
print(arr_reshape)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
print(arr)

arr_loop = np.array([12,13,14,12,15,16])
for x in arr_loop:
    print(x)

for x in np.nditer(arr_loop):
    print(x)

arr_loop = np.array([[12,13,14],[12,15,16]])
for x in arr_loop:
    for y in x:
        print(y)

arr_loop = np.array([[[12,13,14],[71,80,12]],[[12,15,16],[23,45,88]]])
for x in np.nditer(arr_loop):
    print(x)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

arr1 = np.array([42,43,44,14,67,23])
firter_arr = arr1 > 42
newarr = arr1[firter_arr]
print(newarr)
print(firter_arr)