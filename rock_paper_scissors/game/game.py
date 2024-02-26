from game.models import Player, Enemy
from game.settings import FIGHT, KILL, LOSE,ATTACK_PAIRS_OUTCOME, SCORES_TO_ADD, WIN
from game.scores import PlayerRecord, ScoreHandler 
from game.exeptions import EnemyDown, GameOver
from game.validations import validate_mode, validate_scores_adding_type

class Game:
    player: Player
    enemy: Enemy
    mode: str
    level_enemy: int = 0 

    def __init__(self,player: Player,mode: str) -> None:
        self.player = player
        validate_mode(mode)
        self.mode = mode
        self.create_enemy()

    def create_enemy(self) -> None:
        self.enemy = Enemy(self.level_enemy, self.mode)
        self.level_enemy += 1

    def play(self) -> None:
        while True:
            print(f"{self.player.name} - Enemy Level-{self.enemy.level}")
            print(f" {self.player.lives} - {self.enemy.lives}")
            result_of_the_fight = self.fight()# метод боя 
            try:
                self.handle_fight_result(result_of_the_fight)
            except GameOver:
                self.save_results()
                print("Game Over - You losse:(")
                print(f"{self.player.name} your scores - {self.player.scores}")
                break
            except EnemyDown:
                self.create_enemy()
                self.add_scores(KILL)

    def fight(self) -> int:
        player_move = self.player.select_attack()
        enemy_move = self.enemy.select_attack()
        return ATTACK_PAIRS_OUTCOME[player_move,enemy_move]

    def handle_fight_result (self, result: int)-> None:
        if result == WIN:
            self.win()
        elif result == LOSE:
            self.lose()
        else:
            self.draw()

    def win(self) -> None:
        self.add_scores(FIGHT)
        self.enemy.decrease_lives()
    
    def lose(self) -> None:
        self.player.decrease_lives()

    def draw(self) -> None:
        print("DRAW")

    def add_scores(self, score_adding_type: str) -> None:
        validate_scores_adding_type(score_adding_type)
        self.player.add_score(SCORES_TO_ADD[self.mode][score_adding_type])

    def save_results(self) -> None:
        handler = ScoreHandler()
        handler.add_record(PlayerRecord.from_player_and_mode(self.player, self.mode))
        handler.save()