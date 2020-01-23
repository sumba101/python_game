import os
from time import time
import hero
import game_state
import config

import coins, bullets, obstacles
from magnet import Magnet
from villain import Villain


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
    ice=bullets.Bullet()

    screen.create_board( height, width, Coin, Obs, Mag )

    player = hero.Hero( 4, 40 )  # creating hero with co ordinates

    config.time_left = 500
    config.start_time = time()

    screen.refresh_screen( player,Bullets )

    dragon_flag=0
    Dragon=Villain(config.width-49,player.get_y())


    itr=1
    quitter=False

    while ((not game_state.is_game_over()) and (config.time_left > 0) and (not quitter)):
        player.gravity()
        player.magnet_effect(Mag.get_y(),Mag.get_start(),Mag.get_end()) #to put the effect of the magnet on the hero

        quitter=player.movehero( screen.get_screen(), Bullets)

        game_state.coin_check( screen.get_screen() )

        game_state.place_bullets( screen.get_screen(), Bullets, Obs ,dragon_flag)

        config.time_left = 500-(time()-config.start_time)
        screen.refresh_screen( player ,Bullets)

        if config.start_col < 4 * int( width ):  # for moving the board frame
            config.start_col += 1 + config.boost_speed
        else:
            #this takes place when in the last frame
            dragon_flag=1
            Dragon.update(player.get_y(),ice,screen.get_screen())
            game_state.place_ice(screen.get_screen(),ice,player)

        if config.boost_end_time <= time(): #to handle power ups
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

        itr+=1
        if player.get_y()<config.height-3:
            config.hangtime+=1

    if config.result == 1:
        print( "\nYOU WON !!!!!!!!! :)" )
    else:
        print( "YOU LOST :( :( :(" )

    print( "SCORE:- %d" % (config.score) )
