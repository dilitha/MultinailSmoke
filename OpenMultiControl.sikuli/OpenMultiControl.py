from sikuli import *
import sys
def openMultiControl():
    
    import shutil

    print("Image path in OpenMultiControl is : ")
    print(getImagePath())
      
    print("Screens: ")
    print(getNumberScreens())
    print(getBundlePath())

    #Open MultiControl
    os.system(os.environ.get('LOCALAPPDATA')+"\\MultiControl\\MultiControl.Shell.exe")
    #click("1639535107506.png")
    #wait(5)

    #wait(Pattern(getImagePath()[2]+"\\"+"1639536351517.png").similar(0.6),FOREVER)
    wait("1639536351517.png", 20)
    click("1639536369814.png")
    
    click ("1639537035313.png")
    click ("1639537148021.png")
    sleep (2)
    #click ("1639537316424.png")
    type("triple0")

    #click ("1639537494670.png")
    type(Key.ENTER)
    click ("1639537622409.png")
    click ("1639537957147.png")
    click ("1644285805142.png")
   


    type(Key.ALT + Key.SPACE + "x")

    #resetImagePath("C:\\Users\\dilitha.vithanage\\Downloads\\Multinail Test Work\\Test Automation\\SikuliX\\My Tests\\MultiControlAutomation\\Images")
    
    print("Image path when quitting OpenMultiControl is : ")
    print(getImagePath())




    


