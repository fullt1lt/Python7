from unittest import TestCase

from game.models import Enemy
from game.exeptions import EnemyDown, IncorrectModeError
from game.settings import ENEMY_LIVES, ENEMY_LIVES_FOR_MODE_HARD, MODE_HARD, MODE_NORMAL,MAX_ATTACK_VALUE,MIN_ATTACK_VALUE,ALLOWED_ATTACKS
 

class EnemyInitTest(TestCase):

    def test_init_normal_mode(self) -> None:
        enemy_lives : int = 5
        enemy = Enemy(enemy_lives, MODE_NORMAL)
        self.assertEqual(enemy.level, enemy_lives)
        self.assertEqual(enemy.lives, ENEMY_LIVES + enemy_lives)

    def test_init_hard_mode(self) -> None:
        enemy_lives : int = 5
        enemy = Enemy(enemy_lives, MODE_HARD)
        self.assertEqual(enemy.level, enemy_lives)
        self.assertEqual(enemy.lives, ENEMY_LIVES_FOR_MODE_HARD + enemy_lives)

    def test_init_incorrect_mode(self) -> None:
        enemy_lives : int = 5
        with self.assertRaises(IncorrectModeError):
            Enemy(enemy_lives, "blablabla")


class EnemySelectAttackTest(TestCase):

    def test_min_allowed_attack(self) -> None:
        self.assertEqual(min(map(int, ALLOWED_ATTACKS.keys())),MIN_ATTACK_VALUE)

    def test_max_allowed_attack(self) -> None:
        self.assertEqual(max(map(int, ALLOWED_ATTACKS.keys())),MAX_ATTACK_VALUE)

class EnemyDecreaseLivesTest(TestCase):

    def setUp(self) -> None:
       self.enemy = Enemy(0, MODE_NORMAL)

    def test_decrease_lives(self) -> None:
        self.enemy.decrease_lives()
        self.assertEqual(self.enemy.lives, ENEMY_LIVES - 1)

    def test_die_enemy(self) -> None:
        self.enemy.decrease_lives()
        self.enemy.decrease_lives()
        self.enemy.decrease_lives()
        self.enemy.decrease_lives()
        with self.assertRaises(EnemyDown):
            self.enemy.decrease_lives()