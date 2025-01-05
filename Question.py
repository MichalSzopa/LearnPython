from dataclasses import dataclass
from Answer import Answer

@dataclass
class Question:
    """
        Contains question data with list of answers
    """
    text: str
    answers: list[Answer]

    def is_correct(self, answer: str):
        ans = next((x for x in self.answers if x.code == answer), None)
        if (ans != None and ans.isTrue):
            return True
        else:
            return False
    @property
    def correct_answer(self):
        return next((x for x in self.answers if x.isTrue), None)


