import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import cm
from skimage import io
from skimage.feature import canny
from skimage.morphology import dilation, disk
from skimage.transform import ProjectiveTransform, warp
from skimage.feature import match_template
from sudoku import solve_sudoku
from skimage.transform import rescale, resize, downscale_local_mean
from skimage import util 
from skimage.filters import threshold_otsu
from sudoku import solve_sudoku



def img_norm(sudocu):
    
    edges = canny(sudocu,sigma = 2)
    selem = disk(1)
    edges = dilation(edges, selem)
    edges = (edges).astype(np.uint8)
    ext_contours = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
    contour = max(ext_contours, key=cv2.contourArea)
    epsilon = 0.05 * cv2.arcLength(contour, True)
    corners = cv2.approxPolyDP(contour, epsilon, True).squeeze()

    certer_x = (corners[:,0]).mean().astype(int)
    certer_y = (corners[:,1]).mean().astype(int)
    center = np.array([certer_x,certer_y])
    
    left = []
    righ = []
    for i in corners:
        if i[0] < center[0]:
            left.append(i)
        else:
            righ.append(i)
            
    left = np.asarray(sorted(left, key=lambda k: k[1]))
    righ = np.asarray(sorted(righ, key=lambda k: k[1], reverse = True))
    corners_srt = np.vstack([left,righ])
    corners_des = np.array([ [0,0],
                        [0,1800],
                        [1800,1800],
                        [1800,0]
                        ])
    
    tform = ProjectiveTransform()
    tform.estimate(corners_des, corners_srt)
    image_warped = warp(sudocu, tform)
    sudocu_trans = image_warped[0:1800,0:1800]
    
    return sudocu_trans



def digit_search(nor_img,taplet):
    
    list1 = []
    for num,i in enumerate(range(0,1800,200)):
        for j in range(0,1800,200):
            lits = []
            for t in taplet:
                result = match_template(nor_img[i:i+200, j:j+200],t, pad_input=True)
                lits.append(result.max())
            list1.append(lits.index(max(lits)))
    sudocu_matrix=np.array(list1).reshape(9,9)
    
    return sudocu_matrix

