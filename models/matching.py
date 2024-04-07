import cv2
import numpy as np
import matplotlib.pyplot as plt

def filter(images,labels,id):
    mask=labels[:,0]==id
    labels=labels[mask]
    images=images[mask]
    return images,labels

def get_score(test,images):
    # print(len(images))
    test=cv2.resize(test,(200,200))
    sift=cv2.SIFT_create()
    f_image=None
    kp1,kp2,mp=None,None,None
    best_score=0
    score=[]
    i=0
    index=-1
    sift=cv2.SIFT_create()
    keyp1,des1=sift.detectAndCompute(test,None)
    for image in images:
        keyp2,des2=sift.detectAndCompute(image,None)
        matches=cv2.FlannBasedMatcher({'algorithm':4,'trees':5},{}).knnMatch(des1,des2,k=2)
        match_point=[]
        for p,q in matches:
            if p.distance<0.1*q.distance:
                match_point.append(p)
        keypoints=min(len(keyp1),len(keyp2))
        score.append(len(match_point)/keypoints* 100)
        if len(match_point)/keypoints* 100 > best_score:
            best_score=len(match_point)/keypoints* 100
            f_image=image
            kp1,kp2,mp=keyp1,keyp2,match_point
            index=i
        i+=1
    return best_score

def analysis(f_image,index,best_score,kp1,kp2,mp,test,y):
    print("label of matched one is ",y[index])
    print("score: ",best_score)
    result=cv2.drawMatches(test,kp1,f_image,kp2,mp,None)
    result=cv2.resize(result,None,fx=4,fy=4)
    plt.imshow(result)
    plt.axis('off')  # Turn off axis
    plt.show()