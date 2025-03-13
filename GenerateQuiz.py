import GUI
import random

def randomQuastions(Quiz: dict) -> dict | str | str | str:
    '''
    takes the input dictunary
    gets a random number between 1 and the lenth of said dictunary
    gets the question; the ancers and also the currect ancer and returns that information
    delets this question from the quiz
    renumnber the quiz from 1 to the lenth of the quiz
    returns the quiz

    Peramiters:
    -----------
        Quiz : dict
            contaning the question set that is used for the exam


    return
    ------
        dict
            contaning the remaning question set that is used for the exam
        str
            contaning the question
        str
            contaning an array with all answer
        str
            conting what the currect ancer is

    examples
    --------
    >>> Quiz contaning Math and history questions
    Quiz contaning Math and history questions -1 questaion, "Question", ("answer 1","answer 2","answer 3","answer 4"), "Currect answer"
    '''
    PossibleAnswer = []

    quastionNumber = random.randint(1, Quiz.__len__()) # grabs a random question from the question set
    QuastionsSet = Quiz[quastionNumber]

    Quastions = QuastionsSet["Quastion"] # saves it inside of an array
    PossibleAnswer.append(QuastionsSet["A"])
    PossibleAnswer.append(QuastionsSet["B"])
    PossibleAnswer.append(QuastionsSet["C"])
    PossibleAnswer.append(QuastionsSet["D"])
    Answer = QuastionsSet["Currect"]

    del Quiz[quastionNumber] # deleats the quastion dictunary so it cant be chosen again
    returnQuiz = {i: Quiz[key] for i, key in enumerate(Quiz.keys(), 1)} # changes the keys to still be in order from 1 to n

    return returnQuiz, Quastions, PossibleAnswer, Answer

def runQuiz(Quiz: dict, total: int, time: int) -> str:
    '''
    takes the entier quiz; randomly chooses a question inside of the quiz dictunary; removes the question from the set
    displays the question to the user
    lets the user input something with a timeout running so that if they run out of time the quiz ends
    once the user puts in the new input a new timeout time is calculated
    checks if the ancer the user put in is valid (only accepts A, B, C, D, a, b, c, d, 1, 2, 3, 4); if not repet the question
    check if the ancer is currect and therefor appends "C"; if wrong then "W"; if you run out of time then "T"
    retures that array

    Peramiters:
    -----------
        Quiz : dict
            contaning the question set that is used for the exam
        total : int
            the number of possible questions that will be asked (if the user dose not run out on time)
        time : int
            the ammout of time untill the quiz is forced to stop

    retrun
        str
            an array of "C" "W" "T" contaning if the question can ancerd currectly or wrong

    Examples
    --------
    Examples are diffrent dependent on the settings inputed 
    >>> Quiz contaning Math and history questions, 3, 20
        1
        3
        1
    ("C","W","C")

    >>> Quiz contaning Computer sci questions, 8, 20
        1
        b
        4
        A
        b
    ("C","W","C","C","W","T","W","W")
    '''
    i=0
    Results = []
    Values = ["A","B","C","D"]
    nextQuestion = True
    while i != total: # loops untill all quesitons are right
        GUI.clearConsole()

        if nextQuestion == True: # checks if it can go to the next question
            Quiz, Quastions, PossibleAnswer, Answer = randomQuastions(Quiz)
        nextQuestion = False

        GUI.InputUI(i+1, total, 1)
        print(f"Question: {Quastions}")
        f = 0
        for z in PossibleAnswer: # printing the possible ancers to the quetion
            print (f"{Values[f]}: {z}")
            f+=1
        GUI.InputUI(i+1, total, 2)
        output, time = GUI.input(time, Values)


        posresult = False # checks if the valuse is A; B; C; D only
        for t in Values:
            if output == t:
                posresult = True

        if output == Answer: # checks if the result is right wrong or ran out on time
            Results.append("C")
            nextQuestion = True
            i+=1
        elif posresult == True:
            Results.append("W")
            nextQuestion = True
            i+=1
        elif output == "TIME":
            Results.append("T")
            total -= 1
            while i != total:
                Results.append("W")
                i += 1

    GUI.clearConsole()
    return Results