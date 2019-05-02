import sys
import random
import numpy as np
import pickle
from collections import Counter 
ordered = np.load(sys.argv[2])
      
def read_images(a):
    images = []
    for line in a:
        images.append(line.strip()[1:-2])
    return images

a = open(sys.argv[1],'r')
b = open(sys.argv[3],'r')
images = [c.strip() for c in a.readlines()] #read_images(a)
boundaries = read_images(b)

print("legnth of images:", len(images))

sets = pickle.load(open('sets.pkl','rb'))
for cnt in sets:
    print(cnt, len(sets[cnt]))

pairs = []
pairs_nums = []
for j in range(0, ordered.shape[0]):
   a = ordered[j]
   pos = np.where(a>0)[0]
   neg = np.where(a<0)[0]
   if len(pos) > 0 and len(neg) > 0:
      if images[pos[0]] in sets[0] or images[pos[0]] in sets[1]:
         continue
      if images[neg[0]] in sets[0] or images[neg[0]] in sets[1]:
         continue
      
      pos_image = images[pos[0]]
      neg_image = images[neg[0]]
      pairs_nums.append((pos[0], neg[0]))
      pairs.append((pos_image, neg_image))

np.save('pairs_nums.npy', pairs_nums)

scores_load = pickle.load(open('scores.pkl','rb'))
#print(scores_load.keys())
scores = {}
for key in scores_load:
    scores[key.split('/')[-1]] = scores_load[key]
count  = 0
correct = 0
for pair in pairs:
    if pair[0] in scores and pair[1] in scores:
       count = count +1
       if scores[pair[0]] > scores[pair[1]] :
          correct = correct + 1

print(correct, count)
#np.save('pairs_names.npy',pairs)
