from sikuli import *

class TearDown:
    #This is the constructor of the TearDown class.
    #It does all the tear down tasks by calling local methods of the class.
    def __init__(self, passedInLogger):
        print ("tearDownClass __init__ method is called")
        self.closeMultiControl(passedInLogger)

    def closeMultiControl(self, passedInLogger):
       click("Menu_KebabMenu.png")
       click("MenuItem_Close.png")
       click("Btn_YesButton_CloseConfirmationPopup.png")
       #Waiting after closing MultiControl to avoid the MultiControl already running pop-up message in the next test
       wait(2)
       passedInLogger.info("MultiControl is closed")
       
      
       assert True

    def deleteClassFiles(self, passedInLogger):
        print ("Deleting class files in this folder")
        
   