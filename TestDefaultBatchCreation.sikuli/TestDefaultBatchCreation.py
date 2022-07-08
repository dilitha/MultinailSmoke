from sikuli import *
import unittest
import OpenMultiControl
#import LoadJob
import DefaultBatchCreation
import SetUp
import TearDown
from SetUp import SetUp
from TearDown import TearDown

class TestDefaultBatchCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is setup class")

        #Create the SetUp instance
        global setUpClassInstance
        #For the constructor, can use either 'default' or 'customised-<number>'. Refer 'SettingFolders.py' for values
        setUpClassInstance = SetUp('default')

        global imagePath

        #Take the image folder location from the SetUp class instance variable 'setUpImagePath' and store in the global variable 'imagePath'
        imagePath = setUpClassInstance.setUpImagePath
        #imagePath = SetUp.setImagePath()

        print("Image Path in setUpClass method is: " + imagePath)

        #Obtaining logger handle to write all log messages into the log file
        global writeLog
        writeLog = setUpClassInstance.setUpLogger
        writeLog.info('Set up is completed')
    
    @classmethod
    def tearDownClass(cls):
        print("This is teardown class")

        #This is the global variable used to write log messages into the log file
        global writeLog

        #Create the TearDown instance
        global tearDownClassInstance
        tearDownClassInstance = TearDown(writeLog)
        
        #TearDown.closeMultiControl()

        writeLog.info('Tear Down is completed')

        assert True

    print("This is just above \'openSoftware\' method")
    
    def openSoftware(self):
        global imagePath
        print("Image Path at the start of openSoftware is: " + imagePath)

        print getImagePath()
        resetImagePath(imagePath)
        print getImagePath()    
        
        reload(OpenMultiControl)
        
        OpenMultiControl.openMultiControl()

        print("Image path when quitting openSoftware is : ")
        print(getImagePath())

        assert True

 
    def loadTheJob(self):

        print("Image path soon after loadTheJob is : ")
        print(getImagePath())

        reload(DefaultBatchCreation)
        
        print("Image path after reload DefaultBatchCreation is : ")
        print(getImagePath())

        global jobNameInUnitTest
        jobNameInUnitTest = DefaultBatchCreation.loadTheJobFirst()
        print("Job name inside the unit test is : " + jobNameInUnitTest)
        

    def verifyTheLoadedJob(self):

        
        print("Image path before SECOND reload of LoadJob Job is : ")
        print(getImagePath())
               
        reload(DefaultBatchCreation)
        
        print("Image path after SECOND reload DefaultBatchCreation is : ")
        print(getImagePath())
          
        DefaultBatchCreation.verifyJobLoaded(jobNameInUnitTest)

        #print("Image path after LoadJob.verifyJobLoaded is : ")
        #print(getImagePath())

    def verifyTheCurrentBatchDropDown(self):

        global jobNameInUnitTest
        DefaultBatchCreation.verifyCurrentBatchDropDown(jobNameInUnitTest)

    def verifyGreyedOutBinIcon(self):

        DefaultBatchCreation.verifyGreyedBinIcon()

    def verifyGreyedOutCreateBatchButton(self):

        DefaultBatchCreation.verifyGreyedCreateBatchButton()

    def verifyJobNameInBatchDropDown(self):

        DefaultBatchCreation.verifyJobNameInDropDown(jobNameInUnitTest)

    def verifyActiveBinIcon(self):

        DefaultBatchCreation.verifyActiveBinIcon()

    def verifyUpdateBatchButton(self):

        DefaultBatchCreation.verifyUpdateBatchButton()

    def verifySelectionOfCreateNew(self):

        DefaultBatchCreation.verifyCreateNewText()

    def verifyGreyedOutBinIconAgain(self):

        DefaultBatchCreation.verifyGreyedBinIconAgain()

    def verifyActiveCreateBatchButton(self):

        DefaultBatchCreation.verifyActiveCreateBatchButton()
