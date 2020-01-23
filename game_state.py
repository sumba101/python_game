from random import seed
from random import randint
from time import time

import numpy as np
import config

def is_game_over():  # run time check first then run collision detection
    var = False
    if config.lives == 0:
        var = True
    if config.villain_life==0:
        var=True
        config.result=1
    return var

def generate_obstacle(start, end, screen, obs):
    seed( time() )
    count = randint( 5, 10 )

    for m in range( count ):
        seed( time() )
        c = randint( 1, 3 )

        if c == 1:  # vertical obstacle
            y_cor = randint( 0, config.height - 13 )
            x_cor = randint( start, end )

            temp = obs.get_vcor()

            for i in range( 13 ):
                screen[y_cor + i][x_cor] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + i, x_cor, m], axis=0 )

            for i in range( 13 ):
                screen[y_cor + i][x_cor + 1] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + i, x_cor + 1, m], axis=0 )

            for i in range( 13 ):
                screen[y_cor + i][x_cor - 1] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + i, x_cor - 1, m], axis=0 )

            obs.update_vcor( temp )

        elif c == 2:  # horizontal obstacle
            y_cor = randint( 5, config.height - 5 )
            x_cor = randint( start, end )

            temp = obs.get_hcor()

            for i in range( 13 ):
                screen[y_cor][x_cor + i] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor, x_cor + i, m], axis=0 )

            for i in range( 13 ):
                screen[y_cor + 1][x_cor + i] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + 1, x_cor + i, m], axis=0 )

            obs.update_hcor( temp )

        else:  # diagnol obstacle
            y_cor = randint( 0, config.height - 6 )
            x_cor = randint( start, end )

            temp = obs.get_dcor()

            for i in range( 6 ):
                screen[y_cor + i][x_cor - i] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + i, x_cor - i, m], axis=0 )

            for i in range( 6 ):
                screen[y_cor + i][x_cor - i + 1] = 'O'
                temp = np.insert( temp, len( temp ), [y_cor + i, x_cor - i + 1, m], axis=0 )

            obs.update_dcor( temp )

def generate_coins(start, end, screen, coin):
    seed( time() )

    count = randint( 3, 7 )
    temp = coin.get_corr()

    while count > 0:
        seed( time() )
        y_cor = randint( 5, config.height - 5 )
        x_cor = randint( start, end )
        # got co ordinates for the coin group
        for i in range( 4 ):
            for j in range( 3 ):
                screen[y_cor + j][x_cor + i] = 'C'
                temp = np.insert( temp, len( temp ), [y_cor + j, x_cor + i], axis=0 )
        count -= 1

    coin.update_corr( temp )


def coin_check(sc):
    x = config.hero_x
    y = config.hero_y
    for i in range( 3 ):
        for j in range( 5 ):
            if sc[y + i][x + j] == 'C':
                config.score += 10
                sc[y + i][x + j] = ' '  # over write the coins

    return None

def remove_obstacle(y_ob, x_ob, screen, obs):
    temp = obs.get_vcor()
    candidate = list( filter( lambda row: row[0] == y_ob and row[1] == x_ob, temp ) )
    if len( candidate ) != 0:
        candidate = candidate[0]
        ob_no = candidate[2]  # the obstacle number that must be removed

        removal = temp[temp[:, 2] == ob_no]

        for co in removal:
            screen[co[0]][co[1]] = ' '

        temp = temp[temp[:, 2] != ob_no]
        obs.update_vcor( temp )
        return None

    temp = obs.get_hcor()
    candidate = list( filter( lambda row: row[0] == y_ob and row[1] == x_ob, temp ) )
    if len( candidate ) != 0:
        candidate = candidate[0]
        ob_no = candidate[2]  # the obstacle number that must be removed
        removal = temp[temp[:, 2] == ob_no]

        for co in removal:
            screen[co[0]][co[1]] = ' '

        temp = temp[temp[:, 2] != ob_no]
        obs.update_hcor( temp )
        return None

    temp = obs.get_dcor()
    candidate = list( filter( lambda row: row[0] == y_ob and row[1] == x_ob, temp ) )
    if len( candidate ) != 0:
        candidate = candidate[0]
        ob_no = candidate[2]  # the obstacle number that must be removed
        removal = temp[temp[:, 2] == ob_no]

        for co in removal:
            screen[co[0]][co[1]] = ' '

        temp = temp[temp[:, 2] != ob_no]
        obs.update_dcor( temp )
        return None

