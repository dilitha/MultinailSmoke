from imp import reload
from sikuli import *
import unittest
import HTMLTestRunner
reload(HTMLTestRunner)
import OpenMultiControl
import LoadJob
import DeleteJob
import DefaultBatchCreation
import SetUp
import TearDown
from SetUp import SetUp
from TearDown import TearDown


jobNameInUnitTest = ""
alreadyLoadedJobInUnitTest = ""
deletedJobNameInUnitTest = ""
imagePath = ""
writeLog = "" #Used for logging
setUpClassInstance = "" #To hold the instance of SetUp class
tearDownClassInstance = "" #To hold the instance of TearDown class

removeImagePath()
print ("Image repo at the start is : ")
print getImagePath()


class TestLoadJob(unittest.TestCase):

    def openSoftware(self):

        print getImagePath()
        resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
        print getImagePath()
        
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

        resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
        
        print("Image path before SECOND reload of LoadJob Job is : ")
        print(getImagePath())
               
        reload(LoadJob)
        
        print("Image path after SECOND reload LoadJob Job is : ")
        print(getImagePath())
          
        LoadJob.verifyJobLoaded(jobNameInUnitTest)

        #print("Image path after LoadJob.verifyJobLoaded is : ")
        #print(getImagePath())

class TestDeleteJob(unittest.TestCase):
    def verifyJobIsAlreadyLoaded(self):

        reload(DeleteJob)

        global jobNameInUnitTest
        jobNameInUnitTest = DeleteJob.verifyJobIsAlreadyLoaded()
        print("Variable value of jobNameInUnitTest is: " + jobNameInUnitTest)
        #deletedJobNameInUnitTest = DeleteJob.deleteJob(jobNameInUnitTest)
        #DeleteJob.verifyTheJobIsDeleted(deletedJobNameInUnitTest)
        #DeleteJob.verifyTheDeletedJobIsReturned(deletedJobNameInUnitTest)
        
    def deleteTheJob(self):
        reload(DeleteJob)

        global deletedJobNameInUnitTest
        deletedJobNameInUnitTest = DeleteJob.deleteJob(jobNameInUnitTest)
        print("Variable value of deletedJobNameInUnitTest is: " + deletedJobNameInUnitTest)

    def verifyTheJobIsDeleted(self):
        reload(DeleteJob)

        global deletedJobNameInUnitTest
        DeleteJob.verifyTheJobIsDeleted(deletedJobNameInUnitTest)
        print("Variable value of deletedJobNameInUnitTest is: " + deletedJobNameInUnitTest)

    def verifyTheJobIsReturned(self):
        reload(DeleteJob)

        global deletedJobNameInUnitTest
        print("Variable value of deletedJobNameInUnitTest is: " + deletedJobNameInUnitTest)
        DeleteJob.verifyTheDeletedJobIsReturned(deletedJobNameInUnitTest)


def startTestRun(self):
    print("Start Test Run")

setattr(unittest.TestResult, 'startTestRun', startTestRun)

def stopTestRun(self):
    print("Stop Test Run")

setattr(unittest.TestResult, 'stopTestRun', stopTestRun)


class TestDefaultBatchCreation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This is setup class")

        #Create the SetUp instance
        global setUpClassInstance
        setUpClassInstance = SetUp('customised-1')

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

    


def suite():
    suite = unittest.TestSuite()
    # TestLoadJob
    '''
    suite.addTest(TestLoadJob('openSoftware'))
    suite.addTest(TestLoadJob('loadTheJob'))
    suite.addTest(TestLoadJob('verifyTheLoadedJob'))
    # TestDeleteJob
    suite.addTest(TestDeleteJob('verifyJobIsAlreadyLoaded'))
    suite.addTest(TestDeleteJob('deleteTheJob'))
    suite.addTest(TestDeleteJob('verifyTheJobIsDeleted'))
    suite.addTest(TestDeleteJob('verifyTheJobIsReturned'))
    '''
    # TestDefaultBatchCreation
    suite.addTest(TestDefaultBatchCreation('openSoftware'))
    suite.addTest(TestDefaultBatchCreation('loadTheJob'))
    suite.addTest(TestDefaultBatchCreation('verifyTheLoadedJob'))
    suite.addTest(TestDefaultBatchCreation('verifyTheCurrentBatchDropDown'))
    suite.addTest(TestDefaultBatchCreation('verifyGreyedOutBinIcon'))
    suite.addTest(TestDefaultBatchCreation('verifyGreyedOutCreateBatchButton'))
    suite.addTest(TestDefaultBatchCreation('verifyJobNameInBatchDropDown'))
    suite.addTest(TestDefaultBatchCreation('verifyActiveBinIcon'))
    suite.addTest(TestDefaultBatchCreation('verifyUpdateBatchButton'))
    suite.addTest(TestDefaultBatchCreation('verifySelectionOfCreateNew'))
    suite.addTest(TestDefaultBatchCreation('verifyGreyedOutBinIconAgain'))
    suite.addTest(TestDefaultBatchCreation('verifyActiveCreateBatchButton'))

    return suite

if __name__ == "__main__":
    suite = suite()
    unittest.TextTestRunner(verbosity=2)
    output = open(getBundlePath()+"\\results.html", 'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=output, title='Test Report', description='This is a test')
    runner.run(suite)  