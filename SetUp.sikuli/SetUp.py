from sikuli import *
import os
import shutil
import ConfigParser
import logging
import SettingFolders #This is to read different folder names for different types of settings
import LayoutFolders #This is to read different folder names for different types of layouts

configFileLocation = "" #Location of the Config.ini file
settingFilesType = "default" #This indidates that the basic settings files are used
layoutFilesType = "default" #This indidates that the basic layout files are used

class SetUp:
    #This is the constructor of the SetUp class. 
    #It does all the initialisation tasks by calling local methods of the class.
    #When calling the constructor, 'settingsTypePassed' should be either 'default' or 'customised-<number>'
    def __init__(self, settingsTypePassed):
        print ("setUpClass __init__ method is called")

        #This is the variable which identifies whether default or customised settings should be used
        global settingFilesType
        settingFilesType = settingsTypePassed

        #Creating a local variable named setUpLogger
        #This variable will hold the handle to the logger which will be passed to local methods to log messages into the log file
        #setupLogFile() method will define the logging format, create the log file and write the very first message into it.
        self.setUpLogger = self.setupLogFile()

        #cleanFiles() method will delete relavant files before starting the test
        self.cleanFiles(self.setUpLogger)

        #Creating a local variable named 'setUpImagePath'
        #setConfig() method will set configuration values used in the project
        self.setUpImagePath = self.setConfig(self.setUpLogger)
        print ("\'imagePath\' in __init__ is: " + self.setUpImagePath)

        #Copy the 'Settings' folder into 'MultiControl' folder
        self.copySettingFiles(self.setUpLogger)

        #Copy the 'Layout' folder into 'MultiControl' folder
        self.copyLayoutFiles(self.setUpLogger)


    def setupLogFile(self):
        
        logger=logging.getLogger('')
        
        FORMAT='%(asctime)s -  [%(levelname)s] - %(message)s'
        logging.basicConfig(filename='./logs/Test_Automation_Log.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)
        logging.info('Log file initialised as a part of the set up')
    
        return logger

    #This method will perform file deletion tasks before starting tests
    def cleanFiles(self, passedInLogger):
        workDBFilePath = os.environ.get('PROGRAMDATA')+"\\MultiControl\\Work.db"
        
        #Delete the WorkDB file
        try:
           os.remove(workDBFilePath)
           print("Work DB is deleted")
           passedInLogger.info("Work DB is deleted")
        except:
           print("Error while deleting file ", workDBFilePath)
           print("Work DB deletion unsuccssful")
           passedInLogger.error("Work DB deletion unsuccssful")
    
        assert True
        
    #Copy all required setting files into the MultiControl folder
    def copySettingFiles(self, passedInLogger):
        #Global variable which will decide which settings folder to use
        global settingFilesType
        settingsFolderLocation = self.getConfig(passedInLogger)
        settingsFolderInMultiControlPath = os.environ.get('PROGRAMDATA')+"\\MultiControl\\Settings"

        print("\'settingsFolderLocation\' is: " + settingsFolderLocation)
    
        if not os.path.exists(settingsFolderInMultiControlPath):
            print("Destination does not exist")
            shutil.copytree(settingsFolderLocation, settingsFolderInMultiControlPath)
        else:
            print("Destination exists. Have to remove the folder first.")
            shutil.rmtree(settingsFolderInMultiControlPath)
            print("Destination removed. Now have to copy.")
            shutil.copytree(settingsFolderLocation, settingsFolderInMultiControlPath)
    
    def copyLayoutFiles(self, passedInLogger):
    #Purpose of this method is to copy correct layout files(OperationPage, WorkPage) into the 'Layout' folder.
    #Otherwise, tests will fail when the sizes of sections are changed because images will be different then.
    #Then, can use the Region option in Sikuli IDE (Region button at the top bar) to search for an image in a region.
    
        #Global variable which will decide which settings folder to use
        global layoutFilesType
        layoutFolderLocation = self.getLayoutFolderLocation(passedInLogger)
        layoutFolderInMultiControlPath = os.environ.get('PROGRAMDATA')+"\\MultiControl\\Layout"

        print("\'layoutFolderLocation\' is: " + layoutFolderLocation)
    
        if not os.path.exists(layoutFolderInMultiControlPath):
            print("Destination for Layout does not exist")
            shutil.copytree(layoutFolderLocation, layoutFolderInMultiControlPath)
        else:
            print("Destination Layout folder exists. Have to remove the folder first.")
            shutil.rmtree(layoutFolderInMultiControlPath)
            print("Destination Layout folder removed. Now have to copy.")
            shutil.copytree(layoutFolderLocation, layoutFolderInMultiControlPath)
    
    
    #This method will initialise config settings of the project. eg. Images folder for the project, etc.
    #Currently this method is returning only the 'imagePath'
    #If multiple values are required to be returned in future, those can be returned in the same function
    def setConfig(self, passedInLogger): 
        
        path_current_directory = os.path.dirname("__file__")

        #This is the config file which contains configuration values of the project
        path_config_file = os.path.join(path_current_directory, 'Config', 'Config.ini')

        #Write the location of the config file to the global variable
        global configFileLocation
        configFileLocation = path_config_file
        print ("Config file location is: " + configFileLocation)
        passedInLogger.info("Config file location is: " + configFileLocation)
        
        config = ConfigParser.ConfigParser()
        config.read(path_config_file)
        
           
        username = config.get('settings','username')
        password = config.get('settings','password')
        imagePath = config.get('settings','imagePath')
        
        print("Username is: " + username)
        print("Password is: " + password)
        print("Image Path is: " + imagePath)

        passedInLogger.info("Image path is set to: " + imagePath)
        
        assert True
    
        return imagePath

    #This method reads the Config.ini file and retrieves the value of 'configValueRequired' passed to this method
    #'configValueRequired' passed should be exactly the same value specified in the 'Config.ini' file
    def getConfig(self, passedInLogger):
        settingsFolder = ""
       
        #Use the global variable already set in setConfig() method
        global configFileLocation

        #Global variable storing the type of the setting. Whether it's 'default' or 'customized-<number>'
        global settingFilesType
        
        config = ConfigParser.ConfigParser()
        config.read(configFileLocation)

        print("settingFilesType is: " + settingFilesType)

        try:
            if settingFilesType == 'default':
                settingsFolder = config.get('settings', 'defaultSettingFilesPath')
                passedInLogger.info("Settings folder is: " + settingsFolder)
            else:
                settingsFolder = config.get('settings', 'customisedSettingFilesPath')
                passedInLogger.info("Settings folder is: " + settingsFolder)

        except:
            print("Settings folder could NOT be found")

        
        if settingFilesType == 'customised-1':
            print("Customised 1 line is reached")
            settingsFolder = os.path.join(settingsFolder, SettingFolders.CustomisedSettings['setting1'])
            print ("Settings folder path is: " + settingsFolder)
        else:
            if settingFilesType == 'customised-2':
                settingsFolder = os.path.join(settingsFolder, SettingFolders.CustomisedSettings['setting2'])
                print ("Settings folder path is: " + settingsFolder)
        
        assert True
        
        return settingsFolder

    
    def getLayoutFolderLocation (self, passedInLogger):
        layoutFolder = ""
       
        #Use the global variable already set in setConfig() method
        global configFileLocation

        #Global variable storing the type of the setting. Whether it's 'default' or 'customized-<number>'
        global layoutFilesType
        
        config = ConfigParser.ConfigParser()
        config.read(configFileLocation)

        print("layoutFilesType is: " + layoutFilesType)

        try:
            if layoutFilesType == 'default':
                layoutFolder = config.get('settings', 'defaultLayoutFilesPath')
                passedInLogger.info("Layout folder is: " + layoutFolder)
            else:
                layoutFolder = config.get('settings', 'customisedLayoutFilesPath')
                passedInLogger.info("Layout folder is: " + layoutFolder)

        except:
            print("Layout folder could NOT be found")

        
        if layoutFilesType == 'customised-1':
            print("Customised layout 1 line is reached")
            layoutFolder = os.path.join(layoutFolder, LayoutFolders.CustomisedLayouts['layout1'])
            print ("Layout folder path is: " + layoutFolder)
        else:
            if layoutFilesType == 'customised-2':
                layoutFolder = os.path.join(layoutFolder, LayoutFolders.CustomisedLayouts['layout2'])
                print ("Layout folder path is: " + layoutFolder)
        
        assert True
        
        return layoutFolder
    

    
    