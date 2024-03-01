from unittest import TestCase

from game.scores import PlayerRecord, GameRecord
from game.settings import MODE_NORMAL, MODE_HARD

class TestAddRecord(TestCase):

    def setUp(self) -> None:
       player1 = PlayerRecord("test_name",MODE_NORMAL,5)
       player2 = PlayerRecord("test_name",MODE_HARD,10)
       player3 = PlayerRecord("test_name1",MODE_NORMAL,6)
       player4 = PlayerRecord("test_name1",MODE_HARD,8)
       self.test_records = [player1,player2,player3,player4]
       self.game = GameRecord()
       self.game.records = []
       self.game.add_record(PlayerRecord("test_name", MODE_NORMAL, 5))
       self.game.add_record(PlayerRecord("test_name",MODE_HARD,10))
       self.game.add_record(PlayerRecord("test_name1",MODE_NORMAL,6))

    def comparison_of_records(self) -> None:
        self.assertEqual(len(self.game.records),len(self.test_records))
        for game_item, test_item in zip(self.game.records, self.test_records):
            self.assertEqual(game_item.name,test_item.name)
            self.assertEqual(game_item.mode,test_item.mode)
            self.assertEqual(game_item.score,test_item.score)

    def test_add_record(self) -> None: #Проверка на добавление записи с другим модом
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))
        self.comparison_of_records()

    def test_equal_records(self) -> None: #Проверка на добавление одинаковой записи
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))#одинаковая запись 
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))
        self.comparison_of_records()
        
    def test_equal_name_and_more_scores(self) -> None: #Проверка на запись игрока с одинаковым модом но большим количеством очков 
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,7))
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))#Запись с большим колличеством очков
        self.comparison_of_records()

    def test_equal_name_and_less_scores(self) -> None: #Проверка на запись игрока с одинаковым модом но меньшим количеством очков 
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,5))#Запись с меньшим колличеством очков
        self.comparison_of_records()

    def test_new_name_and_equal_score_mode(self) -> None:
        self.test_records.append(PlayerRecord("test_name2",MODE_NORMAL,8))
        self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))
        self.game.add_record(PlayerRecord("test_name2",MODE_NORMAL,8))
        self.comparison_of_records()


class TestPrepareRecords(TestCase):

    def setUp(self) -> None:
       player1 = PlayerRecord("test_name",MODE_HARD,10)
       player2 = PlayerRecord("test_name1",MODE_HARD,8)
       player3 = PlayerRecord("test_name1",MODE_NORMAL,6)
       player4 = PlayerRecord("test_name",MODE_NORMAL,5)
       player5 = PlayerRecord("test_name2",MODE_NORMAL,4)
       self.test_records = [player1,player2,player3,player4,player5]# отсортированный список записей длинной MAX_RECORDS_NUMBER
       self.game = GameRecord()
       self.game.records = []
       self.game.add_record(PlayerRecord("test_name1",MODE_NORMAL,6))
       self.game.add_record(PlayerRecord("test_name",MODE_HARD,10))
       self.game.add_record(PlayerRecord("test_name1",MODE_HARD,8))
       self.game.add_record(PlayerRecord("test_name2",MODE_NORMAL,4))
       self.game.add_record(PlayerRecord("test_name", MODE_NORMAL,5))

    def comparison_of_records(self) -> None:
        self.assertEqual(len(self.game.records),len(self.test_records))
        for game_item, test_item in zip(self.game.records, self.test_records):
            self.assertEqual(game_item.name,test_item.name)
            self.assertEqual(game_item.mode,test_item.mode)
            self.assertEqual(game_item.score,test_item.score)


    def test_max_len_and_sorting(self) -> None:
        self.game.add_record(PlayerRecord("test_name3",MODE_NORMAL,3))
        self.game.add_record(PlayerRecord("test_name4",MODE_NORMAL,2))
        self.game.prepare_records()
        self.comparison_of_records()