
from sikuli import *
import HTMLTestRunner
#myScriptPath = "C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test\\ Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation"

jobName = ""

print getImagePath()
resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
print getImagePath()

##path = "C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\SikuliX\\My Tests\\MultiControlAutomation\\Images\\"

##addImagePath(path)


#click(""+aa+"1639535107506.png")
#click(getImagePath()[1]+"\\"+"1639535107506.png")
#click("C:\Users\dilitha.vithanage\Downloads\Multinail Test Work\Test Automation\SikuliX\My Tests\MultiControlAutomation\Images\1639535107506.png")


import OpenMultiControl
reload(OpenMultiControl)
OpenMultiControl.openMultiControl()

print("Image path before import LoadJob Job is : ")
print(getImagePath())

import LoadJob

print("Image path after import LoadJob Job is : ")
print(getImagePath())

reload(LoadJob)

print("Image path after reload LoadJob Job is : ")
print(getImagePath())

jobName = LoadJob.loadTheJobFirst()

addImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\OpenMultiControl.sikuli")
addImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\LoadJob.sikuli")

print("Image path before SECOND import of LoadJob Job is : ")
print(getImagePath())

import LoadJob

print("Image path after SECOND import of LoadJob Job is : ")
print(getImagePath())

reload(LoadJob)

print("Image path after SECOND reload LoadJob Job is : ")
print(getImagePath())


LoadJob.verifyJobLoaded(jobName)

#print("Image path after LoadJob.verifyJobLoaded is : ")
#print(getImagePath())