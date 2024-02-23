from game import settings,models,scores
from game import game as gm

def create_player()-> tuple:
    name = input("Enter your name.. ")
    while True:
        try:
            mode = settings.MODES[input("Select the game mode: 1 - Normal, 2 - Hard  ")]
            player = models.Player(name,mode)
            return player, mode
        except KeyError:
            print("Incorrect select entered") 


def play_game()->None:
    player, mode = create_player()
    game = gm.Game(player, mode)
    game.play()

def show_scores()-> None:
    result_scores = scores.ScoreHandler()
    result_scores.display()

def main()->None:
    while True:
        choice = input("Enter 1 - to start the game, 2 - to see points, 3 - to end the game... ")
        if choice == settings.START:
            play_game()
        elif choice == settings.SCORES:
            show_scores()
        elif choice == settings.EXIT:
            exit()
        else:
            print("Incorrect move entered")


if __name__ == "__main__":
    main()