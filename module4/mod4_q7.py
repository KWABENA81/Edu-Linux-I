from array import array

import numpy as np
from numpy import nan

nan_data = np.empty((3, 5))
nan_data[:] = np.NaN
print(nan_data)


narr = array([nan,1.,2.,nan,3.,4.,5.])