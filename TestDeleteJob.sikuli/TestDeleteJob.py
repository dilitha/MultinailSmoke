from sikuli import *
import unittest
import OpenMultiControl
import LoadJob
import DeleteJob
import SetUp
import TearDown
from SetUp import SetUp
from TearDown import TearDown

class TestDeleteJob(unittest.TestCase):
    #imagePath = ""
    #writeLog = ""
    #loadedJobName = ""
    deletedJobName = ""
    actuallyDeletedJobName = ""
    
    @classmethod
    def setUpClass(self):
        print("This is setup class")

        #Create the SetUp instance
        #For the constructor, can use either 'default' or 'customised-<number>'. Refer 'SettingFolders.py' for values
        setUpClassInstance = SetUp('default')

        #Take the image folder location from the SetUp class instance variable 'setUpImagePath' and store in the global variable 'imagePath'
        self.imagePath = setUpClassInstance.setUpImagePath
        #imagePath = SetUp.setImagePath()

        print("Image Path in setUpClass method is: " + self.imagePath)

        #Obtaining logger handle to write all log messages into the log file
        self.writeLog = setUpClassInstance.setUpLogger
        self.writeLog.info('Set up is completed')
    
    @classmethod
    def tearDownClass(self):
        print("This is teardown class")

        #Create the TearDown instance
        tearDownClassInstance = TearDown(self.writeLog)
        
        #TearDown.closeMultiControl()

        self.writeLog.info('Tear Down is completed')

        assert True
    
    def openSoftware(self):

        print("Image Path at the start of openSoftware2 is: " + TestDeleteJob.imagePath)

        print getImagePath()
        resetImagePath(self.imagePath)
        print getImagePath()    
        
        reload(OpenMultiControl)
        
        OpenMultiControl.openMultiControl()

        print("Image path when quitting openSoftware is : ")
        print(getImagePath())

        assert True

    #Had to mark this method as a @classmethod. Otherwise 'self.loadedJobName' was not identified.
    @classmethod
    def loadTheJob(self):

        print("Image path soon after loadTheJob is : ")
        print(getImagePath())

        reload(LoadJob)
        
        print("Image path after reload LoadJob Job is : ")
        print(getImagePath())

        self.loadedJobName = LoadJob.loadTheJobFirst()
        print("Job name inside the unit test is : " + self.loadedJobName)


    def verifyTheLoadedJob(self):

        #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
        
        print("Image path before SECOND reload of LoadJob Job is : ")
        print(getImagePath())
               
        reload(LoadJob)
        
        print("Image path after SECOND reload LoadJob Job is : ")
        print(getImagePath())
          
        LoadJob.verifyJobLoaded(self.loadedJobName)

    def verifyJobIsAlreadyLoaded(self):

        reload(DeleteJob)
        '''
        Uncomment next 3 lines after removing the global variable usage
        global jobNameInUnitTest
        jobNameInUnitTest = DeleteJob.verifyJobIsAlreadyLoaded()
        print("Variable value of jobNameInUnitTest is: " + jobNameInUnitTest)

        '''
        TestDeleteJob.deletedJobName = DeleteJob.verifyJobIsAlreadyLoaded()
        print("Variable value of jobNameInUnitTest is: " + TestDeleteJob.deletedJobName)

        #deletedJobNameInUnitTest = DeleteJob.deleteJob(jobNameInUnitTest)
        #DeleteJob.verifyTheJobIsDeleted(deletedJobNameInUnitTest)
        #DeleteJob.verifyTheDeletedJobIsReturned(deletedJobNameInUnitTest)
        
    def deleteTheJob(self):
        reload(DeleteJob)

        TestDeleteJob.actuallyDeletedJobName = DeleteJob.deleteJob(TestDeleteJob.deletedJobName)
        print("Variable value of deletedJobNameInUnitTest is: " + TestDeleteJob.actuallyDeletedJobName)

    def verifyTheJobIsDeleted(self):
        reload(DeleteJob)

        DeleteJob.verifyTheJobIsDeleted(TestDeleteJob.actuallyDeletedJobName)
        print("Variable value of deletedJobNameInUnitTest is: " + TestDeleteJob.actuallyDeletedJobName)

    def verifyTheJobIsReturned(self):
        reload(DeleteJob)

        print("Variable value of actuallyDeletedJobName is: " + TestDeleteJob.actuallyDeletedJobName)
        DeleteJob.verifyTheDeletedJobIsReturned(TestDeleteJob.actuallyDeletedJobName)