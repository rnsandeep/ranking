import sys
import random
import numpy as np

def get_ordered_pairs( sets):
      pairs = []
      for set1 in range(len(sets.keys())-1):
          for set2 in range(set1+1, len(sets.keys())):
              total = len(sets[set1])*len(sets[set2])
              for k in range(len(sets[set1])):
                 for j in range(len(sets[set2])):
                     pairs.append((set1, k, set2, j))
      
      ordered_pairs = []
      for pair in pairs:
      #    print(pair, sets[pair[0]][pair[1]-1], sets[pair[2]][pair[3]-1])
          ordered_pairs.append((images_num[sets[pair[0]][pair[1]-1]], images_num[sets[pair[2]][pair[3]-1]]))
      print(len(ordered_pairs))
      
      selection = 20000
      select_pairs = random.sample(range(0, len(ordered_pairs)), selection)
      
      ordered_select = []
      for idx in select_pairs:
          ordered_select.append(ordered_pairs[idx])
      
      order_numpy = np.zeros((selection, len(images)))
      for idx, pair in enumerate(ordered_select):
          order_numpy[idx, pair[0]] = -1
          order_numpy[idx, pair[1]] = 1
      return  order_numpy
      
def read_images(a):
    images = []
    for line in a:
        images.append(line.strip()[1:-2])
    return images

a = open(sys.argv[1],'r')
b = open(sys.argv[2],'r')

images = [c.strip() for c in a.readlines()]
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

train_order_numpy = get_ordered_pairs(train_sets)
test_order_numpy = get_ordered_pairs(test_sets)
print(len(train_order_numpy), len(test_order_numpy))

np.save('train_ordered.npy', train_order_numpy)
np.save('test_ordered.npy', test_order_numpy)
