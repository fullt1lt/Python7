class PlayerRecord:
    def __init__(self, name, mode, score):
        self.name = name
        self.mode = mode
        self.score = score

    def __eq__(self, other):
        return self.name == other.name and self.mode == other.mode

    def __gt__(self, other):
        return self.score > other.score

    # def __str__(self):
    #     return f"PlayerRecord(name={self.name}, mode={self.mode}, score={self.score})"


class GameRecord:
    def __init__(self):
        self.records = []

    def add_record(self, player_record):
        for existing_record in self.records:
            if existing_record == player_record:
                if player_record.score > existing_record.score:
                    existing_record.score = player_record.score
                break
        else:
            self.records.append(player_record)

    def prepare_records(self, max_records):
        self.records.sort(reverse=True)
        self.records = self.records[:max_records]


class ScoreHandler:
    def __init__(self, file_name):
        self.game_record = GameRecord()
        self.file_name = file_name
        self.read()

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    name, mode, score = data[0], data[1], int(data[2])
                    player_record = PlayerRecord(name, mode, score)
                    self.game_record.add_record(player_record)
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")

    def save(self):
        self.game_record.prepare_records(10)  # Пример: ограничиваем до 10 лучших результатов
        with open(self.file_name, 'w') as file:
            for record in self.game_record.records:
                file.write(f"{record.name},{record.mode},{record.score}\n")

    def display(self):
        for record in self.game_record.records:
            print(f"{record.name} {record.mode} {record.score}")


# Пример использования
handler = ScoreHandler("scores.txt")
new_record = PlayerRecord("John", "normal", 400)
handler.game_record.add_record(new_record)
handler.save()
new_record = PlayerRecord("John1", "normal", 300)
handler.game_record.add_record(new_record)
handler.save()
handler.display()