import Tkinter
#import PIL
#from PIL import ImageTk
from PIL import Image
import tkFileDialog
from WindowFrame import WindowFrame
from Exudates import ExtractExudates
from BloodVessels import BloodVessels


class MainWindow:

    MainWindow = 0
    listOfWinFrame = list()
    FirstFrame = object()
    val = 0
    fileName = 0
    ExEd = 0
    BV = object()

    ## Window "Frames" Dimensions ###
    wHeight = 514
    wWidth = 780
            
    def __init__(self):    
        ### MainWindow: Hosts other windows (frames) ###
        global MainWindow
        MainWindow = Tkinter.Tk()
        MainWindow.geometry('800x534')
        MainWindow.resizable(width = False, height = False)
        #MainWindow.overrideredirect(1)

        ### Creating Extraction Algorithms Objects
        self.ExEd = ExtractExudates()
        self.BV = BloodVessels()

        self.fileName = Tkinter.StringVar()


        ### Welcome Frame [First Frame] ###
##        welcomeFrame = Tkinter.Frame(self.MainWindow, width = wWidth, height = wHeight)
##        welcomeFrame['borderwidth'] = 2
##        welcomeFrame['relief'] = 'sunken'
##        welcomeFrame.place(x=10,y=10)
##        WindowLabel = Tkinter.Label( welcomeFrame, text = "Detection of Diabetic Retinopathy", height = 1, width = 40)
##        WindowLabel.place(x=150, y=30)
##        WindowLabel.configure(background="White", font=("Times New Roman", 16, "bold"))


        ### Creating and Instantiating Objects of WindowFrame ###
        self.FirstFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, 0, 0)
        self.FirstFrame.btnNext['state'] = 'disable'

##        secFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
##        thirdFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
##        fourthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
##        fifthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
##        sixthFrame = WindowFrame(self, MainWindow, wWidth, wHeight)
##        seventhFrame = WindowFrame(self, MainWindow, wWidth, wHeight)


        ### Adding All WindowFrames to the List ###
        self.listOfWinFrame.append(self.FirstFrame)
##        self.listOfWinFrame.append(secFrame)
##        self.listOfWinFrame.append(thirdFrame)
##        self.listOfWinFrame.append(fourthFrame)
##        self.listOfWinFrame.append(fifthFrame)
##        self.listOfWinFrame.append(sixthFrame)
##        self.listOfWinFrame.append(seventhFrame)


        ### Welcome Frame ###
        WindowLabel = Tkinter.Label(self.FirstFrame.getWindowFrame(), text = "Feature Extraction", height = 1, width = 40)
        WindowLabel.place(x=150, y=30)
        WindowLabel.configure(background="White", font=("Times New Roman", 16, "bold"))

        # Adding RadioButtons to Welcome Frame
        self.val = Tkinter.IntVar()
        RB1 = Tkinter.Radiobutton(self.FirstFrame.getWindowFrame(), text="Extraction of Exudates", variable=self.val, value=1, command=self.check)
        RB1.place(x=100,y=100)
        RB2 = Tkinter.Radiobutton(self.FirstFrame.getWindowFrame(), text="Extraction of Blood Vessels", variable=self.val, value=2, command=self.check)
        RB2.place(x=100,y=120)
        RB3 = Tkinter.Radiobutton(self.FirstFrame.getWindowFrame(), text="Extraction of Microaneurysms", variable=self.val, value=3, command=self.check)
        RB3.place(x=100,y=140)

        # Adding Browse Button to Welcome Frame
        browseBtn = Tkinter.Button(self.FirstFrame.getWindowFrame(), text="Browse", width=8, command=self.browseWindow)
        browseBtn.place(x=450,y=410)


        MainWindow.mainloop()


    def getListOfWinFrame():
        return self.listOfWinFrame


