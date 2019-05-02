import sys
import random
import numpy as np

def get_similar_pairs( sets):
      pairs = []
      for set1 in range(len(sets.keys())-1):
          for k in range(len(sets[set1])-1):
              for j in range(k, len(sets[set1])):
                  pairs.append((set1, k, set1, j))
      
      similar_pairs = []
      for pair in pairs:
      #    print(pair, sets[pair[0]][pair[1]-1], sets[pair[2]][pair[3]-1])
          similar_pairs.append((images_num[sets[pair[0]][pair[1]-1]], images_num[sets[pair[2]][pair[3]-1]]))
      print(len(similar_pairs))
      
      selection = 20000
      select_pairs = random.sample(range(0, len(similar_pairs)), selection)
      
      similar_select = []
      for idx in select_pairs:
          similar_select.append(similar_pairs[idx])
      
      similar_numpy = np.zeros((selection, len(images)))
      for idx, pair in enumerate(similar_select):
          similar_numpy[idx, pair[0]] = -1
          similar_numpy[idx, pair[1]] = 1
      return similar_numpy
      
def read_images(a):
    images = []
    for line in a:
        images.append(line.strip()[1:-2])
    return images

a = open(sys.argv[1],'r')
b = open(sys.argv[2],'r')

images = [c.strip() for c in a.readlines()] #read_images(a)
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
print(sets.keys())

train_sets = dict()
test_sets = dict()
for key in sets:
    if key not in train_sets:
       train_sets[key] = sets[key][:int(0.8*len(sets[key]))]
       test_sets[key] = sets[key][int(0.8*len(sets[key])):]
    print(key, len(sets[key]))

train_similar_numpy = get_similar_pairs(train_sets)
test_similar_numpy = get_similar_pairs(test_sets)
print(len(train_similar_numpy), len(test_similar_numpy))

np.save('train_similar.npy', train_similar_numpy)
np.save('test_similar.npy', test_similar_numpy)
