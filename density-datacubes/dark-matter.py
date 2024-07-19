import numpy as np
import pickle
import matplotlib.pyplot as plt
import h5py

path_to_file = "halos_short.bin"

with open(path_to_file, "rb") as f:
    halos = pickle.load(f, encoding='latin1')

#Notes on some halo properties:
# - ```'mvir'```: halo mass in solar masses
# - ```'rvir'```: halo radius in kiloparsecs
# - ```'x','y','z'```: position in Megaparsecs
# - ```'vx','vy','vz'```: velocity in kilometers/second

# print('The mass of the first halo can be accessed like this:\n')
# print(halos[0]['mvir'])
# print('\n')

# print('The masses of all halos can be accessed like this:\n')
# print(halos['mvir'])

#Visualize cosmic web of halos
plt.figure(figsize=(11,11))

plt.scatter(halos['x'],halos['y'],c='gray',s=0.5,alpha=0.3)

plt.axis('off')
plt.show()