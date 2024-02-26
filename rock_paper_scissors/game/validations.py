from game.exeptions import IncorrectModeError, IncorrectScoresAddingType, NegativeOrZeroScoreError
from game.settings import MODES, SCORES_ADDING_TYPES

def validate_mode(mode:str) -> None:
    if mode not in MODES.values():
        raise IncorrectModeError
    
def validate_scores(scores: int) -> None:
    if scores <= 0:
        raise NegativeOrZeroScoreError


def validate_scores_adding_type (type_: str) -> None:
    if type_ not in SCORES_ADDING_TYPES:
        raise IncorrectScoresAddingType