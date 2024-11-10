#You can import any required modules here
import os

#This can be anything you want
moduleName = "cambia"

#All of the words must be heard in order for this module to be executed
commandWords = ["cambia"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
    dataMessage = command.split(' ',2)
    comando = dataMessage[0]
    argumento = dataMessage[1]
    print("comando: ",comando)
    print("argumento: ",argumento)
    string_command = "mosquitto_pub -t cambia -m "
    string_command = string_command + argumento
    print(string_command)
    os.system(string_command)
    #return

