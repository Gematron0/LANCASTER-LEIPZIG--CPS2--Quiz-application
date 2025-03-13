from colorama import Fore, Back, Style # colors for the colsul
from colorama import init
init(autoreset=True) # automaticly reset the color after each line
from inputimeout import inputimeout
import time
import os

clearConsole = lambda: os.system('cls'
    '''
    clears the consol

    peramiters
    ----------
        What version are you using (wondows, linux, ext)

    return
    ------
    there is no return for this file

    examples
    --------
    clearConsole()

    '''
    if os.name in ('nt', 'dos') else 'clear') # clears the consul

def error(messege):
    clearConsole()
    print(Fore.BLACK+Back.YELLOW+f"{messege}") # prints out the error messege; usualy the user put an incurrect value
    print(Fore.BLACK+Back.YELLOW+f"programm will go back in 3 seconds")
    time.sleep(3)
    clearConsole()

def InputUI(totInputsFrunt: int, TotInputsBack: int, Part: int):
    '''
    this dose ui stuff
    takes the number of inputs and outputs and displayes some UI accordingly; the part is for befor or after the prompt
    if part is 1 then its befor the prompt; if its 2 then its after the promps

    peramiters
    ----------
        totInputsFrunt : int
            the number of input that is put infrunt of the prompts

        TotInputsBack : int
            the number of input that is put behind of the prompts

        part : int
            checks if its displaying befor or after the prompt

    return
    ------
    there is no return for this file

    examples
    --------
    InputUI(1, 3, 1)

    InputUI(1, 3, 2)

    '''
    i = 0
    if Part == 1: # the ui befor a question gets asked
        while i != totInputsFrunt - 1:
            i = i + 1
            print (Fore.BLACK+">",i,Fore.BLACK+"-------------------------------")
        print (Fore.YELLOW+"<",totInputsFrunt,Fore.YELLOW+"-------------------------------")
        i = 0
        return
    
    if Part == 2: # the ui after a question is asked
        i = totInputsFrunt
        while i != TotInputsBack:
            i = i + 1
            print (Fore.BLACK+">",i,Fore.BLACK+"-------------------------------")
        i = 0
        return
    
def input(RemainingTime: int, PssibleValues: str) -> str | int:
    '''
    takes the time of the quiz remaning and also the possible values remaning
    sets a time out with the remaning time
    converts the input so its universal 
    so if input is either (a, b, c, d, A, B, C ,D , 1, 2, 3, 4) it converts it to (A, B, C, D)
    returns the input; else askes the question to be reasked

    peramiters
    ----------
        remaningTime : int
            sets up the remaning time untill the exam runs out of time

        possibleVales : str
            an array contaning all of the online values

    return
    -----
        str:
            what the ancer is or the word "TIME", if the uer runs out of time, or "WRONG" if the user input isnt right and the question must be reprnted
        int:
            the remaning time for the quiz

    examples
    --------
    InputUI(20, ("A","B","C","D"))

    InputUI(70, ("A","B","C","D"))
    
    '''
    print (Fore.BLUE+"=========================")
    start = time.time() # set the time
    try: 
        print(f"you have {int(RemainingTime.__round__(0))}s remaining")
        Answer = inputimeout(prompt='input: ', timeout=RemainingTime) # adding a timeout with the remaning ammout of time
        end = time.time() # getting the end time
        Answer = Answer.upper()
        timeTaken = end-start # calculating the remaining time for the quiz
        RemainingTime = RemainingTime - timeTaken

        if Answer == "1": # convering intergers to there althebetical corispondent
            Answer = "A"
        if Answer == "2":
            Answer = "B"
        if Answer == "3":
            Answer = "C"
        if Answer == "4":
            Answer = "D"

        IsAResult = False # checking if the result is an A B C or D; else resting the question
        for i in PssibleValues:
            if i == Answer:
                IsAResult = True
        if IsAResult == True:
            return Answer, RemainingTime
        else:
            return "WRONG", RemainingTime

    except Exception: # the time ran out so it would just send the user to the results
        error(f"Time has endded")
        RemainingTime = 0
        return "TIME", RemainingTime
    
def dispayResults(results: str):
    '''
    takes the input of the results and dose some ui things with it

    peramiters
    ----------
        results : int
            the resuts from the quiz as an array conting entiher "C", "W", or "T"

    return
    ------
    this function returns nothing

    example:
    >>> dispayResults(("C","W","T")):

    >>> dispayResults(("T","W","W")):
    
    '''
    questionNumber = 1
    for t in results: # goes thrue the result array and check the question was right or wrong; then displays it to the user
        if t == "C":
            print (Fore.GREEN+"(+)",questionNumber,"",Fore.GREEN+"-------------------------------")
        elif t == "W":
            print (Fore.RED+"(-)",questionNumber,"",Fore.RED+"-------------------------------")
        elif t == "T":
            print (Fore.YELLOW+"(~)",questionNumber,"",Fore.YELLOW+"-------------------------------")
        questionNumber += 1