from unittest import TestCase

from game.models import Enemy, Player
from game.settings import ATTACK_PAIRS_OUTCOME, ENEMY_LIVES, FIGHT, KILL, LOSE, MODE_HARD, MODE_NORMAL,ALLOWED_ATTACKS, PLAYER_LIVES, POINTS_FOR_FIGHT, POINTS_FOR_FIGHT_FOR_MODE_HARD, POINTS_FOR_KILLING, POINTS_FOR_KILLING_FOR_MODE_HARD, WIN
from game.game import Game
from game.exeptions import IncorrectModeError, IncorrectScoresAddingType
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


class TestHandleFightResult(TestCase):

    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)
       self.game = Game(self.player, MODE_NORMAL)

    def test_win(self) -> None:
        self.game.handle_fight_result(WIN)
        self.assertEqual(self.player.scores, POINTS_FOR_FIGHT)
        self.assertEqual(self.game.enemy.lives, ENEMY_LIVES - 1)

    def test_lose(self) -> None:
        self.game.handle_fight_result(LOSE)
        self.assertEqual(self.player.lives, PLAYER_LIVES - 1)


# class TestPlay(TestCase):
#     pass 