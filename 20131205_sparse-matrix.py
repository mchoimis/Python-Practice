"""

Calculate sparse matrix
http://stackoverflow.com/questions/17743870/calculate-similarity-of-sparse-matrix

c.f.
http://www.mathworks.com/help/matlab/math/sparse-matrix-operations.html
http://en.wikipedia.org/wiki/Sparse_matrix
http://www.mathworks.com/products/matlab/examples.html?file=/products/demos/shipping/matlab/airfoil.html

"""



from scipy.sparse import coo_matrix
import scipy
nrows = 100000
ncols = 100000
row = scipy.array([1,3,5,7,9])
col = scipy.array([2,4,6,8,10])
values = scipy.ones(col.size)
m = coo_matrix((values, (row,col)), shape=(nrows, ncols), dtype=float)
