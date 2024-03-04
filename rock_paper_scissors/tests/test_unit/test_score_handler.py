from unittest import TestCase
from unittest.mock import patch
from game.models import Player
from game.scores import PlayerRecord, ScoreHandler, get_filename, GameRecord
from game.settings import MODE_NORMAL, SCORE_FILE
import os


class TestScoreHandler(TestCase):

    @patch('game.scores.GameRecord')
    def test_init_score_handler(self,mock_game_record) -> None:
        sh = ScoreHandler()
        mock_game_record.assert_called_once()
        self.assertEqual(get_filename(), sh.file_name)


class TestAddRec(TestCase):

    def setUp(self) -> None:
        player = Player('test_name', MODE_NORMAL)
        self.player_record = PlayerRecord.from_player_and_mode(player, MODE_NORMAL)
        self.test_game_record = [self.player_record]

    def tearDown(self) -> None:
        os.remove('test_file.txt')

    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_add_new_record(self, mock) -> None:
        sh = ScoreHandler()
        sh.add_rec(self.player_record)
        self.assertEqual(sh.game_record.records, self.test_game_record)


class TestCheckingFileExistence(TestCase):

    def setUp(self) -> None:
        self.file_test_name = 'test_file.txt'
        self.file_path = os.path.join(os.getcwd(), self.file_test_name)

    def tearDown(self) -> None:
        os.remove(self.file_path)

    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_file_not_exists(self,mock) -> None:
        sh = ScoreHandler()
        sh.checking_file_existence()
        self.assertEqual(os.path.exists(self.file_path), True)
    
    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_file_exists(self,mock) -> None:
        self.write_test_file()
        data_before = self.read_test_file()
        sh = ScoreHandler()
        sh.checking_file_existence()
        date_after = self.read_test_file()
        self.assertEqual(data_before, date_after)

    def read_test_file(self) -> list[tuple]:
        test_data = []
        with open(self.file_test_name, 'r') as file:
            for line in file:
                test_data.append(line)
        return test_data

    def write_test_file(self) -> None:
        self.test_data = ['John,Normal,10','Alice,Normal,5','Bob,Hard,2']
        self.test_file_name = 'test_file.txt'
        with open(self.test_file_name, 'w') as test_file:
            for data_item in self.test_data:
                test_file.write(data_item + '\n')


class TestReadFileValid(TestCase):

    def setUp(self) -> None:
        self.test_data = [('John,Normal,10'),('Alice,Normal,5'),('Bob,Hard,2')]
        self.test_file_name = 'test_file.txt'
        with open(self.test_file_name, 'w') as test_file:
            for data_item in self.test_data:
                test_file.write(data_item + '\n')

    def tearDown(self):
        os.remove(self.test_file_name)
    
    def comparison_of_records(self) -> None:
        self.assertEqual(len(self.reader.game_record.records),len(self.test_data))
        for record_item, test_item in zip(self.reader.game_record.records, self.test_data):
            self.assertEqual(f"{record_item.name},{record_item.mode},{record_item.score}", test_item)

    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_read_valid_file(self,mock) -> None:
        self.reader = ScoreHandler()
        self.reader.game_record.records = []
        self.reader.read_file()
        self.comparison_of_records()


class TestGetFileName(TestCase):

    def test_valid_file_name(self) -> None:
        self.assertEqual(get_filename(), SCORE_FILE)


class TestRead(TestCase):

    def setUp(self) -> None:
        self.test_data = [('John,Normal,10'),('Alice,Normal,5'),('Bob,Hard,2')]
        self.test_file_name = 'test_file.txt'

    def tearDown(self) -> None:
        os.remove(self.test_file_name)

    def create_test_file(self) -> None:
        with open(self.test_file_name, 'w') as test_file:
            for data_item in self.test_data:
                test_file.write(data_item + '\n')
        
    def comparison_of_records(self) -> None:
        self.assertEqual(len(self.reader.game_record.records),len(self.test_data))
        for record_item, test_item in zip(self.reader.game_record.records, self.test_data):
            self.assertEqual(f"{record_item.name},{record_item.mode},{record_item.score}", test_item)
    
    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_read_file_exists(self, mock) -> None:
        self.create_test_file()
        self.reader = ScoreHandler()
        self.reader.game_record.records = []
        self.reader.read()
        self.comparison_of_records()

    @patch("game.scores.get_filename", return_value='test_file.txt')
    def test_read_not_file_exists(self, mock) -> None:
        self.test_data = [] # Обнуляем тест данные так как файл при создании должен быть пустым 
        self.reader = ScoreHandler()
        self.reader.game_record.records = []
        self.reader.read()
        self.comparison_of_records()# сравнение пустых тестовых данных с records