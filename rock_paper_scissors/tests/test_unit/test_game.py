from unittest import TestCase

from game.models import Enemy, Player
from game.settings import ATTACK_PAIRS_OUTCOME, MODE_HARD, MODE_NORMAL,ALLOWED_ATTACKS
from game.game import Game
from game.exeptions import IncorrectModeError
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
            game = Game(player, "BlaBlaBla")

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

    def test_valid_fight(self):
        self.assertEqual([move for move in product(ALLOWED_ATTACKS.values(),repeat =2)],list(ATTACK_PAIRS_OUTCOME.keys()))