### Browse Button for Welcome Frame ###
    def browseWindow(self):
        FILEOPENOPTIONS = dict(defaultextension='*.*', filetypes=[('jpeg','*.jpeg'), ('jpg','*.jpg'), ('All Files','*.*')])
        self.fileName = tkFileDialog.askopenfilename(**FILEOPENOPTIONS)
        image = Image.open(self.fileName)           ##Opening Image
        #imgRes = image.resize((299,299))            ##Resizing Image
        self.listOfWinFrame[0].setImage(image)     ##Passing Image to Frame for setting
        self.listOfWinFrame[0].displayImage()       ##Displaying Image
        self.ExEd.setImage(image)                  ##Passing Image to Exudates for Processing
        self.BV.setImage(image)

    def check(self):
                ### Selecting Set of Frames based on RadioButton Value ###
        print(self.val.get())
        if (self.val.get() == 1):
            print("Selected 1")

            ## Delete All Except first ##
                # Flushing list to clear it for creating new frames
            self.listOfWinFrame = 0
            self.listOfWinFrame = list()
            self.listOfWinFrame.append(self.FirstFrame)

            ## Creating Frames According to the Feature Selected ##
            
            
            self.listOfWinFrame[0].setCallObject(self.ExEd)
            self.listOfWinFrame[0].setMethod(self.ExEd.greenComp)
            secFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.ExEd.applyCLAHE, self.ExEd)
            thirdFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.ExEd.applyDilation, self.ExEd)
            fourthFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.ExEd.applyThreshold, self.ExEd)
            fifthFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.ExEd.applyMedianFilter, self.ExEd)

            ## Adding Frames to the list ##
            self.listOfWinFrame.append(secFrame)
            self.listOfWinFrame.append(thirdFrame)
            self.listOfWinFrame.append(fourthFrame)
            self.listOfWinFrame.append(fifthFrame)
            
            ## Hide All Except first ###
            for i in xrange(len(self.listOfWinFrame)):
                if(i != 0):
                    self.listOfWinFrame[i].hide()
            self.listOfWinFrame[0].unhide()

            if (len(self.listOfWinFrame) > 1):
                        self.listOfWinFrame[0].btnNext['state'] = 'active'
                                            
        elif (self.val.get() == 2):
            print("Selected 2")
            
                        ## Delete All Except first ##
                # Flushing list to clear it for creating new frames
            self.listOfWinFrame = 0
            self.listOfWinFrame = list()
            self.listOfWinFrame.append(self.FirstFrame)

            ## Creating Frames According to the Feature Selected ##
            self.listOfWinFrame[0].setCallObject(self.BV)
            self.listOfWinFrame[0].setMethod(self.BV.greenComp)
            secFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.BV.histEqualize, self.BV )
            thirdFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.BV.applyKirschFilter, self.BV)
            fourthFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.BV.applyThreshold, self.BV)
            fifthFrame = WindowFrame(self, MainWindow, self.wWidth, self.wHeight, self.BV.cleanSmallObjects, self.BV)
            sixthFrame = WindowFrame(self,MainWindow,self.wWidth, self.wHeight, 1, self.BV)

            ## Adding Frames to the list ##
            self.listOfWinFrame.append(secFrame)
            self.listOfWinFrame.append(thirdFrame)
            self.listOfWinFrame.append(fourthFrame)
            self.listOfWinFrame.append(fifthFrame)
            self.listOfWinFrame.append(sixthFrame)
            
            ## Hide All Except first ###
            for i in xrange(len(self.listOfWinFrame)):
                if(i != 0):
                    self.listOfWinFrame[i].hide()
            self.listOfWinFrame[0].unhide()

            if (len(self.listOfWinFrame) > 1):
                        self.listOfWinFrame[0].btnNext['state'] = 'active'
            
            
            
        elif (self.val.get() == 3):
            print("Selected 3")
        else:
            print("Not Working")


#######################
### Main() Function ###
#######################

mainObj = MainWindow()
