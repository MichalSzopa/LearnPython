from dataclasses import dataclass

@dataclass
class Answer:
    """
        Contains answer data
    """
    code: str
    text: str
    isTrue: bool