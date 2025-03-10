import GenerateResults

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
    f = open("results.txt", "a")
    f.write(name)
    f.write("\n")
    f.write(f"{Results}")
    f.write("\n")
    f.close()
    return

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
    with open("results.txt", "r") as f:
        for line in f:
            CurrentLineNumber += 1
            if CurrentLineNumber % 2 != 0:
                if UserInput.strip() == line.strip():
                    resuts.append(line.strip())
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
    with open("results.txt", "r") as f:
        for line in f:
            CurrentLineNumber += 1
            if CurrentLineNumber % 2 != 0:
                if UserInput.strip() == line.strip():
                    NumbersUntillQurryMet += 1
                    if Qurrynumber == NumbersUntillQurryMet:
                        nextResult = True
            elif nextResult == True:
                print(line.strip())
                Output = GenerateResults.rearray(line.strip())
                return Output       