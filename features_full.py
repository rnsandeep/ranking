import sys, os
import random
import numpy as np
import pickle

def read_images(a):
    images = []
    for line in a:
        images.append(line.strip()[1:-2])
    return images

a = open(sys.argv[1],'r')

images = read_images(a)
print("length of images:", len(images))

folder = '/home/ubuntu/rnsandeep/ObjectClassification/features'
count  = 0
features = []
existed = open('existed.txt','w')
for idx, image in enumerate(images):
    pkl = image.strip().replace(".jpg",".pkl")
    f = os.path.join(folder,pkl)
    if os.path.exists(f):
       existed.write(f.split("/")[-1].replace('.pkl','.jpg')+'\n')
       feat = pickle.load(open(f,'rb')).data.cpu().numpy()
       features.append(feat)
print(np.vstack(features).shape)
np.save('features_lower.npy', np.vstack(features))
print(count)
