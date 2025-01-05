from Question import Question
from Quiz import Quiz
from QuestionProvider import QuestionProvider


class QuizManager:
    """
        Manages flow in the app
    """
    def __init__(self):
        self.questions = {
            "easy": list[Question],
            "medium": list[Question],
            "hard": list[Question]
        }

    """
        Sets difficulty by input 
        If user types wrong selection repeats
    """
    def select_difficulty(self):
        print("Select difficulty: [easy, medium, hard]")
        while True:
            difficulty = input("Difficulty: ").strip().lower()
            if difficulty in self.questions:
                return difficulty
            print("Type difficulty again.")

    """
        Starts quiz - sets difficulty, loads questions and runs quiz
    """
    def start_quiz(self):
        difficulty = self.select_difficulty()
        questionProvider = QuestionProvider()
        questions = questionProvider.load_questions(difficulty)
        quiz = Quiz(questions)
        quiz.run()
