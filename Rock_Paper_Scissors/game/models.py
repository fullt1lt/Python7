import settings
from random import randint
from exeptions import GameOver,EnemyDown

class Player:
    name: str
    lives: int
    scores: int = 0

    def __init__(self,user_name : str,player_lives : int) -> None:
        self.name = user_name
        self.lives = player_lives

    def select_attack (self):
        while True:
            try:
                attack = input("Make a move: 1 or 2 or 3")
                if attack in settings.ALLOWED_ATTACKS:
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
        self.lives = settings.LIVES_ENEMY[enemy_level]

    def select_atack(self):
        return settings.ALLOWED_ATTACKS[str(randint(1,3))]

    def reduction_of_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown()
