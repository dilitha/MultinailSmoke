from sikuli import *

jobName = ""

def verifyJobIsAlreadyLoaded():
    import shutil
   
    alreadyLoadedJobSection = ""
    alreadyLoadedJobSplitted = ""
    alreadyLoadedJobWithCheckbox = ""
    alreadyLoadedJob = ""

    #Please note that we have already added the job TR~RF-00180~1 in the 'LoadJob.py' file
    #the exists part was added because, find failed error was displayed otherwise.
    if exists("1647233108239.png"): 
        alreadyLoadedJobSection = find("1647233108239.png").text() 
        print("Job is already loaded !!!!")
        

        alreadyLoadedJobSplitted = alreadyLoadedJobSection.split("\n", 1)
    
    
        print alreadyLoadedJobSplitted
        
        alreadyLoadedJobWithCheckbox = alreadyLoadedJobSplitted[1]
        print alreadyLoadedJobWithCheckbox
        
        alreadyLoadedJobCheckboxAndJob = alreadyLoadedJobWithCheckbox.split(" ",1)
        alreadyLoadedJob = alreadyLoadedJobCheckboxAndJob[1]
    
        print ("Already loaded job is : " + alreadyLoadedJob)

        assert True
    else:
        print("A job is not loaded yet")
        alreadyLoadedJob = ""
        assert False

    print("Image path when quitting verifyJobIsAlreadyLoaded is : ")
    print(getImagePath())


    #This job name is sent to the main program so that it will be passed to the next method to delete the job
    return alreadyLoadedJob

def deleteJob(nameOfTheJobToBeDeleted):

    print("Job passed in is : " + nameOfTheJobToBeDeleted)
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    if nameOfTheJobToBeDeleted == "":
        print("Job passed in is null !!!")
        assert False
        return

 
    jobToBeDeletedSplitted = ""
    jobToBeDeletedWithCheckbox = ""
    loadedJobsTextCheckBoxAndJobName = ""
    checkBoxAndJobName = ""
    actualJobName = ""
    
    print("Image path in deleteJob is : ")
    print(getImagePath())

    print("Bundle path in deleteJob is : ")
    print(getBundlePath())

    #the exists part was added because, find failed error was displayed otherwise.
    if exists(Pattern("1647233108239.png").similar(0.80)): 
        jobToBeDeletedSplitted = find("1647233108239.png").text()
    
        print("Image Found !!!!")
        print("Image text is: " + jobToBeDeletedSplitted)

        #Following part will split 'Loaded Jobs' and '[] JobName'
        loadedJobsTextCheckBoxAndJobName = jobToBeDeletedSplitted.split("\n", 1)
        print(loadedJobsTextCheckBoxAndJobName)

        #Following part will split '[]' and 'JobName'
        checkBoxAndJobName = loadedJobsTextCheckBoxAndJobName[1].split(" ", 1)
        print(checkBoxAndJobName)

        #Following is where the actual job name is extracted
        actualJobName = checkBoxAndJobName[1]
        print(actualJobName)
    
        #Click on the job name to delete
        click("1647572621589.png")
    
        #No need to perform the following action. Check box will be selected when clicked on the job name
        #type(Key.RIGHT + Key.SPACE)

        #click on the 'Delete' button
        click("1647567182720.png")

        print ("The job deleted is : " + actualJobName)
        

        assert True

    else:
        print("A job is not deleted")
        actualJobName = ""
        assert False

    #This job name is sent to the main program so that it will be passed to the next method to compare the displaying of
    #the deleted job in the 'Available Jobs' section
    return actualJobName

def verifyTheJobIsDeleted(nameOfTheJobJustDeleted):
    import shutil
    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")

    emptyLoadedJobsSection = ""
    loadedJobsSplitted = ""
    availableJobsSection = ""
    availableJobsSplitted = ""
    alreadyLoadedJobWithCheckbox = ""
    alreadyLoadedJob = ""
    
    #the exists part was added because, find failed error was displayed otherwise.
    if exists("1647576358827.png"): 
        emptyLoadedJobsSection = find("1647576358827.png").text() 
        print ("Text displayed in the Loaded Jobs section is: " + emptyLoadedJobsSection)
        
        #Verify that 'Loaded Jobs' is the only text in the image
        loadedJobsSplitted = emptyLoadedJobsSection.split("\n", 1)

        #No jobs should be displayed under 'Loaded Jobs'. Hence, the only text in the section should be "Loaded Jobs"
        loadedJobsSplittedlength = len(loadedJobsSplitted)
        print loadedJobsSplittedlength

        assert loadedJobsSplittedlength == 1, "Loaded Jobs section is NOT empty"


        assert True
    else:
        print("Loaded Jobs section is not displayed")
        assert False

    #Verify that Current Batch drop down menu has the text Current Batch displayed
    if exists("CurrentBatchDropdownEmpty.png"):
        print("Batch name is removed from the Current Batch drop down in the home page")
        assert True
    else:
        print("Batch name is NOT removed from the Current Batch drop down in the home page")
        assert False 


