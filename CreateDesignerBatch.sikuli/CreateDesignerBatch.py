from sikuli import *
import shutil

'''
#Here is the structure of the global dictionary which will store designer member details.
#Currently, this is not used to retrieve information. Only storing is done.
#In future, use this to retrieve information as well.
designerMembers = {
    'Member1' : {
        'MemberName' : " ",
        'Grade'      : " ",
        'Batch'      : " ",
        'Length'     : " ",
        'Width'      : " ",
        'Depth'      : " "
    }
}
'''

designerMembers = {}

memberDesignedCount = 0
lastDesignedMemberName = ""
memberNameCharacterCount = 0

def setDesignerMembers(memberCreated):
    global designerMembers
    designerMembers[memberCreated['MemberName']] = memberCreated


def getDesignerMembers(memberToRetrieve):
    global designerMembers
    print("Inside the \'getDesignerMembers\' function")
    print(designerMembers)
    return designerMembers[memberToRetrieve]

def openDesignerPage():
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    #Following Wait was added because, in the VM, Designer button was not clicked otherwise. 
    wait(1)
    if exists("Btn_Designer.png"):
        click("Btn_Designer.png")
    else:
        print("Designer button not found")
        assert False
    mouseMove(-100, 0)
    

def verifyDesignerPageHeadings():

    designerArea = Region(Region(652,5,1264,1033))
    try:
        designerArea.find("Txt_Designer.png")
        print("Designer text found!")
    except:
        print("Designer text not found")
        assert False

    try:
       designerArea.find("Section_Mitres.png")
       print("Mitres text found!")
    except:
       print("Mitres text not found")
       assert False

    try:
        designerArea.find("Section_Stock.png")
        print("Stock text found!")
    except:
        print("Stock text not found")
        assert False

    try:
        designerArea.find("Section_Batch.png")
        print("Batch text found")
    except:
        print("Batch text not found")
        assert False
    
def expandDesignerHeadings():
    click("Section_Mitres.png")
    wait(0.5)
    
    click("Section_Stock.png")

def verifyDesignerSubSections():
    designerAreaExpanded = Region(Region(1151,91,766,781))
    try:
        designerAreaExpanded.find("SubHeading_Mitre_Type.png")
        print("Mitre Type sub-heading found")
    except:
        print("Mitre Type sub-heading not found")
        assert False
    click("SubHeading_Mitre_Type.png")

    try:
        designerAreaExpanded.find("SubHeading_Mitre_Type.png")
        print("Second Mitre Type sub-heading found")
    except:
        print("Second Mitre Type sub-heading not found")
        assert False

    try:
        designerAreaExpanded.find("SubHeading_Member_Name.png")
        print("Member Name found")
    except:
        print("Member Name not found")
        assert False

    try:
        designerAreaExpanded.find("SubHeading_Stock_Length.png")
        print("Stock Length found")
    except:
        print("Stock Length not found")
        assert False

    try:
        designerAreaExpanded.find("DropDown_Designer_Grade.png")
        print("Grade drop down found")
    except:
        print("Grade drop down not found")
        assert False
        
    try:
        designerAreaExpanded.find("Checkbox_Allow_Stacking.png")
        print("Allow stacking found")
    except:
        print("Allow stacking not found")
        assert False

    try:
        designerAreaExpanded.find("Checkbox_Print_Label.png")
        print("Print Label found")
    except:
        print("Print Label not found")
        assert False

    try:
        designerAreaExpanded.find("Checkbox_Enable_Reuse.png")
        print("Enable Re-use found")
    except:
        print("Enable Re-use not found")
        assert False

    try:
        designerAreaExpanded.find("SubHeading_Designer_Batch.png")
        print("Batch drop down found")
    except:
        print("Batch drop down not found")
        assert False

    try:
        designerAreaExpanded.find("Btn_Designer_Add.png")
        print("Add button found")
    except:
        print("Add button not found")
        assert False

    try:
        designerAreaExpanded.find("Shape_designer_left.png")
        print("Designer left corner shape found")
    except:
        print("Designer left corner shape not found")
        assert False

    try:
        designerAreaExpanded.find("Shape_designer_right.png")
        print("Designer right corner shape found")
    except:
        print("Designer right corner shape not found")
        assert False

    try:
        designerAreaExpanded.find("Txt_Designer_Size.png")
        print("Size text found")
    except:
        print("Size text not found")
        assert False

    try:
        designerAreaExpanded.find("Txt_Designer_Qty.png")
        print("Qty text found")
    except:
        print("Qty text not found")
        assert False

    try:
        designerAreaExpanded.find("Checkbox_Designer_Overall_Length.png")
        print("Overall Length text found")
    except:
        print("Overall Length text not found")
        assert False

    try:
        designerAreaExpanded.find("Checkbox_Designer_Chord.png")
        print("Chord text found")
    except:
        print("Chord text not found")
        assert False

    assert True

