import numpy as np
import scipy
from scipy.sparse import csr_matrix
from rank_svm import *

X = scipy.matrix(np.load('features_lower.npy').astype(float))
print(X.shape)
S = np.load('train_similar.npy')
O = np.load('train_ordered.npy')
print(O.shape, S.shape)
pairs = np.load('pairs_nums.npy')
S = S[:2000]
O = []
for pair in pairs:
    vector = np.zeros(X.shape[0])
    vector[pair[0]] = 1
    vector[pair[1]] = -1
O.append(vector)
O = np.array(O)
count = 0
for pw in range(5,10):
    c = pow(2, pw)
    C_O = scipy.matrix(c * np.ones([O.shape[0], 1]))
    C_S = scipy.matrix(c * np.ones([S.shape[0], 1]))

    S = csr_matrix(S)
    O = csr_matrix(O)

    X = scipy.matrix(X)
    w = rank_svm(X, S, O, C_S, C_O)
    count = count +1
    print(w.shape)
    np.save("weight_lower_"+str(count)+".npy", w)
    
    

