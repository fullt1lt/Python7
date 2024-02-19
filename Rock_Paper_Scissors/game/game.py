class Game:
    player: player
    enemy: enemy
    mode: int

    def __init__(self,pl) -> None:
        self.player = pl
        pass

    def create_enemy(self):
        pass

    def Play(self):
        while True:
            try:
                fight()# метод драка 
            except: