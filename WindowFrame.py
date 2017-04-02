import Tkinter
import numpy
import PIL
from PIL import ImageTk
from PIL import Image

class WindowFrame:

    xAxis = 0
    yAxis = 0
    MainWindow = 0
    MainObj = 0
    winFrame = object()
    btnQuit = object()
    btnNext = object()
    image = object()
    method = object()
    callingObj = object()
#    ImagePath = "C:\\Users\\Imran Ullah\\Desktop\\FYP\\GUI - FYP2\\Images\\6_left-grayscale.png"
    labelImg = 0
  
    
    def __init__(self, mainObj, MainWin, wWidth, wHeight, function, Object, xAxis = 10, yAxis = 10):
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.MainWindow = MainWin
        self.MainObj = mainObj
        if (self.callingObj != 0):    
            self.callingObj = Object
        
        if (function != 0):
            self.method = function
        
        global winFrame
        self.winFrame = Tkinter.Frame(self.MainWindow, width = wWidth, height = wHeight)
        self.winFrame['borderwidth'] = 5
        self.winFrame['relief'] = 'ridge'
        self.winFrame.place(x=xAxis,y=yAxis)
        #self.winFrame.configure(background="White")


        self.btnQuit= Tkinter.Button(self.winFrame, text = "Close", width=8, command= lambda: self.quitProgram(self.MainWindow))
        self.btnQuit.place(x=650, y=450)
        self.btnNext = Tkinter.Button(self.winFrame, text = "Next", width=8, command= lambda: self.NextWindow(self.method))
        self.btnNext.place(x=575, y=450)


    def setCallObject(self, obj):
        self.callingObj = obj

        
    def setMethod(self, function):
        self.method = function


    def quitProgram(self, window):
        global MainWindow
        self.MainWindow.destroy()

        
    def getWindowFrame(self):
        global winFrame
        return self.winFrame


    def unhide(self):
        self.winFrame.place(x=self.xAxis,y=self.yAxis)


    def hide(self):
        self.winFrame.place_forget()


    def NextWindow(self, methodToExecute):
        listWF = list(self.MainObj.listOfWinFrame)
        print("Size: ", len(listWF))
        
        if (self.method == 0 or self.callingObj == 0):
            print("Calling Method or the Object from which Method is called is 0")
            return
        
        if (self.method != 1):
            methodToExecute()                   ## Executing the Method for "Next Frame" 
        
        if (self.callingObj == self.MainObj.ExEd):
            img = self.MainObj.ExEd.getImage()  ## Getting Result for "Next Frame"
        elif (self.callingObj == self.MainObj.BV):
            img = self.MainObj.BV.getImage()  ## Getting Result for "Next Frame"
        else:
            print ("Error: No specified object for getImage() function")
            
        jpgImg = Image.fromarray(img)
        current = 0
        
        for i in xrange(len(listWF)):       ## Hiding all Frames
            listWF[i].hide()
            if (listWF[i] == self):
                current = i
                print (current)
                

        if (current == len(listWF)-1):    ## Disable the "Next Button" of last frame
            print ("Last")
            listWF[current].unhide()
            listWF[current].setImage(jpgImg)
            listWF[current].displayImage()
            self.btnNext['state'] = 'disable'
        else:                               ## unhide the Next Frame
            listWF[current+1].unhide()
            listWF[current+1].setImage(jpgImg)
            listWF[current+1].displayImage()
            
        print(current, " is done!! _Remove me_")


    def removeComponent(self):
        self.btnQuit.destroy()
        self.btnNext.destroy()


    def setImage(self, img):
        self.image = img


    def displayImage(self):
        #imgRes = self.image.resize((375,250))
        #self.image = imgRes
        imgTk = ImageTk.PhotoImage(image=self.image)
        self.image = imgTk
        self.labelImg = Tkinter.Label(self.winFrame, image = self.image)
        self.labelImg.place(x=450, y=100)