def createDesignerMember(memberName, grade, batchName, length, width, depth, batchType):
    global lastDesignedMemberName
    #'batchType' can have one of the followings: new, existing, reuse
    defaultMemberName = "Block"
    #memberName = defaultMemberName + " " + memberName
    newDesignerMember = {'MemberName':'', 'Grade':'', 'Batch':'', 'Length':'', 'Width':'', 'Depth':''}
    print(newDesignerMember)
    newDesignerMember['MemberName'] = defaultMemberName + " " + memberName
    newDesignerMember['Grade'] = grade
    newDesignerMember['Batch'] = batchName
    print(newDesignerMember)

    
    
    designerArea = Region(Region(1123,91,790,940))
    
    click("SubHeading_Member_Name.png")

    if batchType == 'existing' or batchType =='reuse':
        #Delete the block name portion after 'Block' text of the previous member.
        #Then enter the new member name after 'Block' text portion. eg. 'Block bbb'.
        for x in range(memberNameCharacterCount):
            type(Key.BACKSPACE)
        type(Key.BACKSPACE)
    
    type(Key.SPACE + memberName)
    type(Key.ENTER)

    mouseMove(-42,11)
    
    x = Env.getMouseLocation().getX()
    y = Env.getMouseLocation().getY()
    captured = capture(x, y, 210, 26)

    #Name of the job screenshot which will be moved shortly to the 'Captured' folder
    currentMemberScreenshotName = "CurrentMemberDesigned.png"
    
    #Move the captured image away from the temp folder
    shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + currentMemberScreenshotName))

    print getBundlePath()

    #Store the text of the Current Member
    lastDesignedMemberName = find(getBundlePath()+"./temp/" + currentMemberScreenshotName).text()
    print("\'lastDesignedMemberName\' captured is: " + lastDesignedMemberName)

   
    type(Key.TAB + Key.TAB)
    click("DropDownBtn_Designer_Grade.png")
    type(grade)
    type(Key.ENTER)
    wait(0.25)

    try:
        designerArea.find("SubHeading_Designer_Grade.png")
        print("Grade sub-heading found")
    except:
        print("Grade sub-heading not found")
        assert False

    click("MemberLength_Designer.png")
    type(length)
    type(Key.ENTER)
    click("SubHeading_Designer_Batch.png")
    click("DropDownBtn_Designer_Batch.png")
    if batchType == 'new':
        click("DropDownOption_Designer_Create_New.png")
        type(batchName)
    else: 
        if batchType == 'existing':
            click("DropDownOption_Designer_Add_to_Existing.png")
        else: 
            if batchType == 'reuse':
                click("DropDownOption_Designer_Add_to_Reuse.png")
            else:
                print("Invalid batch type passed")
                assert False
                      
    type(Key.ENTER)
    click("Btn_Designer_Add.png")
    '''
    newMember = {
            'MemberName' : "Block Three",
            'Grade'      : "MGP10",
            'Batch'      : "One",
            'Length'     : "1000",
            'Width'      : "90",
            'Depth'      : "35"
            }
    '''
    setDesignerMembers(newDesignerMember)

    #Printing the global dictionary which contains all the designer members
    print("The global dictionary is: ")
    print(designerMembers)

    assert True
    #Returning the whole member created. This can be used to verify the batch name in the 'Batches' page 
    return newDesignerMember

    
    

def verifyCurrentBatchChangedToDesigner(designerBatchNamePassedIn):

    print("Designer batch name passed in is : " + designerBatchNamePassedIn)
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    #designerBatchNamePassedIn = "BatchOne"
    if exists("Section_Current_Batch.png"):
        click("Section_Current_Batch.png")
        
        #mouseMove(-50,20)
        mouseMove("DropDownBtn_Designer_Current_Batch.png")

        x = Env.getMouseLocation().getX()
        y = Env.getMouseLocation().getY()
        captured = capture(x-120, y-10, 115, 20)

        #Name of the job screenshot which will be moved shortly to the 'Captured' folder
        currentBatchScreenshotName = "CurrentBatch.png"
        
        #Move the captured image away from the temp folder
        shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + currentBatchScreenshotName))

        print getBundlePath()

        #Compare the text in the Current Batch drop-down with the Designer batch name
        currentBatchName = find(getBundlePath()+"./temp/" + currentBatchScreenshotName).text()

        #Extract the batch name. The batch name is displayed as, an example, "Designer - BatchOne"
        #We seperate by the " - " part. Then the batch name will be the 2nd item in the list generated
        batchName = currentBatchName.split(" - ")[1]
        
        #currentJobName = find("Captured1.png").text()
        print("Text extracted from the Current Batch drop-down is: " + batchName)

        print("Name given when creating the designer batch is: " + designerBatchNamePassedIn)
    
        #If equal, return
        if designerBatchNamePassedIn == batchName:
            print("Current Batch drop-down displays the name of the designer batch created")
            assert True
        
        else:
            print("Current Batch drop-down DOES NOT display the name of the designer batch created")
            assert False
    else:
        print("Current Batch Drop  down does not exist")
        assert False


