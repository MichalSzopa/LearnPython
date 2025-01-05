from Question import Question
from Answer import Answer

class QuestionProvider:
    """
        Provides question list with answers for each question
    """
    def load_questions(self, difficulty: str):
        def easy_questions():
            questions = list[Question]
            questions = [
                Question(text="What is the correct way to print \"Hello, World!\" in Python?", 
                         answers=[
                             Answer(code="A", text="A) print(\"Hello, World!\")", isTrue=True),
                             Answer(code="B", text="B) x=2", isTrue=False),
                             Answer(code="C", text="C) return \"Hello World!\"", isTrue=False)
                             ]),
            ]
            return questions
        
        def medium_questions():
            questions = list[Question]
            questions = [
                # TODO
            ]
            return questions
        
        def hard_questions():
            questions = list[Question]
            questions = [
                # TODO
            ]
            return questions

        match difficulty:
            case "easy":
                return easy_questions()
            case "medium":
                return medium_questions()
            case "hard":
                return hard_questions()
            case _:
                return list

        # TODO put questions and answers to external source, like database or json files
        # TODO randomize questions ~random.sample(self.questions[difficulty], min(10, len(self.questions[difficulty])))
        
        
