import numpy as np

rand_image=np.random.rand(24, 24, 3)

np.savez("sampleData.npz", rand_image)
