import sys
import numpy as np

# print(str(sys.argv[1]))
# print(str(sys.argv[1]).split('.')[0]+'.csv')

my_data = np.genfromtxt(str(sys.argv[1]), delimiter=',')
np.save(str(sys.argv[1]).split('.')[0]+'.npy', my_data)




