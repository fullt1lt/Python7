from unittest import TestCase
from unittest.mock import patch

from game.scores import ScoreHandler
from game.settings import MODE_HARD, MODE_NORMAL,SCORE_FILE
import os

class TestRead(TestCase):

    def setUp(self):
        self.test_file_name = 'test_file.txt'
        with open(self.test_file_name, 'w') as test_file:
            test_file.write('John,Normal,10\n')
            test_file.write('Alice,Normal,5\n')
            test_file.write('Bob,Hard,2\n')
        
    def tearDown(self):
        os.remove(self.test_file_name)

    def test_read_valid_file(self):
        with patch('game.settings.SCORE_FILE', new=self.test_file_name):
            reader = ScoreHandler()
            reader.game_record.records = []
            reader.read()

        # Проверяем, что записи добавлены в game_record
        self.assertEqual(len(reader.game_record.records), 3)

        # Проверяем, что записи добавлены корректно
        self.assertEqual(reader.game_record.records[0].name, 'John')
        self.assertEqual(reader.game_record.records[0].mode, MODE_NORMAL)
        self.assertEqual(reader.game_record.records[0].score, 10)

        self.assertEqual(reader.game_record.records[1].name, 'Alice')
        self.assertEqual(reader.game_record.records[1].mode, MODE_NORMAL)
        self.assertEqual(reader.game_record.records[1].score, 5)

        self.assertEqual(reader.game_record.records[2].name, 'Bob')
        self.assertEqual(reader.game_record.records[2].mode, MODE_HARD)
        self.assertEqual(reader.game_record.records[2].score, 2)