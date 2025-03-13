# files; all file functions that the main fincition needs to work
import GenerateQuiz
import GenerateResults
import Settings
import FileHandeling

def main():
    while True: # indefent loop
        UserChoice = Settings.Selection()
        if UserChoice == 1: # the choce of makeing and compleating a quiz
            Quiz, NumberOfQuestions, time = Settings.QuizSelection()
            results = GenerateQuiz.runQuiz(Quiz, NumberOfQuestions, time)
            GenerateResults.runResults(results, True)
        if UserChoice == 2: # the choice of reading thrue a file and seeing past results
            UserInput = input("what result name shuld be read: ")
            PossibleResults = FileHandeling.read(UserInput)
            if PossibleResults != "FILENOTFOUND": # checking if the file exsts
                qurryNumber = Settings.pastResultSelection(PossibleResults)
                if qurryNumber != "NORESULTFOUND":
                    results = FileHandeling.readWithQurry(UserInput, qurryNumber)
                    GenerateResults.runResults(results, False)


if __name__ == "__main__":
    main()