from Question import Question
from Answer import Answer
import json

class QuestionProvider:
    """
        Provides question list with answers for each question
    """
    def load_questions(self, difficulty: str):

        def load_questions_from_file(fileName: str):
            with open(fileName, 'r') as file:
                data = json.load(file)
                questions = []
                for question in data['questions']:
                    questionToAdd = Question(text=question['text'], answers=[])
                    for answer in question['answers']:
                        answerToAdd = Answer(code=answer['code'], text=answer['text'], isTrue=answer['isTrue'])
                        questionToAdd.answers.append(answerToAdd)
                    questions.append(questionToAdd)

                return questions

        match difficulty:
            case "easy":
                return load_questions_from_file('easyQuestions.json')
            case "medium":
                return load_questions_from_file('mediumQuestions.json')
            case "hard":
                return load_questions_from_file('hardQuestions.json')
            case _:
                return list

        # TODO randomize questions ~random.sample(self.questions[difficulty], min(10, len(self.questions[difficulty])))
        
        
