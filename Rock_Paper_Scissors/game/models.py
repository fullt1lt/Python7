import settings
from random import randint
from exeptions import GameOver,EnemyDown

class Player:
    name: str
    lives: int
    scores: int = 0

    def __init__(self,user_name : str) -> None:
        self.name = user_name
        self.lives = settings.PLAYER_LIVES

    def select_attack (self):
        while True:
            try:
                attack = input("Make a move: 1 - Paper or 2 - Stone or 3 - Scissors... ")
                return  settings.ALLOWED_ATTACKS[attack]
            except KeyError:
                print("Incorrect move entered")


    def add_score (self, scrores: int)-> None:
        self.scores += scrores

    def decrease_lives (self)-> None:
        self.lives -= 1
        if self.lives == 0:
            raise GameOver()

class Enemy:
    lives: int
    level: int

    def __init__(self, enemy_level: int) -> None:
        self.level = enemy_level
        self.lives = settings.LIVES_ENEMY + enemy_level

    def select_attack(self):
        return settings.ALLOWED_ATTACKS[str(randint(1,3))]

    def decrease_lives (self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()
