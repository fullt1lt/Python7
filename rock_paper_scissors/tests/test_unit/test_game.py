from unittest import TestCase
from unittest.mock import patch
from game.models import Enemy, Player
from game.settings import ATTACK_PAIRS_OUTCOME, DRAW, ENEMY_LIVES, FIGHT, KILL, LOSE, MODE_HARD, MODE_NORMAL,ALLOWED_ATTACKS, PLAYER_LIVES, POINTS_FOR_FIGHT, POINTS_FOR_FIGHT_FOR_MODE_HARD, POINTS_FOR_KILLING, POINTS_FOR_KILLING_FOR_MODE_HARD, WIN
from game.game import Game
from game.exeptions import GameOver, IncorrectModeError, IncorrectScoresAddingType
from itertools import product

class TestGameInit(TestCase):

    def test_valid_init_mode_normal(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        game = Game(player, MODE_NORMAL)
        enemy = Enemy(0, MODE_NORMAL)
        self.assertEqual(game.enemy, enemy)
        self.assertEqual(game.level_enemy, 1)

    def test_valid_init_mode_hard(self) -> None:
        player = Player('test_name', MODE_HARD)
        game = Game(player, MODE_HARD)
        enemy = Enemy(0, MODE_HARD)
        self.assertEqual(game.enemy, enemy)
        self.assertEqual(game.level_enemy, 1)

    def test_invalid_init(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        with self.assertRaises(IncorrectModeError):
            Game(player, "BlaBlaBla")

class TestGameCreateEnemy(TestCase):

    def test_vali_new_enemy(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        game = Game(player, MODE_NORMAL)
        enemy = Enemy(3,MODE_NORMAL)
        game.create_enemy()
        game.create_enemy()
        game.create_enemy()
        self.assertEqual(game.enemy, enemy)
        self.assertEqual(game.level_enemy, 4) # Сравниваем с 4 так, как уровень соперника начинается с 0


class TestGameFight(TestCase):

    def test_valid_fight(self) -> None:
        self.assertEqual([move for move in product(ALLOWED_ATTACKS.values(),repeat =2)],list(ATTACK_PAIRS_OUTCOME.keys()))


class TestAddScores(TestCase):

    def test_fight_mode_normal(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        game = Game(player, MODE_NORMAL)
        game.add_scores(FIGHT)
        self.assertEqual(player.scores,POINTS_FOR_FIGHT)

    def test_fight_hard_normal(self) -> None:
        player = Player('test_name', MODE_HARD)
        game = Game(player, MODE_HARD)
        game.add_scores(FIGHT)
        self.assertEqual(player.scores,POINTS_FOR_FIGHT_FOR_MODE_HARD)

    def test_kill_mode_normal(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        game = Game(player, MODE_NORMAL)
        game.add_scores(KILL)
        self.assertEqual(player.scores,POINTS_FOR_KILLING)

    def test_kill_hard_normal(self) -> None:
        player = Player('test_name', MODE_HARD)
        game = Game(player, MODE_HARD)
        game.add_scores(KILL)
        self.assertEqual(player.scores,POINTS_FOR_KILLING_FOR_MODE_HARD)

    def test_invalid_figth(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        game = Game(player, MODE_NORMAL)
        with self.assertRaises(IncorrectScoresAddingType):
            game.add_scores("Test")


class TestWin(TestCase):
    
    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)
       self.game = Game(self.player, MODE_NORMAL)
    
    def test_win(self) -> None:
        self.game.win()
        self.assertEqual(self.player.scores, POINTS_FOR_FIGHT)
        self.assertEqual(self.game.enemy.lives, ENEMY_LIVES - 1)
        
class TestLose(TestCase):
    
    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)
       self.game = Game(self.player, MODE_NORMAL)
    
    def test_lose(self) -> None:
        self.game.lose()
        self.assertEqual(self.player.lives, PLAYER_LIVES - 1)
        
class TestDraw(TestCase):
    
    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)
       self.game = Game(self.player, MODE_NORMAL)
       
    def test_darw(self) -> None:
        self.assertEqual(self.player.scores, 0)
        self.assertEqual(self.game.enemy.lives, ENEMY_LIVES)
        self.assertEqual(self.player.lives, PLAYER_LIVES)

class TestHandleFightResult(TestCase):

    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)
       self.game = Game(self.player, MODE_NORMAL)

    def test_handle_fight_result_win(self) -> None:
        self.game.handle_fight_result(WIN)
        self.assertEqual(self.player.scores, POINTS_FOR_FIGHT)
        self.assertEqual(self.game.enemy.lives, ENEMY_LIVES - 1)
        
    def test_handle_fight_result_lose(self) -> None:
        self.game.handle_fight_result(LOSE)
        self.assertEqual(self.player.lives, PLAYER_LIVES - 1)
        
    def test_handle_fight_result_draw(self) -> None:
        self.game.handle_fight_result(DRAW)
        self.assertEqual(self.player.scores, 0)
        self.assertEqual(self.game.enemy.lives, ENEMY_LIVES)
        self.assertEqual(self.player.lives, PLAYER_LIVES)


# class TestPlay(TestCase):
    
#     def setUp(self) -> None:
#         self.player = Player('test_name', MODE_NORMAL)
#         self.game = Game(self.player, MODE_NORMAL)

#     @patch('builtins.print')
#     @patch.object(Player, 'select_attack')
#     @patch.object(Player, 'decrease_lives')
#     @patch.object(Enemy, 'select_attack')
#     @patch.object(Game, 'handle_fight_result')
#     @patch.object(Game, 'create_enemy')
#     @patch.object(Game, 'add_scores')
#     def test_play_game_over(self, mock_add_scores, mock_create_enemy, mock_handle_fight_result, mock_enemy_select_attack, mock_player_select_attack, mock_print, mock_decrease_lives):
#         mock_enemy_select_attack.return_value = "Stone"
#         mock_player_select_attack.return_value = "Paper"
#         mock_handle_fight_result.side_effect = GameOver

#         with self.assertRaises(GameOver):
#             self.game.play()

#         mock_create_enemy.assert_not_called()
#         mock_add_scores.assert_not_called()
