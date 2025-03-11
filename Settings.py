import GUI
from colorama import Fore, Back, Style # colors for the colsul
from colorama import init
init(autoreset=True) # automaticly reset the color after each line
import sys
import quastions

def QuizSelection() -> dict | int | int:
    '''
    Goes into the main setting menu which lets you change multipull peramiters
    you can change the which question set is seleted; the ammount of time untill the exam ends; and also the number of questions

    peramters
    ---------
        there are no input peramters inside of this function

    Return
    ------
        dict
            containing the set of questions that the user wanted insdie of there code
        int
            containing the number of questions that the user wants to go threu
        int
            containing the ammount of time; in seconds; for how long the quiz shuld run for

    Examples
    --------
    >>> QuizSelection()
        Q 1,2
        S 400
        N 12
    Dictunary contaning the quiz of math and computer science combined, 12, 400

    >>> QuizSelection()
        Q 3
        N 4
        S 20
    Dictunary contaning the quiz of history, 4, 20

    '''
    MathQuestions = False
    ComputerSceinceQuestions = False
    HistoryQuestions = False
    timechange = False
    quastionchange = False
    time = 5
    NumberOfQuestions = 3
    Quiz = {}
    returnQuiz = {}
    while True:
        GUI.clearConsole()
        GUI.InputUI(2, 2, 1)
        print("enter the letter Q and the number on which quiz you wish to add to the question pool")
        print("to add multipull add a comma between selection (e.g., Q1,2)")
        if MathQuestions == True:
            print(Fore.GREEN+ f"(1) Math Questions")
        else:
            print(Fore.BLACK+ f"(1) Math Questions")

        if ComputerSceinceQuestions == True:
            print(Fore.GREEN+ f"(2) Computer Science Questions")
        else:
            print(Fore.BLACK+ f"(2) Computer Science Questions")

        if HistoryQuestions == True:
            print(Fore.GREEN+ f"(3) History Questions")
        else:
            print(Fore.BLACK+ f"(3) History Questions")
        print("-----------------------------")
        if timechange == True:
            print(Fore.GREEN+ f"(S) edit time in seconds (e.g., S 40); its currently set to {time}s")
        else:
            print(Fore.BLACK+ f"(S) edit time in seconds (e.g., S 40); its currently set to {time}s")
        if quastionchange == True:
            print(Fore.GREEN+ f"(N) number of questions that shuld be quized on (e.g., N 9); between 1 and {Quiz.__len__()}; it is currently set to {NumberOfQuestions} question(s)")
        else:
            print(Fore.BLACK+ f"(N) number of questions that shuld be quized on (e.g., N 9); between 1 and {Quiz.__len__()}; it is currently set to {NumberOfQuestions} question(s)")
        print("-----------------------------")
        print("to exit the porgram type (EXIT), or 0")
        if returnQuiz.__len__() != 0 and int(NumberOfQuestions) >= 0 and int(NumberOfQuestions) <= Quiz.__len__() and time >= 0:
            print(Fore.GREEN+ f"to go to the next step type (NEXT, or 1)")
        else:
            print(Fore.RED+ f"to go to the next step type (NEXT, or 1)")
        GUI.InputUI(2, 2, 2)
        timechange = False
        quastionchange = False
        UserInput = input("Input: ")
        if UserInput[0] == "Q" or UserInput[0] == "q":
            try:
                value = UserInput[1:]
                MathQuestions = False
                ComputerSceinceQuestions = False
                HistoryQuestions = False
                Quiz = {}
                for i in value.split(","):
                    if i == "1" or i == " 1":
                        MathQuestions = True
                        Quiz = Quiz | quastions.mathQuastion().copy()
                    elif i == "2" or i == " 2":
                        ComputerSceinceQuestions = True
                        Quiz = Quiz | quastions.computerScienceQuastion().copy()
                    elif i == "3" or i == " 3":
                        HistoryQuestions = True
                        Quiz = Quiz | quastions.historyQuastion().copy()
                    else:
                        GUI.error(f"ERROR: input of 'Q' function was not readable; expected 1,2,3 recived: {i}; EXAMPLE Q 1,2")
                returnQuiz = {i: Quiz[key] for i, key in enumerate(Quiz.keys(), 1)} # changes the keys to still be in order from 1 to n
            except:
                GUI.error(f"ERROR: input of 'Q' function was not readable; EXAMPLE Q 1,2")
                pass

        elif UserInput[0] == "N" or UserInput[0] == "n":
            value = UserInput[1:]
            try:
                if int(value) >= 1 and int(value) <= Quiz.__len__():
                    NumberOfQuestions = int(value)
                    quastionchange = True
                else:
                    GUI.error(f"ERROR: input of 'N' function was not revicing a valid input; expected number between 1 and {Quiz.__len__()}; recived {value}; EXAMPLE N 9")
            except:
                GUI.error(f"ERROR: input of 'N' function was not readable; EXAMPLE N 9")
                pass

        elif UserInput[0] == "S" or UserInput[0] == "s":
            try:
                value = UserInput[1:]
                if int(value) >= 0:
                    time = int(value)
                    timechange = True
                else:
                    GUI.error(f"ERROR: input of 'S' function was not revicing a valid input; expected number above 0; recived {value}; EXAMPLE S 20")
            except:
                pass
                GUI.error(f"ERROR: input of 'S' function was not readable; EXAMPLE S 20")
        elif UserInput == "EXIT" or UserInput == "0":
            GUI.clearConsole()
            sys.exit()
        elif UserInput == "NEXT" or UserInput == "next" or UserInput == "1":
            GUI.clearConsole()
            if returnQuiz.__len__() != 0 and int(NumberOfQuestions) >= 0 and int(NumberOfQuestions) <= Quiz.__len__() and time >= 0:
                return returnQuiz, NumberOfQuestions, time
        else:
            GUI.error(f"value {UserInput} is not recognised")
            
