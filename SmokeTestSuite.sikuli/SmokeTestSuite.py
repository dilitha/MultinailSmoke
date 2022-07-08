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
import TestLoadJob
from TestLoadJob import TestLoadJob
import TestDeleteJob
from TestDeleteJob import TestDeleteJob
import TestDefaultBatchCreation
from TestDefaultBatchCreation import TestDefaultBatchCreation
import TestCreateDesignerBatch
from TestCreateDesignerBatch import TestCreateDesignerBatch


jobNameInUnitTest = ""
alreadyLoadedJobInUnitTest = ""
deletedJobNameInUnitTest = ""
imagePath = ""
writeLog = "" #Used for logging
setUpClassInstance = "" #To hold the instance of SetUp class
tearDownClassInstance = "" #To hold the instance of TearDown class


def suite():
    suite = unittest.TestSuite()
    # TestDemo
    
    suite.addTest(TestLoadJob('openSoftware'))
    suite.addTest(TestLoadJob('loadTheJob'))
    suite.addTest(TestLoadJob('verifyTheLoadedJob'))
    
    # TestDemo2
    
    suite.addTest(TestDeleteJob('openSoftware'))
    suite.addTest(TestDeleteJob('loadTheJob'))
    suite.addTest(TestDeleteJob('verifyTheLoadedJob'))
    suite.addTest(TestDeleteJob('verifyJobIsAlreadyLoaded'))
    suite.addTest(TestDeleteJob('deleteTheJob'))
    suite.addTest(TestDeleteJob('verifyTheJobIsDeleted'))
    suite.addTest(TestDeleteJob('verifyTheJobIsReturned'))
    
    
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
    
    
    suite.addTest(TestCreateDesignerBatch('openSoftware'))
    suite.addTest(TestCreateDesignerBatch('openDesignerPage'))
    suite.addTest(TestCreateDesignerBatch('verifyDesignerPageHeadings'))
    suite.addTest(TestCreateDesignerBatch('expandDesignerHeadings'))
    suite.addTest(TestCreateDesignerBatch('verifyDesignerSubSections'))
    suite.addTest(TestCreateDesignerBatch('createDesignerMember'))
    suite.addTest(TestCreateDesignerBatch('verifyCurrentBatchChangedToDesigner'))
    suite.addTest(TestCreateDesignerBatch('verifyDesignerBatchNameInBatchDropDown'))
    suite.addTest(TestCreateDesignerBatch('verifyTheVeryFirstMemberInTheDesignerBatch'))
    
    suite.addTest(TestCreateDesignerBatch('goBackToDesignerPage'))
    suite.addTest(TestCreateDesignerBatch('setCharacterCountOfPreviousMember'))
    suite.addTest(TestCreateDesignerBatch('createSecondDesignerMember'))
    suite.addTest(TestCreateDesignerBatch('setCharacterCountOfPreviousMember'))

    suite.addTest(TestCreateDesignerBatch('verifyDesignerBatchNameInBatchDropDown'))
    suite.addTest(TestCreateDesignerBatch('verifyTheSecondMemberInTheDesignerBatch'))
    suite.addTest(TestCreateDesignerBatch('goBackToDesignerPage'))
    suite.addTest(TestCreateDesignerBatch('createReuseMember'))

    suite.addTest(TestCreateDesignerBatch('verifyReuseConfirmationPopupIsDisplayed'))
    suite.addTest(TestCreateDesignerBatch('cancelTheReuseConfirmationPopup'))
    suite.addTest(TestCreateDesignerBatch('clickAgainOnTheAddButton'))
    suite.addTest(TestCreateDesignerBatch('verifyReuseConfirmationPopupIsDisplayed'))

    suite.addTest(TestCreateDesignerBatch('confirmReuseMemberCreation'))
    suite.addTest(TestCreateDesignerBatch('verifyMemberInReuseGroup'))
    
    return suite

if __name__ == "__main__":
    suite = suite()
    unittest.TextTestRunner(verbosity=2)
    output = open(getBundlePath()+"\\results.html", 'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=output, title='Test Report', description='This is a test')
    runner.run(suite)  