###
def verifyTheDeletedJobIsReturned(nameOfTheJobJustDeleted):
    #import Env
    import os.path
    import shutil
    #jobDeleted = "TR~RF-00178~1"
    #jobDeleted = "TR~RF-00180~1"
    jobDeleted = nameOfTheJobJustDeleted
    #jobDeleted = "FR~RAKERS~11"

    #Delete this variable after debugging
    testCounter = 0

    firstJobInAvailableJobs = True
    isDeletedJobFound = False

    #To track whether the scroller is in the bottom of the list in 'Available Jobs' section
    scrollerInBottom = False

    #Base name for the captured screenshot image of each job in 'Available Jobs' section
    baseScreenshotName = "Available_Job_Captured"

    #Actual screenshot name for each captured job name portion from 'Available Jobs' section
    jobScreenshotName = ""

    #This is to check whether there are unchecked check boxes available under 'Available Jobs' section
    jobsPresentInAvailableJobs = True
    
    #This is to decide the screenshot name for each job text extracted.
    #Also, this tracks which job is currently considered in the 'Available Jobs' section.
    jobNumberInAvailableJobs = 1

    print("Job passed in is: " + jobDeleted)

    #This is the start of the comparing job names
    click("1647821813877.png")
    mouseMove(-50, 0)

    '''
    if exists("1647822505043.png"):
        print("At the very first job")
        jobsPresentInAvailableJobs = True
    else:
        print("Lighter check box is not present. Checking for the darker check box...")

    if exists("1647836634685.png"):
        print("At a job other than the very first job")
        jobsPresentInAvailableJobs = True
    else:
        jobsPresentInAvailableJobs = False
        print("Darker check box is not present.")

        #Add a break statement later
    '''

    while jobsPresentInAvailableJobs == True:

        ################################
        #Delete this portion after debugging
        testCounter += 1
        if testCounter == 7:
            break

        ###############################
        
        if jobNumberInAvailableJobs == 1:
        
            #Still at the first job in the 'Available Jobs' section. So, the check box will be in lighter colour when highlighted.
            #click on the lighter check box
            click("1647822505043.png")
            print("Clicked on the very first job")
        else:
            #After the first job, check boxes will be in darker colour when highlighted.
            #click on the darker check box
            click("1647836634685.png")
            print("Clicked on a job OTHER THAN very first job")

        wait(0.75)
        
        print(Env.getMouseLocation())
        x = Env.getMouseLocation().getX()
        y = Env.getMouseLocation().getY()
        print("Mouse coordinates soon after checking the checkbox")
        print (x)
        print (y)

        #Following line is the one used before addressing the job 00180 capturing issue.
        #Capture the job name part
        #captured = capture(x+25, y-10, 215, 20)
        #####################
        #Following 9 lines were added because sometimes the job 00180 was not captured.
        #Now, the mouse will move little bit to the right after clicking the checkbox before capturing the screenshot of the job.
        mouseMove(+25, 0)
        print(Env.getMouseLocation())
        a = Env.getMouseLocation().getX()
        b = Env.getMouseLocation().getY()
        print("---")
        print("Mouse coordinates after moving slightly to the right side")
        print (a)
        print (b)
        captured = capture(a, b-10, 215, 20)
        #####################
        print captured
        print getBundlePath()

        #Name of the job screenshot which will be moved shortly to the 'Captured' folder
        jobScreenshotName = baseScreenshotName + str(jobNumberInAvailableJobs) + ".png"

        
        #Move the captured image away from the temp folder
        shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + jobScreenshotName))
        #shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + jobScreenshotName + ".png"))

        print jobNumberInAvailableJobs

        jobNumberInAvailableJobs += 1 
        
               
    
        #Compare the job name with the deleted job
        currentJobName = find(getBundlePath()+"./temp/"+jobScreenshotName).text()
        #currentJobName = find("Captured1.png").text()
        print currentJobName

        print("jobDeleted is: " + jobDeleted)
    
        #If equal, return
        if currentJobName == jobDeleted:
            print("Deleted job IS FOUND under Available Jobs")
            #reload()
            #Delete the captured job name screenshot
            #os.remove(' '.join(getImagePath())+"\\Captured1.png")
            #assert True

            #Mark that the deleted job is found under 'Available Jobs' section
            isDeletedJobFound = True

            #To go out of the While loop
            jobsPresentInAvailableJobs = False

            
        #If not equal, move to the next job 
        else:
            if scrollerInBottom == True:
                print("Scroller is in the bottom. Checking whether this job is the matching job.")

                ####################################################################################
                
                #Check for the last job
                #Then exit the While loop

                click("1647836634685.png")
                print("Clicked on the check box at the VERY BOTTOM")

                print(Env.getMouseLocation())
                x = Env.getMouseLocation().getX()
                y = Env.getMouseLocation().getY()
                print (x)
                print (y)
        
                #Capture the job name part
                captured = capture(x+25, y-10, 215, 20)
                print captured
                print getBundlePath()
        
                #Name of the job screenshot which will be moved shortly to the 'Captured' folder
                jobScreenshotName = baseScreenshotName + str(jobNumberInAvailableJobs) + ".png"
        
                
                #Move the captured image away from the temp folder
                shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + jobScreenshotName))
                #shutil.move(captured, os.path.join(getBundlePath(), "./temp/" + jobScreenshotName + ".png"))
        
                print jobNumberInAvailableJobs
        
                jobNumberInAvailableJobs += 1 
                
                       
            
                #Compare the job name with the deleted job
                currentJobName = find(getBundlePath()+"./temp/"+jobScreenshotName).text()
                #currentJobName = find("Captured1.png").text()
                print currentJobName

                #Compare the job name with the deleted job
                currentJobName = find(getBundlePath()+"./temp/"+jobScreenshotName).text()
                #currentJobName = find("Captured1.png").text()
                print currentJobName
            
                #If equal, return
                if currentJobName == jobDeleted:
                    print("Matching job was found in the Available Jobs section. <Inside the If statement>")
                    #reload()
                    #Delete the captured job name screenshot
                    #os.remove(' '.join(getImagePath())+"\\Captured1.png")
                    #assert True
        
                    #Mark that the deleted job is found under 'Available Jobs' section
                    isDeletedJobFound = True
        
                    #To go out of the While loop
                    jobsPresentInAvailableJobs = False

                else:
                    #This bottom job is also not the matching job.
                    #Have to go out of the While loop
                    print("Bottom job is also NOT the matching job.")
                    break
                
                ####################################################################################
                
                
            else:
                #Scroller is not in the bottom. Have to check for other jobs.
                print("Job NOT matched. Checking the next job.")
                #Delete the captured job name screenshot
                #os.remove(' '.join(getImagePath())+"\\Captured1.png")
                
                if firstJobInAvailableJobs == True:
                    #Very first job in the 'Available Jobs' section. Have to press the down arrow key 3 times.
                    type(Key.DOWN)
                    type(Key.DOWN)
                    type(Key.DOWN)
        
                    #The following uncheck box color is different.(Bit darker)
        
                    click("1647836634685.png")
                    print("Clicked on when scroller is not in the bottom. [Key down 3 times]")
        
                    firstJobInAvailableJobs == False
    
                else:
                    #Current job is not the very first job in the 'Available Jobs' section. 
                    #Have to press the down arrow key only 1 time.
                    type(Key.DOWN)
                    print("Clicked on when scroller is not in the bottom. [Key down 1 time]")

                    
        if exists("1647906606414.png"):
            #Scroll bar is at the very bottom. Have to exit the verification.

            #Check whether the job is already matched
            if isDeletedJobFound == True:
                #Matching job was found at the bottom of the list
                print("Delete job was found at the bottom of the list")

                #To go out of the While loop
                jobsPresentInAvailableJobs = False
            else:
                #At the bottom of the list. But the matching job is still not found.
                #Should check for the last remaining job.
                scrollerInBottom = True
                

    #Following statements are out of the While loop         
    if isDeletedJobFound == True:
        print ("Deleted job was FOUND under Available Jobs <Outside the While statement>")

        #Delete the screenshots of job names
        import os
        yourFilePath = os.path.join(getBundlePath(), "./temp/")
        files = os.listdir(yourFilePath)
        for f in files:
            os.remove(yourFilePath + f)

        assert True
    else:
        print("Deleted job NOT found under Available Jobs  <Outside the While statement>")
        assert False






    


