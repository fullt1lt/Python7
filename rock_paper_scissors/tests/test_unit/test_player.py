from unittest import TestCase

from game.models import Player
from game.settings import PLAYER_LIVES
 

class PlayerInitTest(TestCase):

    def test_init_normal(self):
        player = Player('test_name', 'Normal')
        self.assertEqual(player.name, 'test_name')
        self.assertEqual(player.lives, PLAYER_LIVES)