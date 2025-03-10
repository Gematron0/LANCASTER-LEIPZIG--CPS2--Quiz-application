from colorama import Fore, Back, Style # colors for the colsul
from colorama import init
init(autoreset=True) # automaticly reset the color after each line
from inputimeout import inputimeout
import time
import os

### clears the concle for easey reading ###
clearConsole = lambda: os.system('cls'
    if os.name in ('nt', 'dos') else 'clear')

### inputs the UI to let the person input some numbers ###
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
    if Part == 1:
        while i != totInputsFrunt - 1:
            i = i + 1
            print (Fore.BLACK+">",i,Fore.BLACK+"-------------------------------")
        print (Fore.YELLOW+"<",totInputsFrunt,Fore.YELLOW+"-------------------------------")
        i = 0
        return
    
    if Part == 2:
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
    start = time.time()
    try: 
        print(f"you have {int(RemainingTime.__round__(0))}s remaining")
        Answer = inputimeout(prompt='input: ', timeout=RemainingTime)
        Answer = Answer.upper()
        end = time.time()
        timeTaken = end-start
        RemainingTime = RemainingTime - timeTaken

        if Answer == "1":
            Answer = "A"
        if Answer == "2":
            Answer = "B"
        if Answer == "3":
            Answer = "C"
        if Answer == "4":
            Answer = "D"

        IsAResult = False
        for i in PssibleValues:
            if i == Answer:
                IsAResult = True
        if IsAResult == True:
            return Answer, RemainingTime
        else:
            return "WRONG", RemainingTime

    except Exception:
        print("time has ended")
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
    for t in results:
        if t == "C":
            print (Fore.GREEN+"(+)",questionNumber,"",Fore.GREEN+"-------------------------------")
        elif t == "W":
            print (Fore.RED+"(-)",questionNumber,"",Fore.RED+"-------------------------------")
        elif t == "T":
            print (Fore.YELLOW+"(~)",questionNumber,"",Fore.YELLOW+"-------------------------------")
        questionNumber += 1