from game import models
from game import settings
from game import scores
from game import exeptions

class Game:
    player: object
    enemy: object
    mode: int
    level_enemy: int = 0 

    def __init__(self,player: object,mode: str) -> None:
        self.player = player
        self.mode = mode
        self.enemy = models.Enemy(self.level_enemy)

    def create_enemy(self,level_enemy: int)-> None:
        self.enemy = models.Enemy(level_enemy)

    def play(self)-> None:
        while True:
            print(f"{self.player.name} - Enemy Level-{self.enemy.level}")
            print(f" {self.player.lives} - {self.enemy.lives}")
            result_of_the_fight = self.fight()# метод боя 
            try:
                self.handle_fight_result(result_of_the_fight)
            except exeptions.GameOver:
                handler = scores.ScoreHandler()
                handler.game_record.add_record(scores.PlayerRecord(self.player.name,self.mode,self.player.scores))
                handler.save()
                print("Game Over - You losse:(")
                print(f"{self.player.name} your scores - {self.player.scores}")
                break
            except exeptions.EnemyDown:
                self.create_enemy(self.level_enemy + 1)
                self.player.add_score(settings.POINTS_FOR_KILLING)

    def fight(self) -> int:
        player_move = self.player.select_attack()
        enemy_move = self.enemy.select_attack()
        return settings.ATTACK_PAIRS_OUTCOME[player_move,enemy_move]

    def handle_fight_result (self, result: int)-> None:
        if result > 0:
            self.player.add_score(settings.POINTS_FOR_FIGHT)
            self.enemy.decrease_lives ()
        elif result < 0:
            self.player.decrease_lives()
        else:
            print("DRAW")