def verifyDesignerBatchNameInBatchDropDown(designerBatchName):
    global batchNameCopied
    click("Btn_Work.png")
    click("SubHeading_Batches_Batch.png")
    click("DropDownBtn_Batches_Batch.png")
    type(Key.DOWN)
    
    #Copy the batch name already selected
    type("c", KEY_CTRL)
    batchNameCopied = Env.getClipboard()

    print ("batchNameCopied is: " + batchNameCopied)

    #Extract the batch name. The batch name is displayed as, an example, "Designer - BatchTwo"
    #We seperate by the " - " part. Then the batch name will be the 2nd item in the list generated
    batchName = batchNameCopied.split(" - ")[1]

    #Compare the batch name copied 
    if (designerBatchName == batchName):
       print ("Designer batch is displayed in the \'Batch\' drop-down")
       assert True
    else:
       print ("Designer batch is NOT displayed in the \'Batch\' drop-down")
       assert False 

def verifyMembersInTheDesignerBatch(memberNamePassedIn, isVeryFirstMember):
    print("isVeryFirstMember value is: ")
    print isVeryFirstMember
    type(Key.ESC)
    import shutil 
    type(Key.TAB + Key.TAB + Key.TAB)
      

    for x in range(5):
        #Added this wait to make the Key.DOWN slow
        wait(0.15)
        type(Key.DOWN)

    wait(0.15)

    for x in range(4):
        #Added this wait to make the Key.RIGHT slow
        wait(0.3)
        type(Key.RIGHT)


    #Please note that the members are alphabetically sorted.
    #Hence create members in the alphabetical order (eg, First member = aaa, Second member = bbb)
    if(isVeryFirstMember == True):
        print("This is the very first member")
        #Continue from here
        if exists("Checkbox_checked_Batches_Selected_Member.png"):
            mouseMove("Checkbox_checked_Batches_Selected_Member.png")
        else:
            print("Batch selected checkbox is not displayed")
            assert False
    else:
        #Second member
        type(Key.DOWN)
        for x in range(4):
            #Added this wait to make the Key.RIGHT slow
            wait(0.3)
            type(Key.RIGHT)
            mouseMove("Checkbox_checked_Batches_Selected_Member.png")
        
    #Capture the member name
    x = Env.getMouseLocation().getX()
    y = Env.getMouseLocation().getY()
    captured = capture(x+25, y-10, 215, 20)
    
     #Name of the member screenshot which will be moved shortly to the 'Captured' folder
    currentMemberScreenshotName = "DesignerBatchMemberName.png"

    
    #Move the captured image away from the temp folder
    shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + currentMemberScreenshotName))

    #Compare the text in the Member name in the Designer batch with the member name given in the Designer
    currentMemberName = find(getBundlePath()+"./temp/" + currentMemberScreenshotName).text()
    print("Text extracted from the Current Member Name is: " + currentMemberName)

    #Compare the member name in the Designer batch with the name provided when designing the member
    if (currentMemberName == memberNamePassedIn):
       print ("Designer batch contains the member designed")
       assert True
    else:
        if (currentMemberName == lastDesignedMemberName):
            print("Last Designed Member Name is: " + lastDesignedMemberName)
            print("Designer batch contains the member designed - Verified with the member name captured")
        else:
            print ("Designer batch does NOT contain the member designed")
            assert False 

def goBackToDesignerPage():
    mouseMove("SubHeading_Batches_Batch.png")
    click("DropDownBtn_Batches_Batch.png")
    #We are selecting the 'Create New' option because, when we do so,
    #the designer batch won't be selected when we return.
    click("DropDownOption_Batches_Create_New.png")
    click("Btn_Home.png")
    click("Btn_Designer.png")


