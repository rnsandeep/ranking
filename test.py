import numpy as np
import scipy
from scipy.sparse import csr_matrix
from rank_svm import *

X = scipy.matrix(np.load('features_rank.npy').astype(float))

S = np.load('test_similar.npy')
O = np.load('test_ordered.npy')

#print(w.shape)
w = np.load("weight_rank.npy")
#pairs = np.load('pairs_nums.npy')
count = 0
for o in O:
    pos = np.where(o==1)
    neg = np.where(o==-1)
    if X[pos]*w > X[neg]*w:
       count = count + 1
print(count, len(O))# len(pairs)) #len(O))
