
import numpy as np
import cv2 

def path2(img):
    path = "C:\\Users\\HamzaFayaz\\OneDrive\\Work Zone\\Skills-works\\Computer Vision\\Image Processing\\Images\\Data\\Concrete Crack Images"
    newpath = path +"\\"+img
    return newpath


def stackimages(array,time):
    
    size = len(array)-1
    check = 0
    for index in range(size):
        
        h1 = np.hstack((array[index],array[index+1]))
        h2 = np.hstack((array[index+2],array[index+3]))
        v = np.vstack((h1,h2))
        
        cv2.imshow("stack Images ",v)
        cv2.waitKey(0)
        check = check + 1
        if check == time:
            break 
    cv2.destroyAllWindows() 


def path(img):
    path = "F:\\Computer vison projects + data\\Deep Learning for Computer Vision\\Data\\MathWorks Created\\ASL Alphabet\\Classification\\Test\\A"
    path = path + '\\' + img
    return path

