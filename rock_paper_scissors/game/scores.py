from game.settings import MAX_RECORDS_NUMBER, SCORE_FILE
from game.models import Player

class PlayerRecord:
    def __init__(self, name:str, mode:str, score:int) -> None:
        self.name = name
        self.mode = mode
        self.score = score

    @classmethod
    def from_player_and_mode(cls, player: Player, mode : str) -> "PlayerRecord":
        return cls(name=player.name, mode=mode, score=player.scores)


    def __eq__(self, other) -> bool:
        return self.name == other.name and self.mode == other.mode

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"{self.name} {self.mode} {self.score}"


class GameRecord:
    records: list[PlayerRecord] = []

    def add_record(self, player_record: PlayerRecord) -> None:
        for existing_record in self.records:
            if existing_record == player_record:
                existing_record.score = max(existing_record.score, player_record.score)
                return
        self.records.append(player_record)

    def prepare_records(self) -> None:
        self.records.sort(reverse=True)
        self.records = self.records[:MAX_RECORDS_NUMBER]


class ScoreHandler:
    def __init__(self) -> None:
        self.game_record = GameRecord()
        self.file_name = SCORE_FILE
        self.read()

    def read(self) -> None:
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name, mode, score = data[0], data[1], int(data[2])
                    self.game_record.add_record(PlayerRecord(name, mode, score))
        except FileNotFoundError:
            open(self.file_name, "w").close()
        except IndexError:
            self.game_record.add_record(PlayerRecord())

    def save(self) -> None:
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record.name},{record.mode},{record.score}\n")

    def display(self) -> None:
        for record in self.game_record.records:
            print(f"{record}")

    def add_record(self, record: PlayerRecord) -> None:
        self.game_record.add_record(record)