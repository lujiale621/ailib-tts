import numpy as np
from io import BytesIO

array = np.array([1, 2, 3])

npy = BytesIO()
np.save(npy,array)
npy.seek(0)
tmp = np.load("H:\git/vits-simple-api\Model/npy/25ecb3f6-f968-11ed-b094-e0d4e84af078.npy")
print(tmp)

