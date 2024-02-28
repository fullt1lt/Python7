from game.settings import ALLOWED_ATTACKS, ENEMY_LIVES, ENEMY_LIVES_FOR_MODE_HARD, MAX_ATTACK_VALUE, MIN_ATTACK_VALUE, MODE_HARD, MODE_NORMAL,PLAYER_LIVES, PLAYER_LIVES_FOR_MODE_HARD  
from random import randint
from game.exeptions import EnemyDown, GameOver
from game.validations import validate_mode, validate_scores

class Player:
    name: str
    lives: int
    scores: int = 0

    def __init__(self,user_name : str, mode : str) -> None:
        self.name = user_name
        validate_mode(mode)
        if mode == MODE_NORMAL:
            self.lives = PLAYER_LIVES
        else:
            self.lives = PLAYER_LIVES_FOR_MODE_HARD


    def select_attack (self):
        while True:
            try:
                attack = input("Make a move: 1 - Paper or 2 - Stone or 3 - Scissors... ")
                return  ALLOWED_ATTACKS[attack]
            except KeyError:
                print("Incorrect move entered")

    def add_score (self, scores: int)-> None:
        validate_scores(scores)
        self.scores += scores

    def decrease_lives (self)-> None:
        self.lives -= 1
        if self.lives == 0:
            raise GameOver


class Enemy:
    def __init__(self, enemy_level: int, mode : str) -> None:
        self.level = enemy_level
        validate_mode(mode)
        if mode == MODE_NORMAL:
            self.lives = ENEMY_LIVES + enemy_level
        else:
            self.lives = ENEMY_LIVES_FOR_MODE_HARD + enemy_level

    def select_attack(self):
        return ALLOWED_ATTACKS[str(randint(MIN_ATTACK_VALUE,MAX_ATTACK_VALUE))]

    def decrease_lives (self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
