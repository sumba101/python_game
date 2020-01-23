import os
import screen_control
import render_game

os.system( 'clear' )
screen = screen_control.scrn()

getch=input()

while(getch != 'Q' and getch != 'q' and getch != 's' and getch != 'S'):
    getch=input("Try again meat head")
    print("")

if getch == 's':
        render_game.start_game(screen)
else:
    print( """
                TRY AGAIN NEXT TIME
            """ )
