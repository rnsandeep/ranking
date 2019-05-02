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
images = read_images(a) #c.strip() for c in a.readlines()] #read_images(a)
boundaries = read_images(b)

print("legnth of images:", len(images))
sets = dict()
counter = 0

sets[counter] = []
images_num = dict()
for idx, image in enumerate(images):
    images_num[image] = idx
    if image not in boundaries:
       sets[counter].append(image)
    else:
       counter =  counter +1
       sets[counter] = []
       sets[counter].append(image)

pickle.dump(sets, open('sets.pkl','wb'))

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

#np.save('pairs_nums.npy', pairs_nums)

features = np.load('features_rank.npy')
weight = np.load('weight_rank_1.npy')
#scores_load = pickle.load(open('scores.pkl','rb'))
#print(scores_load.keys())
scores = {}
for idx, key in enumerate(images):
    scores[key] = np.dot(features[idx], weight)
count  = 0
correct = 0
for pair in pairs:
    if pair[0] in scores and pair[1] in scores:
       count = count +1
       if scores[pair[0]] > scores[pair[1]] :
          correct = correct + 1

print(correct, count)
#np.save('pairs_names.npy',pairs)
