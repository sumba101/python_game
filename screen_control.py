import game_state
import config
import os
import numpy as np
from colorama import Back, Fore, Style, init

init()

class scrn():
    def __init__(self):
        self._start_screen = [".        .          .    .    .            .            .                   .",
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
                              "              5) Use P to quit the game at any time           ", "                          ", "                          "
                              ]

        self._initial()

    def _initial(self):
        buff = "           "
        for x in self._instructions:
            print( x )

        for y in self._start_screen:
            print( buff, y, buff )

    def create_board(self, height, width,Coin,Obs,Mag):
        self._height = int( height ) - 8
        self._frame_width = int( width )
        self._width = int( width ) * 5

        self._ground = np.full( (3, self._frame_width), 'T' )
        self._screen = np.full( (self._height, self._width), ' ' )

        # generate coins
        game_state.generate_coins( int( width ), 2 * int( width ), self._screen ,Coin)
        game_state.generate_coins( 3 * int( width ), 4 * int( width ), self._screen ,Coin)
        #generate magnet
        game_state.generate_magnet(2*int(width),3*int(width),self._screen,Mag)

        # generate obstacles
        game_state.generate_obstacle( 2 * int( width ), 4 * int( width ), self._screen ,Obs)

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

    def refresh_screen(self,player,bullets):
        print( "\033[0;0H" )
        print(Back.WHITE + Fore.BLACK + "SCORE :- %d                    TIME REMAINING:- %d                    LIVES:- %d   %s" % (config.score, config.time_left, config.lives, config.state) + Style.RESET_ALL )

        for y in range( self._height ):
            x = config.start_col

            while (x - config.start_col) < self._frame_width:

                if y >= config.hero_y and y <= config.hero_y + 2 and x >= config.hero_x and x <= config.hero_x + 4:
                    if (self._screen[y][x]=='O' and config.shield==False) or (self._screen[y][x]=='+'): #COLLISION WITH OBSTACLE OR WITH DRAGONS ICE BALLS(+)
                        config.lives-=1
                        player.restart_life()
                        if self._screen[y][x]=='+':
                            self._screen[y][x] = ' '
                        os.system('clear')
                        self.refresh_screen(player,bullets) #refresh screen with player in the restart position
                        return None

                    elif config.shield==True:
                        self.print_on_blue( config.hero[y - config.hero_y][x - config.hero_x], y='green' )

                    else:
                        self.print_on_blue( config.hero[y - config.hero_y][x - config.hero_x], y='white' )

                elif y >= config.villain_y and y <= config.villain_y + 12 and x >= config.villain_x and x <= config.villain_x + 39:
                    if self._screen[y][x]=='>': #Collision with a bullet from the hero
                        config.villain_life-=1
                        self._screen[y][x]=' ' #remove this bullet
                        game_state.remove_bullet(bullets,y,x)
                        os.system('clear')
                        self.refresh_screen(player,bullets)
                        return None
                    else:
                        self.print_on_blue(config.villain[y-config.villain_y][x-config.villain_x],y='red')


                elif self._screen[y][x] == '>':
                    self.print_on_blue( self._screen[y][x], y='white' )

                elif self._screen[y][x] == 'C':  # its a coin
                    self.print_on_blue( self._screen[y][x], y='yellow' )

                elif self._screen[y][x] == 'O':
                    self.print_on_blue( self._screen[y][x], y='red' )


                else:
                    self.print_on_blue( self._screen[y][x], y='black' )

                x += 1

        for row in self._ground:
            for ele in row:
                self.print_on_green( ele )

    def get_screen(self):
        return self._screen