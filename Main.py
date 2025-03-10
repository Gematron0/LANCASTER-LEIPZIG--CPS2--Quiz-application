# files
import GenerateQuiz # this file generates the quiz
import GenerateResults
import Settings
import FileHandeling

import sys

def main():
    while True:
        UserChoice = Settings.Selection()
        if UserChoice == 1:
            Quiz, NumberOfQuestions, time = Settings.QuizSelection()
            results = GenerateQuiz.runQuiz(Quiz, NumberOfQuestions, time)
            GenerateResults.runResults(results, True)
        if UserChoice == 2:
            UserInput = input("what result name shuld be read: ")
            PossibleResults = FileHandeling.read(UserInput)
            qurryNumber = Settings.pastResultSelection(PossibleResults)
            try:
                results = FileHandeling.readWithQurry(UserInput, qurryNumber)
                GenerateResults.runResults(results, False)
            except:
                pass


if __name__ == "__main__":
    main()