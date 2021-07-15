
import numpy as np
if __name__ == "__main__":
    dtypes = [('name', np.unicode_, 16),('num',int)]
    values = [('Hrithik', 9), ('Arun', 2),
              ('Pankaj', 8), ('Aakash', 6),
              ('Helo', 91), ('Its', 212),
              ('Me', 832), ('Jayhawk', 645)]
    arr = np.array(values, dtype=dtypes)
    sorteddict = {a : b for a,b in  np.sort(arr, order=['name', 'num'])}
    print("\nArray sorted by names and then nums:\n",
         sorteddict)
