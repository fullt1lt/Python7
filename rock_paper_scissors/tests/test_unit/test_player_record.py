from unittest import TestCase

from game.scores import PlayerRecord
from game.settings import MODE_NORMAL
from game.models import Player

class TestPlayerRecord(TestCase):

    def test_init_normal(self) -> None:
        name = 'test_name'
        score = 1
        player_record = PlayerRecord(name, MODE_NORMAL, score)
        self.assertEqual(player_record.name,name)
        self.assertEqual(player_record.mode,MODE_NORMAL)
        self.assertEqual(player_record.score,score)

    def test_init_object(self) -> None:
        name = 'test_name'
        player = Player(name,MODE_NORMAL)
        player_record = PlayerRecord.from_player_and_mode(player,MODE_NORMAL)
        self.assertEqual(player_record.name,name)
        self.assertEqual(player_record.mode,MODE_NORMAL)
        self.assertEqual(player_record.score,0)