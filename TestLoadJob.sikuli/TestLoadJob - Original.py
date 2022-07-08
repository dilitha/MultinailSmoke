from sikuli import *
import OpenMultiControl
import LoadJob


class TestLoadJob(unittest.TestCase):
    
    def openSoftware(self):

        print getImagePath()
        resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
        #print getImagePath()
        
        ##path = "C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\SikuliX\\My Tests\\MultiControlAutomation\\Images\\"
        
        ##addImagePath(path)
        
        
        #click(""+aa+"1639535107506.png")
        #click(getImagePath()[1]+"\\"+"1639535107506.png")
        #click("C:\Users\dilitha.vithanage\Downloads\Multinail Test Work\Test Automation\SikuliX\My Tests\MultiControlAutomation\Images\1639535107506.png")
        
        
        reload(OpenMultiControl)
        
        OpenMultiControl.openMultiControl()

        print("Image path when quitting openSoftware is : ")
        print(getImagePath())

        assert True

        print("Image path when quitting openSoftware after Assert true is : ")
        print(getImagePath())

 
    def loadTheJob(self):

        print("Image path soon after loadTheJob is : ")
        print(getImagePath())

        reload(LoadJob)
        
        print("Image path after reload LoadJob Job is : ")
        print(getImagePath())

        global jobNameInUnitTest
        jobNameInUnitTest = LoadJob.loadTheJobFirst()
        print("Job name inside the unit test is : " + jobNameInUnitTest)
        

    def verifyTheLoadedJob(self):

        #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
        
        print("Image path before SECOND reload of LoadJob Job is : ")
        print(getImagePath())
               
        reload(LoadJob)
        
        print("Image path after SECOND reload LoadJob Job is : ")
        print(getImagePath())
          
        LoadJob.verifyJobLoaded(jobNameInUnitTest)

        #print("Image path after LoadJob.verifyJobLoaded is : ")
        #print(getImagePath())