def Selection() -> int:
    '''
    this is the main menu
    it lets the user chose between compleating a quiz and also look thrue results
    returns that value

    perameters
    ----------
    there are no peramiters for this function
    
    return
    ------
        int
            the number (1, 2) depending on what the user selecetd; or if the user seleced 0; exit the code

    examples
    --------
    >>> Selection()
        2
    2

    >>> Selection()
        EXIT
    '''
    while True:
        GUI.clearConsole()
        GUI.InputUI(1, 2, 1)
        print("Select one of the three options")
        print("(1) go and compelat a quiz")
        print("(2) look thrue results")
        print("to exit the porgram type (EXIT) or (0)")
        GUI.InputUI(1, 2, 2)
        UserInput = input("Input: ")
        if UserInput == "1":
            return 1
        if UserInput == "2":
            return 2
        if UserInput == "EXIT" or UserInput == "0":
            GUI.clearConsole()
            sys.exit()

def SaveSelection() -> int:
    '''
    this is the menu to save a resut to a file
    it lets the user chose between saveing and gowing back to the menu, just gowing back to the menu; or exiting the code
    returns that value

    perameters
    ----------
    there are no peramiters for this function
    
    return
    ------
        int
            the number (1, 2) depending on what the user selecetd; or if the user seleced 0; exit the code

    examples
    --------
    >>> Selection()
        2
    2

    >>> Selection()
        EXIT
    '''
    print("Select one of the three options")
    print("(1) exit, and go back to the  main screen")
    print("(2) exit and save to file, and back to the main screen")
    print("to exit the porgram type (EXIT) or (0)")
    print("--------------------------------------")
    while True:
        UserInput = input("Input: ")
        if UserInput == "1":
            return 1
        if UserInput == "2":
            return 2
        if UserInput == "EXIT" or UserInput == "0":
            GUI.clearConsole()
            sys.exit()

def pastResultSelection(Results: str)-> int:
    GUI.clearConsole()
    if Results.__len__() == 0:
        GUI.error("No results found")
        return 0
    while True:
        number = 0
        GUI.clearConsole()
        GUI.InputUI(2, 2, 1)
        print(" Hear are the resuts from your quorry")
        for i in Results:
            number += 1
            print(f"{number}: {i}")
        GUI.InputUI(2, 2, 2)
        UserInput = input(f"put in which result you wish to check between 1 and {Results.__len__()}: ")
        try:
            if int(UserInput) >= 1 and int(UserInput) <= Results.__len__():
                return int(UserInput)
        except:
            pass