from game.settings import EXIT, MODES, SCORES, START
from game.models import Player
from game.scores import ScoreHandler
from game.game import Game

def create_player() -> tuple:
    name = input("Enter your name.. ")
    while True:
        try:
            mode = MODES[input("Select the game mode: 1 - Normal, 2 - Hard  ")]
            player = Player(name,mode)
            return player, mode
        except KeyError:
            print("Incorrect select entered") 


def play_game() -> None:
    player, mode = create_player()
    game = Game(player, mode)
    game.play()

def show_scores() -> None:
    result_scores = ScoreHandler()
    result_scores.display()

def main() -> None:
    while True:
        choice = input("Enter 1 - to start the game, 2 - to see points, 3 - to end the game... ")
        if choice == START:
            play_game()
        elif choice == SCORES:
            show_scores()
        elif choice == EXIT:
            exit()
        else:
            print("Incorrect move entered")


if __name__ == "__main__":
    main()