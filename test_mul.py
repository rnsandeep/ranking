import numpy as np
import scipy
from scipy.sparse import csr_matrix
from rank_svm import *

X = scipy.matrix(np.load('features_lower.npy').astype(float))

S = np.load('test_similar.npy')
O = np.load('test_ordered.npy')
for i in range(1,20):

   w = np.load("weight_lower_"+str(i)+".npy")
   pairs = np.load('pairs_nums.npy')
   count = 0
   for o in O:
    pos = np.where(o==1)
    neg = np.where(o==-1)
    if X[pos]*w > X[neg]*w:
       count = count + 1
   print("ordered pairs all accuracy:", count, len(O))# len(pairs)) #len(O))

   pairs = np.load('pairs_nums.npy')
   count = 0
   for o in pairs:
    pos = o[0]
    neg = o[1] #np.where(o==-1)
    if X[pos]*w > X[neg]*w:
       count = count + 1
   print("ordered pairs only pos accuracy:", count, len(pairs))# len(pairs)) #len(O))   
