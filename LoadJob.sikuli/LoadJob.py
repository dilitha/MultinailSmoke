from sikuli import *

jobName = ""
loadedJobsSection = ""
loadedJobsSplitted = ""


def loadTheJobFirst():
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    print("Image path in loadTheJobFirst is : ")
    print(getImagePath())
    
    print("Bundle path in loadTheJobFirst is : ")
    print(getBundlePath())
    
    
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    #print("Image path AGAIN in loadTheJobFirst is : ")
    #print(getImagePath())

    #addImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\OpenMultiControl.sikuli")
    #addImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\LoadJob.sikuli")
    #addImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\UnitTestExample.sikuli")

    print ("Looping the imagePath")
    imgPath = list(getImagePath()) # makes it a Python list
    # to loop through
    for p in imgPath:
        print p

    #We are loading the job TR~RF-00180~1
    #the exists part was added because, find failed error was displayed otherwise.
    if exists("1647225026050.png"): a = find("1647225026050.png").text()
    #a = find("1647225026050.png").text()
    
    print("Image Found !!!!")
    print("Image text is: " + a)
    b = a.split(" ", 1)

    #This is the job which will be loaded
    jobLoaded = b[1]
    print (jobLoaded)
    click("1647225026050.png")
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
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    print("Image path in verifyJobLoaded is : ")
    print(getImagePath())

    print("Bundle path in verifyJobLoaded is : ")
    print(getBundlePath())


    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    print("Image path AGAIN in verifyJobLoaded is : ")
    print(getImagePath())

    wait(1)

    if exists("1647233108239.png"): 
        loadedJobsSection = find("1647233108239.png").text() 
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






    


