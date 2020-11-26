from boardgamegui import gui_play
from Threeinarow import Threeinarow

def main():
    game = Threeinarow(6, 6)
    gui_play(game)
    ##console_play(game)

main()