def place_bullets(screen, bullet, obs,flag):
    if not flag: #flag is true means its the last frame boss fight so collision handling becomes easier
        temp = bullet.get_cor()
        temp = temp[temp[:, 1] > config.start_col]  # removes bullets behind the frame if any for some reason
        # clean out bullets outside of frame

        # space out all the bullets
        for co in temp:
            x = co[1]
            y = co[0]
            screen[y][x] = ' '

        temp = temp[temp[:, 1] < config.start_col + config.frame_width - 1]  # removes bullets outside of the frame
        # check for obstacles that might get rekted and remove accordingly
        # any obstacles within the 4 forward of current location if removed
        for row_no, co in enumerate( temp ):
            x_curr = co[1]
            y_curr = co[0]
            if x_curr + 4 >= config.width:
                np.delete( temp, row_no, 0 )
                continue
            for i in range( 5 ):
                if screen[y_curr][x_curr + i] == 'O':
                    remove_obstacle( y_curr, x_curr + i, screen, obs )
                    np.delete( temp, row_no, 0 )

        # update the bullet positions i.e curr_x+4
        temp[:, 1] += 4

        temp = temp[temp[:, 1] < config.start_col + config.frame_width - 1]  # removes bullets outside of the frame

        # place all the bullets
        for co in temp:
            x = co[1]
            y = co[0]
            screen[y][x] = '>'

        bullet.update_cor( temp )

    else: #its the boss fight frame
        temp = bullet.get_cor()
        temp = temp[temp[:, 1] > config.start_col]  # removes bullets behind the frame if any for some reason
        # clean out bullets outside of frame

        # space out all the bullets
        for co in temp:
            x = co[1]
            y = co[0]
            screen[y][x] = ' '

        temp = temp[temp[:, 1] < config.start_col + config.frame_width - 1]  # removes bullets outside of the frame
        # check for obstacles that might get rekted and remove accordingly
        # any obstacles within the 4 forward of current location if removed
        for row_no, co in enumerate( temp ):
            x_curr = co[1]
            y_curr = co[0]
            if x_curr + 4 >= config.width:
                np.delete( temp, row_no, 0 )
                continue
            for i in range( 5 ):

                if screen[y_curr][x_curr + i] != ' ': #cos the dragon has all kinds of ascii to keep track of
                    config.villain_life-=1 #reduce villain life
                    np.delete( temp, row_no, 0 )

        # update the bullet positions i.e curr_x+4
        temp[:, 1] += 4

        temp = temp[temp[:, 1] < config.start_col + config.frame_width - 1]  # removes bullets outside of the frame

        # place all the bullets
        for co in temp:
            x = co[1]
            y = co[0]
            screen[y][x] = '>'

        bullet.update_cor( temp )

def generate_magnet(start, end,screen, Mag):
    seed( time() )
    x_cor = randint( start, end )
    y_cor = randint(0,4) #creates magnet towards the top of the board

    for i in range(5):
        screen[y_cor][x_cor+i]=screen[y_cor][x_cor-i] = '_'

    for i in range(4):
        screen[y_cor+1][x_cor+i]=screen[y_cor+1][x_cor-i] = '_'

    for i in range(3):
        screen[y_cor+1+i][x_cor+5]=screen[y_cor+1+i][x_cor-5]='|'

    for i in range(2):
        screen[y_cor + 2 + i][x_cor + 3] = screen[y_cor + 2 + i][x_cor - 3] = '|'

    Mag.init(x_cor,y_cor)

    return None

def place_ice(screen,ice,player):
    temp = ice.get_cor()

    # space out all the bullets
    for co in temp:
        x = co[1]
        y = co[0]
        screen[y][x] = ' '

    temp = temp[temp[:, 1] > config.start_col]  # removes bullets behind the frame if any for some reason
    # clean out bullets outside of frame

    # any obstacles within the 4 forward of current location if removed
    for row_no, co in enumerate( temp ):
        x_curr = co[1]
        y_curr = co[0]
        for i in range( 5 ):
            if screen[y_curr][x_curr - i] == 'O' or screen[y_curr][x_curr - i] == '=' or screen[y_curr][x_curr - i] == '\\':
                config.lives -= 1  # reduce hero life
                np.delete( temp, row_no, 0 )
                player.restart_life()
    # update the bullet positions i.e curr_x+4
    temp[:, 1] -= 4

    temp = temp[temp[:, 1] > config.start_col]  # removes bullets behind the frame if any

    # place all the bullets
    for co in temp:
        x = co[1]
        y = co[0]
        screen[y][x] = '+'

    ice.update_cor( temp )

def remove_bullet(bullets, y, x): #to remove that one bullet show by the hero that hit the dragon
    temp=bullets.get_cor()
    temp2=np.zeros((1,2),dtype=int) #this would be removed when placing bullets so no worries
    for row in temp:
        y_cur=row[0]
        x_cur=row[1]
        if y_cur==y and x==x_cur:
            continue
        else:
          temp2 = np.insert( temp2, len( temp2 ), [y_cur, x_cur], axis=0 )

    bullets.update_cor( temp2 )
    return None

def generate_clouds(start, end, screen):
    seed( time() )
    count = randint( 5, 6 )
    for _ in range(count):
        seed( time() )
        x_cor = randint( start, end )
        y_cor = randint( 0, 4 )  # creates cloud to top of board

        for (i,row) in enumerate(config.cloud):
            for (j,ele) in enumerate(row):
                screen[y_cor+i][x_cor+j]=ele
