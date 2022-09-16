import numpy as np

# vec1 = np.array([[7.6, 2.3, 5.5], [3.4, 2.2, 9.8], [1.7, 5.2, 7.1]])
vec2 = np.array(
    [
        [0.000000e0, 1.125544e-4, 0.000000e0],
        [0.000000e0, 1.125544e-4, 0.000000e0],
        [0.000000e0, 0.000000e0, 0.000000e0],
        [0.000000e0, 0.000000e0, 0.000000e0],
        [4.791020e-4, 1.968889e-6, 3.929008e-4],
        [4.791020e-4, 1.968889e-6, 3.929008e-4],
    ]
)

print(np.sum(vec2.T, axis=0, keepdims=True))
# print(vec3 + 5)
