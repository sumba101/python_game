import os
from time import time, sleep
import hero
import game_state
import config

import coins, bullets, obstacles
from magnet import Magnet


def start_game(screen):
    height, width = os.popen( 'stty size', 'r' ).read().split()

    #this obtains board size and width as dependent on the terminal size
    config.height = int( height ) - 8
    config.width = int( width ) * 5
    config.frame_width = int( width )

    Coin = coins.Coins()
    Obs = obstacles.Obstacles()
    Bullets = bullets.Bullet()
    Mag=Magnet()

    screen.create_board( height, width, Coin, Obs, Mag )

    #print(Mag.get_y(),Mag.get_start(),Mag.get_end())


    player = hero.Hero( 4, 40 )  # creating hero with co ordinates

    config.time_left = 500
    config.start_time = time()

    screen.refresh_screen( player )

    while ((not game_state.is_game_over()) and (config.time_left > 0)):
        player.gravity()
        player.magnet_effect(Mag.get_y(),Mag.get_start(),Mag.get_end()) #to put the effect of the magnet on the hero

        player.movehero( screen.screen, Bullets)

        game_state.coin_check( screen.screen )

        game_state.place_bullets( screen.screen, Bullets, Obs )

        #config.time_left = config.time_left-(time()-config.start_time)
        screen.refresh_screen( player )

        if config.start_col <= 4 * int( width ):  # for moving the board frame
            config.start_col += 1 + config.boost_speed

        if config.boost_end_time <= time():
            if config.state == 'u':
                if config.boost_speed!=0:
                    config.boost_speed = 0
                elif config.shield!=0:
                    config.shield=0
                config.state = 'c'
                config.boost_end_time=time()+10

            elif config.state=='c':
                config.boost_end_time=time()+10
                config.state='r'


    if config.result == 1:
        print( "YOU WON !!!!!!!!! :)" )
    else:
        print( "YOU LOST :( :( :(" )

    print( "SCORE- %d" % (config.score) )
