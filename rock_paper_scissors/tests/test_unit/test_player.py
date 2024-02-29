from unittest import TestCase
from unittest.mock import patch

from game.models import Player
from game.settings import ALLOWED_ATTACKS, MODE_HARD, MODE_NORMAL, PLAYER_LIVES, PLAYER_LIVES_FOR_MODE_HARD
from game.exeptions import GameOver, IncorrectModeError, NegativeOrZeroScoreError
 

class PlayerInitTest(TestCase):

    def test_init_normal_mode(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        self.assertEqual(player.name, 'test_name')
        self.assertEqual(player.lives, PLAYER_LIVES)

    def test_init_hard_mode(self) -> None:
        player = Player('test_name', MODE_HARD)
        self.assertEqual(player.name, 'test_name')
        self.assertEqual(player.lives, PLAYER_LIVES_FOR_MODE_HARD)


    def test_init_incorrect_mode(self) -> None:
        with self.assertRaises(IncorrectModeError):
            Player('test_name', "blablabla")

class PlayerSelectAttackTest(TestCase):

    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)

    @patch('builtins.input', side_effect=ALLOWED_ATTACKS.keys())
    def test_valid_attack(self, mock_input) -> None:
        for allowed_attack_value in ALLOWED_ATTACKS.values():
            self.assertEqual(self.player.select_attack(),allowed_attack_value)

    @patch('builtins.input', side_effect=['hello','Daniil','432','2'])
    def test_invalid_atack(self, mock_input) -> None:
        self.player.select_attack()
        self.assertEqual(mock_input.call_count, 4)


class PlayerAddScoreTest(TestCase):

    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)

    def test_valid_add_scores(self) -> None:
        score = 5
        self.player.add_score(score)
        self.assertEqual(self.player.scores,score)

    def test_negative_add_scores(self) -> None:
        with self.assertRaises(NegativeOrZeroScoreError):
            self.player.add_score(-10)

    def test_zero_add_scores(self) -> None:
        with self.assertRaises(NegativeOrZeroScoreError):
            self.player.add_score(0)


class PlayerDecreaseLivesTest(TestCase):

    def setUp(self) -> None:
       self.player = Player('test_name', MODE_NORMAL)

    def test_decrease_lives(self) -> None:
        self.player.decrease_lives()
        self.assertEqual(self.player.lives, PLAYER_LIVES - 1)

    def test_die_player(self) -> None:
        self.player.decrease_lives()
        self.player.decrease_lives()
        self.player.decrease_lives()
        self.player.decrease_lives()
        with self.assertRaises(GameOver):
            self.player.decrease_lives()

