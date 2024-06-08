import numpy as np
x_1d = np.array([1, 2, 3])
x_2d = np.array([[1, 2, 3], [12, 23, 14]])
x_3d = np.array([[[12, 13, 14], [14, 15, 16]], [[17, 18, 19], [12, 11, 22]]])
x_4d = np.array([[[[12, 13, 14], [14, 15, 16]], [[45, 42, 43], [47, 48, 49]]],
                 [[[14, 12, 13], [15, 16, 17]], [[23, 22, 45], [12, 45, 87]]]])
met_x = np.array([[1, 2], [3, 4], [5, 6]])
met_y = met_x + 2
hadmard_p = met_x + met_y
print(met_y)
print(hadmard_p)
m_1 = np.array([[25, 10], [-2, 1]])
m_2 = np.array([[-1, 7], [10, 8]])
hadamard_p = m_1 * m_2
print(f"hadamard : {hadamard_p}")
x = np.array([[42, 4, 7, 99], [-99, -3, 17, 22]])
w = np.array([-1, 2, -2])
w2 = np.array([5, 10, 0])
hadmard_2 = w + w2
print("jibu ni ", hadmard_2)
y_a = np.dot(w, w2)
print(y_a)
print(x.T)
print(x_1d.shape)
print(x_4d.ndim)
print(x_4d)
print(x_4d.shape)
