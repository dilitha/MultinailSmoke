from sikuli import *
import unittest
import OpenMultiControl
#import LoadJob
import CreateDesignerBatch
import SetUp
import TearDown
from SetUp import SetUp
from TearDown import TearDown

class TestCreateDesignerBatch(unittest.TestCase):

    createdDesignerMember = {} #To hold designer member details
    createdReuseMember = {} #To hold reuse designer member details
    
    
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

    def openDesignerPage(self):
        CreateDesignerBatch.openDesignerPage()

    def verifyDesignerPageHeadings(self):
        CreateDesignerBatch.verifyDesignerPageHeadings()

    def expandDesignerHeadings(self):
        CreateDesignerBatch.expandDesignerHeadings()

    def verifyDesignerSubSections(self):
        CreateDesignerBatch.verifyDesignerSubSections()

    def createDesignerMember(self):
        TestCreateDesignerBatch.createdDesignerMember = CreateDesignerBatch.createDesignerMember("aaa", "MGP10", "One", "1000", "90", "35", "new")

    def verifyCurrentBatchChangedToDesigner(self):
        CreateDesignerBatch.verifyCurrentBatchChangedToDesigner(TestCreateDesignerBatch.createdDesignerMember['Batch'])

    def verifyDesignerBatchNameInBatchDropDown(self):
        CreateDesignerBatch.verifyDesignerBatchNameInBatchDropDown(TestCreateDesignerBatch.createdDesignerMember['Batch'])

    def verifyTheVeryFirstMemberInTheDesignerBatch(self):
        CreateDesignerBatch.verifyMembersInTheDesignerBatch(TestCreateDesignerBatch.createdDesignerMember['MemberName'], True)

    def goBackToDesignerPage(self):
        CreateDesignerBatch.goBackToDesignerPage()

    def setCharacterCountOfPreviousMember(self):
        CreateDesignerBatch.setCharacterCountOfPreviousMember(TestCreateDesignerBatch.createdDesignerMember['MemberName'])

    def createSecondDesignerMember(self):
        TestCreateDesignerBatch.createdDesignerMember = CreateDesignerBatch.createDesignerMember("bbb", "MGP10", "One", "1000", "90", "35", "existing")

    def setCharacterCountOfPreviousMember(self):
        CreateDesignerBatch.setCharacterCountOfPreviousMember(TestCreateDesignerBatch.createdDesignerMember['MemberName'])

    def verifyDesignerBatchNameInBatchDropDown(self):
        CreateDesignerBatch.verifyDesignerBatchNameInBatchDropDown(TestCreateDesignerBatch.createdDesignerMember['Batch'])

    def verifyTheSecondMemberInTheDesignerBatch(self):
        CreateDesignerBatch.verifyMembersInTheDesignerBatch(TestCreateDesignerBatch.createdDesignerMember['MemberName'], False)

    def goBackToDesignerPage(self):
        CreateDesignerBatch.goBackToDesignerPage()

    def createReuseMember(self):
        TestCreateDesignerBatch.createdReuseMember = CreateDesignerBatch.createDesignerMember("ccc", "MGP10", "One", "1000", "90", "35", "reuse")

    def verifyReuseConfirmationPopupIsDisplayed(self):
        CreateDesignerBatch.verifyReuseConfirmationPopupIsDisplayed()

    def cancelTheReuseConfirmationPopup(self):
        CreateDesignerBatch.cancelTheReuseConfirmationPopup()

    def clickAgainOnTheAddButton(self):
        CreateDesignerBatch.clickAgainOnTheAddButton()

    def verifyReuseConfirmationPopupIsDisplayed(self):
        CreateDesignerBatch.verifyReuseConfirmationPopupIsDisplayed()

    def confirmReuseMemberCreation(self):
        CreateDesignerBatch.confirmReuseMemberCreation()

    def verifyMemberInReuseGroup(self):
        CreateDesignerBatch.verifyMemberInReuseGroup(TestCreateDesignerBatch.createdReuseMember['MemberName'])
        
    
    
    
    