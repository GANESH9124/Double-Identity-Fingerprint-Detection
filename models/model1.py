import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def format(img):
    width=200
    height=200
    size = (height,width)
    rs=cv2.resize(img,size)
    return rs

def create_dataset(path1,path2):
    x_real=np.load(path2)['data']
    x_real=x_real.squeeze()
    files=os.listdir(path1)
    images_dfp=[]
    labels_dfp=[]
    for file in files:
        pat=os.path.join(path1,file)
        img=cv2.imread(pat,0)
        rs=format(img)
        images_dfp.append(rs)
        labels_dfp.append(0)#for double
    images_dfp=np.array(images_dfp)
    labels_dfp=np.array(labels_dfp).reshape(-1,1)
    images_sfp=[]
    labels_sfp=[]
    for image in x_real:
        rs=format(image)
        images_sfp.append(rs)
        labels_sfp.append(1)# for single
    images_sfp=np.array(images_sfp)
    labels_sfp=np.array(labels_sfp).reshape(-1,1)

    return images_dfp,labels_dfp,images_sfp,labels_sfp

def combine_and_split(images_dfp,labels_dfp,images_sfp,labels_sfp,size):
    final_images = np.vstack((images_sfp, images_dfp))
    flattened_images = final_images.reshape(final_images.shape[0], -1)
    final_labels=np.vstack((labels_sfp,labels_dfp))
    X_train, X_test, y_train, y_test = train_test_split(flattened_images, np.ravel(final_labels), test_size=size,random_state=42)
    return X_train, X_test, y_train, y_test

def train(X_train,y_train):
    # Creating a Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    # Training the classifier on the training data
    rf_classifier.fit(X_train, y_train)
    return rf_classifier

def predict(image,rf_classifier):
    width=200
    height=200
    size = (height,width)
    rs=cv2.resize(image,size)
    image=rs.reshape(-1,1).T
    y_pred = rf_classifier.predict(image)
    return y_pred

def predict_lr(image,model):
    width=200
    height=200
    size = (height,width)
    rs=cv2.resize(image,size)
    image=rs.reshape(-1,1).T
    y_pred = model.predict(image)
    return y_pred
