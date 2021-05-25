# Dependencies
import os
import fitz
import pyttsx3
from colorama import Fore, init

# Global Var
strPDF = ""
engine = ""

# Get input from User
def gInUs():

    global strPDF

    # Print input
    print(Fore.GREEN + "[!] Insert path to PDF file:" + Fore.RESET)
    inputUser = input()
    # -------------

    # Print an alert if input is not valid, if not, call to fun reDoc
    if(inputUser == "" or len(inputUser.split("\\"))  == 1):
        print(Fore.RED + "Please put a valid PATH to a file" + Fore.RESET)
    else:
        reDoc(inputUser)
    # -------------

# Fun reDoc, read and extract text from PDF file, then call to fun reStr
def reDoc(strFile):
    # Global var
    global strPDF
    # -------------

    # Extract text
    fileObj = fitz.open(strFile)
    for page in fileObj:
        strPDF += page.get_text("text")
    print(Fore.GREEN + "[!] Init engine text to speech pyttsx3"+ Fore.RESET)
    reStr(strPDF)
    # -------------

# Fun reStr that read the text from string strPDF
def reStr(strRead):
    global engine

    # Init engine
    engine = pyttsx3.init()
    engine.say(strRead)
    # -------------
    print(Fore.YELLOW + "[.] Reading"+ Fore.RESET)
    
# Call to main fun
gInUs()

# Finish engine
engine.runAndWait()
print(Fore.GREEN + "[!] Finished"+ Fore.RESET)
