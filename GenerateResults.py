import GUI
import Settings
import FileHandeling

def runResults(Results: str, AllowSave: bool):
    '''
    takes in the resuls displays them and ask the user if it shuld save it to a file; if yes; then saves it isnide of a file

    perameters
    ----------
        Results : str
            a array conting all of the results from the quiz

        AllowSawe : bool
            whcih checks if the user is allowed to save the resuts to the filer

    return
    ------

    examples
    --------
    >>> runResults(("C","W","T"), True)

    >>> runResults(("W","W","W"), False)

    '''
    GUI.clearConsole()
    GUI.dispayResults(Results)

    currect = 0
    wrong = 0
    for t in Results: # prints out the results of the code
        if t == "C":
            currect += 1
        elif t == "W" or t == "T":
            wrong += 1
    
    print(f"[{currect}/{wrong+currect}][{round((currect/(wrong+currect))*100, 2)}%]")
    if AllowSave == True:
        UserInput = Settings.SaveSelection()
        if UserInput == 2: # saveing system
            name = input("input a name that this attempt shuld be saved unter: ")
            FileHandeling.save(Results,name)
        return
    else:
        input("to return; press enter: ")
        return

def rearray(input: str)-> str:
    '''
    takes an input array and checks if each char is entier "C" "W" or "T"
    appends that to another array and returns

    perameters
    ----------
        input : str
            a sting of input that needs to be converted to that array
    
    return
    ------
        str
            a string array with all of the inputs
    
    examples
    --------
    >>> rearray(("C","W","T"))
    ("C","W","T")
    '''
    Output = []
    for char in input: # checks each char it saved under and converts it back to an array
        if char == "C":
            Output.append("C")
        elif char == "W":
            Output.append("W")
        elif char == "T":
            Output.append("T")
        else:
            pass
    return(Output)