'''
Purpose: The purpose is to create an integration solutions python module class

Date: July 2024

Created by: Graham MacGregor Integration Solutions

Arguments:

Assumptions: That necessary python modules will be called in main script

Version: Python 3

Classes
-----------

Revisions or Changes
Date, Who
Description

'''

class Variable_Secrets:


    def __init__(self, inSecretsFile, variableRequired = None, userRequired = None, passwordRequired = None, driveNeeded = None):#, boundarySource):
        self.inSecretsFile = inSecretsFile
        self.variableRequired = variableRequired
        self.userRequired = userRequired
        self.passwordRequired = passwordRequired
        self.driveNeeded = driveNeeded

    def UseConfigparser(self):
        import configparser
        config = configparser.ConfigParser()
        config.read(self.inSecretsFile)
        returnUser = config[self.variableRequired][self.userRequired]
        returnPassword = config[self.variableRequired][self.passwordRequired]
        returnDrive = config[self.variableRequired][self.driveNeeded]
        print (returnUser)
        print (returnPassword)
        print (returnDrive)


        