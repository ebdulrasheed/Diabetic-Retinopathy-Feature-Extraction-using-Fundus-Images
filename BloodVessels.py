import numpy as np
import cv2
#from matplotlib import pyplot as plt
from skimage import morphology

class BloodVessels:
    #img = cv2.imread("E:\\Rasheed Files\\Rasheed Data (DONOT DELETE)\\FYP\Dataset\\1\\30_left.jpeg")
    
    jpegImg = 0
    grayImg = 0
    curImg = 0
    
    
    def setImage(self, img):
        self.jpegImg = img
        self.curImg = np.array(img)    ##Convert jpegFile to numpy array (Required for CV2)


    def getImage(self):
        return self.curImg

        
    def greenComp(self):
    ###Extracting Green Component
        gcImg = self.curImg[:,:,1]
        self.curImg = gcImg
    
    
    def histEqualize(self):
        histEqImg = cv2.equalizeHist(self.curImg)
        self.curImg = histEqImg    


    def applyKirschFilter(self):
        gray = self.curImg
        if gray.ndim > 2:
            raise Exception("illegal argument: input must be a single channel image (gray)")
        kernelG1 = np.array([[ 5,  5,  5],
                             [-3,  0, -3],
                             [-3, -3, -3]], dtype=np.float32)
        kernelG2 = np.array([[ 5,  5, -3],
                             [ 5,  0, -3],
                             [-3, -3, -3]], dtype=np.float32)
        kernelG3 = np.array([[ 5, -3, -3],
                             [ 5,  0, -3],
                             [ 5, -3, -3]], dtype=np.float32)
        kernelG4 = np.array([[-3, -3, -3],
                             [ 5,  0, -3],
                             [ 5,  5, -3]], dtype=np.float32)
        kernelG5 = np.array([[-3, -3, -3],
                             [-3,  0, -3],
                             [ 5,  5,  5]], dtype=np.float32)
        kernelG6 = np.array([[-3, -3, -3],
                             [-3,  0,  5],
                             [-3,  5,  5]], dtype=np.float32)
        kernelG7 = np.array([[-3, -3,  5],
                             [-3,  0,  5],
                             [-3, -3,  5]], dtype=np.float32)
        kernelG8 = np.array([[-3,  5,  5],
                             [-3,  0,  5],
                             [-3, -3, -3]], dtype=np.float32)
    
        g1 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g2 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG2), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g3 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG3), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g4 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG4), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g5 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG5), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g6 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG6), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g7 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG7), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        g8 = cv2.normalize(cv2.filter2D(gray, cv2.CV_32F, kernelG8), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)
        magn = cv2.max(g1, cv2.max(g2, cv2.max(g3, cv2.max(g4, cv2.max(g5, cv2.max(g6, cv2.max(g7, g8)))))))
        self.curImg = magn

    
    def applyThreshold(self):
        ret, threshImg = cv2.threshold(self.curImg,160,180,cv2.THRESH_BINARY_INV)
        self.curImg = threshImg

    
    def cleanSmallObjects(self):
        cleanImg = morphology.remove_small_objects(self.curImg, min_size=130, connectivity=100)
        self.curImg = cleanImg
    
    #cv2.imwrite('Final123.jpg',threshImg)