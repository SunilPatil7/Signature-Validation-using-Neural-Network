import preproc
import features
import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from scipy import ndimage
from skimage.measure import regionprops
from skimage import io
from skimage.filters import threshold_otsu   # For finding the threshold for grayscale to binary conversion


def getFeatures(path, img=None, display=False):
    if img is None:
        img = mpimg.imread(path)
    img = preproc.preproc(path, display=display)
    ratio = features.Ratio(img)
    centroid = features.Centroid(img)
    eccentricity, solidity = features.EccentricitySolidity(img)
    skewness, kurtosis = features.SkewKurtosis(img)
    retVal = (ratio, centroid, eccentricity, solidity, skewness, kurtosis)
    return retVal

def getCSVFeatures(path, img=None, display=False):
    if img is None:
        img = mpimg.imread(path)
    temp = getFeatures(path, display=display)
    features = (temp[0], temp[1][0], temp[1][1], temp[2], temp[3], temp[4][0], temp[4][1], temp[5][0], temp[5][1])
    return features

def makeCSV():
    if not(os.path.exists('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features')):
        os.mkdir('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features')
        print('New folder "Features" created')
    if not(os.path.exists('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Training')):
        os.mkdir('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Training')
        print('New folder "Features/Training" created')
    if not(os.path.exists('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Testing')):
        os.mkdir('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Testing')
        print('New folder "Features/Testing" created')
    # genuine signatures path
    gpath = 'C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/valid/'
    # forged signatures path
    fpath = 'C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/invalid/'
    for person in range(1, 11):
        per = ('00'+str(person))[-3:]
        print('Saving features for person id-',per)
        
        with open('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Training/training_'+per+'.csv', 'w') as handle:
            handle.write('ratio,cent_y,cent_x,eccentricity,solidity,skew_x,skew_y,kurt_x,kurt_y,output\n')
            # Training set
            for i in range(0,3):
                source = os.path.join(gpath, per+per+'_00'+str(i)+'.png')
                features = getCSVFeatures(path=source)
                handle.write(','.join(map(str, features))+',1\n')
            for i in range(0,3):
                source = os.path.join(fpath, '021'+per+'_00'+str(i)+'.png')
                features = getCSVFeatures(path=source)
                handle.write(','.join(map(str, features))+',0\n')
        
        with open('C:/Users/patol/Desktop/final year project/final year project/Signature-Verification-master/data/Features/Testing/testing_'+per+'.csv', 'w') as handle:
            handle.write('ratio,cent_y,cent_x,eccentricity,solidity,skew_x,skew_y,kurt_x,kurt_y,output\n')
            # Testing set
            for i in range(3, 5):
                source = os.path.join(gpath, per+per+'_00'+str(i)+'.png')
                features = getCSVFeatures(path=source)
                handle.write(','.join(map(str, features))+',1\n')
            for i in range(3,5):
                source = os.path.join(fpath, '021'+per+'_00'+str(i)+'.png')
                features = getCSVFeatures(path=source)
                handle.write(','.join(map(str, features))+',0\n')

if __name__ == "__main__":
    main()