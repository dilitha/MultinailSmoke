from sikuli import *

jobName = ""
loadedJobsSection = ""
loadedJobsSplitted = ""
currentBatchSection = ""
currentBatchName = ""
jobNameCopied = ""
createNewTextCopied = ""
createNewText = "Create New"


def loadTheJobFirst():
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    print("Image path in DefaultBatchCreation is : ")
    print(getImagePath())

    print ("Looping the imagePath")
    imgPath = list(getImagePath()) # makes it a Python list
    # to loop through
    for p in imgPath:
        print p

    #the exists part was added because, find failed error was displayed otherwise.
    if exists("1648421660383.png"): a = find("1648421660383.png").text()
    
    print("Image Found !!!!")
    print("Image text is: " + a)
    b = a.split(" ", 1)

    #This is the job which will be loaded
    jobLoaded = b[1]
    print (jobLoaded)
    click("1648421660383.png")
    type(Key.DOWN + Key.SPACE)
    
    #wait(3)
    click("1647218830234.png")

    global jobName
    jobName = jobLoaded

    print ("The job loaded is : " + jobLoaded)
    
    print ("Global variable jobName is : " + jobName)

    print("Image path when quitting loadTheJobFirst is : ")
    print(getImagePath())

    assert True

    #This job name is sent to the main program so that it will be passed to the next method to compare with the actual job loaded
    return jobName

def verifyJobLoaded(nameOfTheJob):

    print("Job passed in is : " + nameOfTheJob)
    import shutil
    resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    print("Image path in verifyJobLoaded is : ")
    print(getImagePath())

    print("Bundle path in verifyJobLoaded is : ")
    print(getBundlePath())


    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    print("Image path AGAIN in verifyJobLoaded is : ")
    print(getImagePath())

    wait(1)

    if exists("1648422953985.png"): 
        loadedJobsSection = find("1648422953985.png").text() 
        #loadedJobsSection = find("1647233108239.png").text()
        loadedJobsSplitted = loadedJobsSection.split("\n", 1)
    
    
    print loadedJobsSplitted
    
    jobWithCheckbox = loadedJobsSplitted[1]
    print jobWithCheckbox
    
    checkboxAndJob = jobWithCheckbox.split(" ",1)
    actualJobWhichIsLoaded = checkboxAndJob[1]

    print ("Loaded job is : " + actualJobWhichIsLoaded)

    global jobName

    jobName = nameOfTheJob

    print ("Global variable jobName is : " + jobName)

    #Comparing the job which is loaded into the 'Loaded Jobs' section with the job which was loaded in the previous method
    if jobName == actualJobWhichIsLoaded:
        print ("Correct job is loaded")
        assert True
    else:
        print ("Job loaded is not correct")
        assert False

def verifyCurrentBatchDropDown(nameOfTheJob):

    print("Job passed in is : " + nameOfTheJob)
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    #nameOfTheJob = "TR~RF-00178~1"

    global currentBatchSection
    global currentBatchName

    #Check the 'Current Batch' drop-down and the batch name selected
    if exists("1648425226383.png"):
       currentBatchSection = find("1648425226383.png").text() 
       #Split the image to extract the name of the batch created. Split using the new line.
       currentBatchName = currentBatchSection.split("\n", 1)
       print("currentBatchSection is: " + currentBatchSection)
       #print("Name of the job is: " + nameOfTheJob)
       #Current batch name is the 2nd element in the list created after splitting
       print("Current batch name in the drop-down is: " + currentBatchName[1])
    else:
       print("\'Current Batch\' drop-down is NOT displayed")
       assert False

    #Compare the job loaded with the value selected in the 'Current Batch' drop-down
    if (currentBatchName[1] == nameOfTheJob):
       print ("Loaded job is displayed in the \'Current Batch\' drop-down")
       assert True
    else:
       print ("Loaded job is NOT displayed in the \'Current Batch\' drop-down")
       assert False


def verifyGreyedBinIcon():
    click("1648430723364.png")
    if(exists("1648431088726.png")!="null"):
        print("Greyed-out red bin icon is present")
        assert True
    else:
       print("Greyed-out red bin icon is NOT present")
       assert False

def verifyGreyedCreateBatchButton():
    if(exists("1648432899460.png")!="null"):
        print("\'Create Batch\' button is present")
        assert True
    else:
       print("\'Create Batch\' button is NOT present")
       assert False
                    
def verifyJobNameInDropDown(nameOfTheJob):
    global jobNameCopied

    click("1648433759871.png")
    type(Key.DOWN)
    type(Key.ESC)
    
    #Copy the job name already selected
    type("c", KEY_CTRL)
    jobNameCopied = Env.getClipboard()

    #Compare the job name copied 
    if (jobNameCopied == nameOfTheJob):
       print ("Loaded job is displayed in the \'Batch\' drop-down")
       assert True
    else:
       print ("Loaded job is NOT displayed in the \'Batch\' drop-down")
       assert False   

def verifyActiveBinIcon():
    if(exists("1648431514091.png")!="null"):
        print("Active red bin icon is present")
        assert True
    else:
       print("Active red bin icon is NOT present")
       assert False

def verifyUpdateBatchButton():
    if(exists("1648431599204.png")!="null"):
        print("\'Update Batch\' button is present")
        assert True
    else:
       print("\'Update Batch\' button is NOT present")
       assert False

def verifyCreateNewText():
    global createNewTextCopied
    global createNewText
    click("1648433759871.png")
    type(Key.UP)
    type(Key.ESC)
    
    #Copy 'Create New' text from the text field
    type("c", KEY_CTRL)
    createNewTextCopied = Env.getClipboard()

    #Compare the job name copied 
    if (createNewTextCopied == createNewText):
       print("\'Create New\' is displayed in the \'Batch\' drop-down")
       assert True
    else:
       print("\'Create New\' is NOT displayed in the \'Batch\' drop-down")
       assert False

def verifyGreyedBinIconAgain():
    if(exists("1648431088726.png")!="null"):
        print("Greyed-out bin icon is present again")
        assert True
    else:
       print("Greyed-out bin icon is NOT present again")
       assert False

def verifyActiveCreateBatchButton(): 
    if(exists("1648433870545.png")!="null"):
        print("Active \'Create Batch\' button is present")
        assert True
    else:
       print("Active \'Create Batch\' button is NOT present")
       assert False


#####################

verifyJobLoaded("TR~RF-00178~1")
verifyCurrentBatchDropDown("TR~RF-00178~1")
    
    
    






    


