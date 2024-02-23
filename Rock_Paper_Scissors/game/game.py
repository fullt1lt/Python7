from game.models import Player,Enemy
from game import settings
from game import scores
from game import exeptions

class Game:
    player: Player
    enemy: Enemy
    mode: int
    level_enemy: int = 0 

    def __init__(self,player: Player,mode: str) -> None:
        self.player = player
        self.mode = mode
        self.enemy = self.create_enemy(self.level_enemy, self.mode)

    def create_enemy(self,level_enemy: int, mode: str)-> None:
        return Enemy(level_enemy, mode)

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
                self.enemy = self.create_enemy(self.level_enemy + 1, self.mode)
                if self.mode == settings.MODE_HARD:
                    self.player.add_score(settings.POINTS_FOR_KILLING_FOR_MODE_HARD)
                else:
                    self.player.add_score(settings.POINTS_FOR_KILLING)

    def fight(self) -> int:
        player_move = self.player.select_attack()
        enemy_move = self.enemy.select_attack()
        return settings.ATTACK_PAIRS_OUTCOME[player_move,enemy_move]

    def handle_fight_result (self, result: int)-> None:
        if result == settings.WIN:
            if self.mode == settings.MODE_HARD:
                self.player.add_score(settings.POINTS_FOR_FIGHT_FOR_MODE_HARD)
            else:
                self.player.add_score(settings.POINTS_FOR_FIGHT)
            self.enemy.decrease_lives()
        elif result == settings.LOSE:
            self.player.decrease_lives()
        else:
            print("DRAW")