def setCharacterCountOfPreviousMember(previousMemberName):
    #This method will return the character count of the previous member name
    global designerMembers
    global previousMembers
    memberNamePortion = ""
    global memberNameCharacterCount
    print("Member passed in is: "+ previousMemberName)

    memberNamePortion = previousMemberName.split(" ")[1]
    memberNameCharacterCount = len(memberNamePortion)
    
    print("Character count of the previous member is: ")
    print(memberNameCharacterCount)

def verifyReuseConfirmationPopupIsDisplayed():
    if exists("Pop-up_Reuse_Design_Confirmation.png"):
        print("Reuse confirmation pop-up is present")
    else:
        print("Reuse confirmation pop-up is NOT present")
        assert False

def cancelTheReuseConfirmationPopup():
    if exists("Btn_Reuse_Confirmation_Popup_No.png"):
        click("Btn_Reuse_Confirmation_Popup_No.png")
        print("Reuse confirmation pop-up No button is clicked")
    else:
        print("Reuse confirmation pop-up No button is NOT present")
        assert False

def clickAgainOnTheAddButton():
    if exists("Btn_Designer_Add.png"):
        click("Btn_Designer_Add.png")
        print("Designer Add button is clicked again")
    else:
        print("Designer Add button is NOT present when trying to click after clicking \'No\'")
        assert False

def confirmReuseMemberCreation():
    if exists("Btn_Reuse_Confirmation_Popup_Yes.png"):
        click("Btn_Reuse_Confirmation_Popup_Yes.png")
        print("Reuse confirmation pop-up Yes button is clicked")
    else:
        print("Reuse confirmation pop-up Yes button is NOT present")
        assert False

def verifyMemberInReuseGroup(reuseMemberNamePassedIn):
    click("Btn_Work.png")
    click("Section_Batches_Reuse_Group_Not_Selected.png")
    type(Key.DOWN)
    type(Key.DOWN)
    
    for x in range(4):
        type(Key.RIGHT)

    #Without this wait, mouse was moved only to the first bin icon
    wait(0.15)

    mouseMove("Btn_Batches_Reuse_Remove_Icon_Focussed.png")
    
    #Capture the member name
    x = Env.getMouseLocation().getX()
    y = Env.getMouseLocation().getY()
    captured = capture(x+25, y-10, 215, 20)
    
     #Name of the reuse member screenshot which will be moved shortly to the 'Captured' folder
    currentReuseMemberScreenshotName = "DesignerReuseMemberName.png"

    
    #Move the captured image away from the temp folder
    shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + currentReuseMemberScreenshotName))

    #Compare the text in the Reuse Member name in the Designer batch with the member name given in the Designer
    currentReuseMemberName = find(getBundlePath()+"./temp/" + currentReuseMemberScreenshotName).text()
    print("Text extracted from the Current Reuse Member Name is: " + currentReuseMemberName)

    #Compare the member name in the Designer batch with the name provided when designing the member
    if (currentReuseMemberName == reuseMemberNamePassedIn):
       print ("Designer batch contains the reuse member designed")
       assert True
    else:
        print ("Designer batch does NOT contain the reuse member designed")
        assert False 

'''
openDesignerPage()
verifyDesignerPageHeadings()
expandDesignerHeadings()
verifyDesignerSubSections()

createdDesignerMember = createDesignerMember("aaa", "MGP10", "One", "1000", "90", "35", "new")
verifyCurrentBatchChangedToDesigner(createdDesignerMember['Batch'])
verifyDesignerBatchNameInBatchDropDown(createdDesignerMember['Batch'])
verifyMembersInTheDesignerBatch(createdDesignerMember['MemberName'], True)

goBackToDesignerPage()

setCharacterCountOfPreviousMember(createdDesignerMember['MemberName'])
#memberDesignedCount += 1

createdDesignerMember = createDesignerMember("bbb", "MGP10", "One", "1000", "90", "35", "existing")
setCharacterCountOfPreviousMember(createdDesignerMember['MemberName'])
verifyDesignerBatchNameInBatchDropDown(createdDesignerMember['Batch'])
verifyMembersInTheDesignerBatch(createdDesignerMember['MemberName'], False)

goBackToDesignerPage()

createdReuseMember = createDesignerMember("ccc", "MGP10", "One", "1000", "90", "35", "reuse")
verifyReuseConfirmationPopupIsDisplayed()
cancelTheReuseConfirmationPopup()
clickAgainOnTheAddButton()
verifyReuseConfirmationPopupIsDisplayed()
confirmReuseMemberCreation()

verifyMemberInReuseGroup(createdReuseMember['MemberName'])
'''







    
    
    
    






    


