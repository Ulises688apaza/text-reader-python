# Dependencies
import os
import fitz
import pyttsx3
from colorama import Fore, init

# Global Var
strPDF = ""

# Get input from User
def gInUs():
    global strPDF
    fileObj = ""
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

    # Extract text
    fileObj = fitz.open(strFile)
    for page in fileObj:
        strPDF += page.get_text("text")
    reStr(strPDF)
    # -------------

# Fun reStr that read the text from string strPDF
def reStr(strRead):
    engine = pyttsx3.init()

    engine.say(strRead)
    engine.runAndWait()

# Call to main fun
gInUs()