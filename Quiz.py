class Quiz:

    """
        Runs the actual quiz
    """
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    """
        Starts quiz flow, asks user all the provided questions and counts correct answers
        When questions end, shows the result
    """
    def run(self):
        print("Quiz starting!")
        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}: {question.text}")
            for answer in question.answers:
                print(answer.text)
            
            answer = input("Your answer: ")
            if question.is_correct(answer):
                print("Good answer!")
                self.score += 1
            else:
                print(f"Bad answer! Correct was: {question.correct_answer.text}")
        
        print(f"Quiz end. Your score: {self.score}/{len(self.questions)}")