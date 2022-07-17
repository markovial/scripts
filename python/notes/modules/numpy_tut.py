import numpy as np

A = np.arange(0,10,2);          # Generate Sequence (start,stop,step)
A = np.linspace(0,2,5);         # Generate Sequence (start,stop,num_elem)
A = np.zeros((3,3));            # Generate zeroes (rows,cols)
A = np.ones((3,3));             # Generate ones (rows,cols)
A = np.random.rand(3);          # DO NOT USE , nx1 matrix is better , cause bugs
A = np.random.rand(3,3);        # Generate random floats (rows,cols)
A = A.astype(np.float16);       # Force type of array
A = np.array([1, 2, 3, 4])      # 1-Dim Array
A = np.array([[1, 2], [3, 4]])  # 2-Dim Array
A = np.ndarray(shape=(2,2))     # N-Dim Array (shape=tuple,buffer=init_vals)
A = np.array([[1, 2], [3, 4]]); #
B = np.ones(( 2,2 ))*10;        #

A.ndim        # Num of rows , int
A.shape       # Num of rows and cols , tuple
A.dtype       # type of elements
A.sum()       # Sum of all elements
A.max()       # Max of all elements
A.min()       # Min of all elements
A.mean()      # Mean of all elements
np.nanmean(A) # Mean and ignore NaN values

# print(f"ndim  : { A.ndim   } " )
# print(f"shape : { A.shape  } " )
# print(f"dtype : { A.dtype  } " )
# print(f"sum   : { A.sum()  } " )
# print(f"max   : { A.max()  } " )
# print(f"min   : { A.min()  } " )
# print(f"mean  : { A.mean() } " )

# A[row_start:row_end , col_start:col_end]

C = A + B;                 # print (C) # Element wise sum
C = A - B;                 # print (C) # Element wise subtract
C = A * B;                 # print (C) # Element wise multiply
C = A / B;                 # print (C) # Element wise divide
C = A @ B;                 # print (C) # Matrix Product = Dot Product
C = A.T;                   # print (C) # Matrix Transpose
C = np.linalg.inv(A);      # print (C) # Matrix Inverse
C = A % 2 == 0;            # print (C) # boolean array , elementwise truthness

C = np.exp(A);  # print (C) # Elementwise Exponentiatal
C = np.log(A);  # print (C) # Elementwise Ln
C = np.tanh(A); # print (C) # Elementwise Hyperbolic Tangent

C = np.array(C,dtype=int); # print (C) # binary array , elementwise truthness
C = A[:2];                 # print (C) # rows 0 to 2 (excluding 2)
C = A[1:2];                # print (C) # rows 1 to 2
C = A[1:];                 # print (C) # rows 1 to end
C = A[: , 0];              # print (C) # col 0
C = A[: , 0:1];            # print (C) # col 0 , preserve data shape
C = A[:,:-1];              # print (C) # wrap around slicing
C = A.sum(axis=0);         # print (C) # sum of columns , i.e. vertically
C = A.sum(axis=1);         # print (C) # sum of rows , i.e. horizontally
C = np.reshape(A,-1);      # print (C) # Reshape array without changing data
C = A.reshape(1,4);        # print (C) # Reshape array without changing data

# broadcasting ???


import os
#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, '../00_data/AAPL.csv')

# I think nupmy only deals with numerical data
#A = np.genfromtxt(filename , delimiter="," , skip_header=1); print(A)


# normalize all elements
A_n = np.linalg.norm(A, axis=1, keepdims=True) # length = ||A||
A_normalized = A / A_n; print(A_normalized)

# Flatten image input data
# data = [num_examples , height , width , rgb=3 ]
# flatten a matrix of shape (a,b,c,d) to shape (b*c*d, a)  use:
A_flatten = (A.reshape(A.shape[0], -1)).T

np.squeeze(A) # remove redundant dimensions
A.squeeze()

np.pad( A , pad_width ) # add padding around a given array
np.pad( A , pad_width ) # specific padding for specific dimension of the array

# casting to a differnt type
A.astype(int)
