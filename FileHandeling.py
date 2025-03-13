import GenerateResults
import GUI

def save(Results: str, name: str):
    '''
    takes in the results and the user name; the puts inside of a text file the results and the name of the user in this order
    1: name
    2: results

    perameters
    ----------
        Results : str
            a array of results contaning 3 letters corisponding if they got there input currect; wrong; or they ran out of time
        name : str
            a name for which the user shuld enter to save there results under
    
    return
    ------
        this code returns nothing

    examples
    --------
    >>> save(("C","W","T"), John)

    >>> save(("T","W","W"), Eli)
    '''
    f = open("results.txt", "a") # saveing the result
    f.write(name)
    f.write("\n")
    f.write(f"{Results}")
    f.write("\n")
    f.close()
    return

import sys
def read(UserInput) -> str:
    '''
    reads thrue a file and checks if the username of the file matches with the inputed user name

    perameters
    ----------
        UserInput : str
            the user name that shuld be serched thrue the text file
    
    return
    ------
        str: an array contning the number of times this user name has been found isnide of the code

    examples
    --------
    examples are dependent on situation
    >>> read(John)
    ("John")

    >>> read(k)
    ("k","k","k")
    '''
    CurrentLineNumber = 0
    resuts = []
    try: # reading thrue the results and see if there is any input like the user input
        with open("results.txt", "r") as f:
            for line in f:
                CurrentLineNumber += 1
                if CurrentLineNumber % 2 != 0:
                    if UserInput.strip() == line.strip():
                        resuts.append(line.strip())
    except: # if the file dose not exsist
        GUI.error("The file dose not exsist; becuase no tests were saved")
        pass
        return "FILENOTFOUND"
    return resuts

def readWithQurry(UserInput: str, Qurrynumber: int) -> str:
    '''
    reads thrue a file and checks if the username of the file matches with the inputed user name
    if so increments untill the qurry number is the same; then goes to the next line in the text file, converts it into an array, and returns the array

    perameters
    ----------
        UserInput : str
            the user name that shuld be serched thrue the text file
        Qurrynumber : int
            the number requierd to check if itsright
    
    return
    ------
        str: an array continng the resuts for that quiz

    examples
    --------
    examples are dependent on situation
    >>> read(John, 1)
    ("C","C","W")

    >>> read("k", 2)
    ("W","C","T")
    '''
    CurrentLineNumber = 0
    NumbersUntillQurryMet = 0
    nextResult = False 
    with open("results.txt", "r") as f: # reads thrue the file and checks if the qurry number is like the function numebr
        for line in f:
            CurrentLineNumber += 1
            if CurrentLineNumber % 2 != 0:
                if UserInput.strip() == line.strip():
                    NumbersUntillQurryMet += 1 # adds one and sees if this is the result the user wanted to see
                    if Qurrynumber == NumbersUntillQurryMet:
                        nextResult = True
            elif nextResult == True:
                print(line.strip()) # strips the spaces; and runs it thrue a function and convert it into an array
                Output = GenerateResults.rearray(line.strip())
                return Output       