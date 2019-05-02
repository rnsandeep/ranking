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
b = open("existed.txt",'w')
for idx, image in enumerate(images):
    pkl = image.strip().replace(".jpg",".pkl")
    up = os.path.join(folder+ "_up", pkl)
    middle = os.path.join(folder+ "_middle", pkl) # "_middle", pkl)
    lower = os.path.join(folder+ "_lower", pkl)
    if  os.path.exists(up) and os.path.exists(middle) and os.path.exists(lower):
        up_feat = pickle.load(open(up ,'rb')).data.cpu().numpy()
        middle_feat = pickle.load(open(middle ,'rb')).data.cpu().numpy()
        lower_feat = pickle.load(open(lower ,'rb')).data.cpu().numpy()
        feat = np.hstack((up_feat, middle_feat, lower_feat))
        features.append(feat)
        b.write(image+'\n')
    else:
        if os.path.exists(up):
           feat = pickle.load(open(up ,'rb')).data.cpu().numpy()
        elif os.path.exists(middle):
           feat = pickle.load(open(middle ,'rb')).data.cpu().numpy()
        elif os.path.exists(lower):
           feat = pickle.load(open(lower ,'rb')).data.cpu().numpy()
        else:
           count = count +1
#           feat = np.zeros(2048).reshape((1,2048))
#        features.append(np.hstack((feat, feat, feat)))
b.close()
print(np.vstack(features).shape)
np.save('features_parts.npy', np.vstack(features))
print(count)
