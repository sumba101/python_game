import game_state
import config
import os
import numpy as np
from colorama import Back, Fore, Style


class scrn():
    def __init__(self):
        self.start_screen = [".        .          .    .    .            .            .                   .",
                             ".               ..       .       .   .             .",
                             " .      .     T h i s   i s   t h e   g a l a x y   o f   . . .             .",
                             "                     .              .       .                    .      .",
                             ".        .               .       .     .            .",
                             "   .           .        .                     .        .            .",
                             "             .               .    .          .              .   .         .",
                             "               _______________                  ",
                             " .       .    |##############|              .             ",
                             "     .        |##|   |#|   |#| .               .         .     .",
                             "              |##|   |#|   |#|       .       .        .",
                             "           .  |##|   |#|   |#|       .   .        .            .",
                             " .            |##|   |#|   |#| ANDALORIAN           .    .",
                             "     .                           .         .               .                 . ",
                             "                .                                   .            . "]
        self._instructions = ["                          ",
                              "                          ",
                              "                          ",
                              "                  Instructions:",
                              "                    ",
                              "              1) Press S to start the game",
                              "              2) Press Q to quit the Game",
                              "                    ",
                              "              Controls:",
                              "                    ",
                              "              1) Use WAD to move the hero",
                              "              2) Use SPACE to shoot ",
                              "              3) Use Q to use shield when you have power-up",
                              "              4) Use E to use boost when you have power-up ",
                              "                          ", "                          ", "                          "
                              ]

        self._initial()

    def _initial(self):
        buff = "           "
        for x in self._instructions:
            print( x )

        for y in self.start_screen:
            print( buff, y, buff )

    def create_board(self, height, width,Coin,Obs,Mag):
        self._height = int( height ) - 8
        self._frame_width = int( width )
        self._width = int( width ) * 5

        self.ground = np.full( (3, self._frame_width), 'T' )
        self.screen = np.full( (self._height, self._width), ' ' )

        # generate coins
        game_state.generate_coins( int( width ), 2 * int( width ), self.screen ,Coin)
        game_state.generate_coins( 3 * int( width ), 4 * int( width ), self.screen ,Coin)
        game_state.generate_magnet(2*int(width),3*int(width),self.screen,Mag)

        # generate obstacles
        game_state.generate_obstacle( 2 * int( width ), 4 * int( width ), self.screen ,Obs)

    def print_on_blue(self, x, y):
        if y == 'black':
            print( Fore.BLACK + Back.BLUE + x + Style.RESET_ALL, end='', sep='' )

        elif y == 'white':
            print( Fore.WHITE + Back.BLUE + x + Style.RESET_ALL, end='', sep='' )

        elif y == 'yellow':
            print( Fore.YELLOW + Back.BLUE + x + Style.RESET_ALL, end='', sep='')

        elif y == 'red':
            print( Fore.RED + Back.BLUE + x + Style.RESET_ALL, end='', sep='')

        elif y == 'green':
            print( Fore.GREEN + Back.WHITE + x + Style.RESET_ALL, end='', sep='')

    def print_on_green(self, x):
        print( Fore.BLACK + Back.GREEN + x + Style.RESET_ALL, end='', sep='')

    def refresh_screen(self,player):
        print( "\033[0;0H" )
        print(Back.WHITE + Fore.BLACK + "SCORE :- %d                    TIME REMAINING:- %d                    LIVES:- %d   %s" % (config.score, config.time_left, config.lives, config.state) + Style.RESET_ALL )

        for y in range( self._height ):
            x = config.start_col

            while (x - config.start_col) < self._frame_width:

                if y >= config.hero_y and y <= config.hero_y + 2 and x >= config.hero_x and x <= config.hero_x + 4:
                    if self.screen[y][x]=='O' and config.shield==False: #COLLISION WITH OBSTACLE
                        config.lives-=1
                        player.restart_life()
                        os.system('clear')
                        self.refresh_screen(player) #refresh screen with player in the restart position
                        return None

                    elif config.shield==True:
                        self.print_on_blue( config.hero[y - config.hero_y][x - config.hero_x], y='green' )

                    else:
                        self.print_on_blue( config.hero[y - config.hero_y][x - config.hero_x], y='white' )

                elif self.screen[y][x] == '>':
                    self.print_on_blue( self.screen[y][x], y='white' )

                elif self.screen[y][x] == 'C':  # its a coin
                    self.print_on_blue( self.screen[y][x], y='yellow' )

                elif self.screen[y][x] == 'O':
                    self.print_on_blue( self.screen[y][x], y='red' )

                else:
                    self.print_on_blue( self.screen[y][x], y='black' )

                x += 1

        for row in self.ground:
            for ele in row:
                self.print_on_green( ele )

        # there shall be an if condition to stop screen movement when dragon has fully entered the screen
        # if condition shall check if the x_co ordinate has entered the screen space and stops if so
        # game_state.move_xcor()
