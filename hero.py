import signal
from time import time

from alarmexeception import AlarmException
import config
import input
import numpy as np


# declarations to aid in reading code
from person import Person

SHOOT=' '
LEFT = 'a'
RIGHT = 'd'
UP = 'w'
SHIELD = 'q'
BOOST = 'e'


class Hero(Person):
    def __init__(self, x, y):
        Person.__init__( self, x, y )
        self._boost= False
        self._shield=False
        self.change()

    def change(self):
        config.hero_x=self.get_x()
        config.hero_y=self.get_y()

    def gravity(self):
        if self.get_y()<config.height-4:
            self.update_y(self.get_y()+2)
            self.change()
        elif self.get_y()==config.height-4:
            self.update_y(self.get_y()+1)
            self.change()

    def acceleration(self):
        if self.get_y()>=3:
            self.update_y(self.get_y()-3-config.boost_speed)


    def left(self):
        self.update_x(config.hero_x) #because of changes produced by screen movement
        if self.get_x()-3-config.boost_speed <= config.start_col:
            pass
        else:
            self.update_x(self.get_x()-3-config.boost_speed)
            self.change()

    def right(self):
        self.update_x(config.hero_x) #because of changes produced by screen movement
        if self.get_x() + 3+config.boost_speed >= config.start_col+config.frame_width:
            pass
        else:
            self.update_x( self.get_x() + 3 +config.boost_speed)
            self.change()

    def up(self):
        self.acceleration()
        self.change()

    def shield(self):
        if config.state!='r':
            return None
        config.shield=True
        config.state='u'
        config.boost_end_time = time() + 10

    def boost(self):
        if config.state!='r':
            return None
        config.boost_end_time=time()+10
        config.boost_speed=1
        config.state='u'

    def movehero(self,screen,bullet):
        ''' moves hero'''

        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.15):
            ''' input method '''
            signal.signal( signal.SIGALRM, alarmhandler )
            signal.setitimer( signal.ITIMER_REAL, timeout )
            try:
                text = input._getChUnix()()
                signal.alarm( 0 )
                return text
            except AlarmException:
                pass
            signal.signal( signal.SIGALRM, signal.SIG_IGN )
            return ''

        char = user_input()
        if char == LEFT:
            self.left()

        elif char==RIGHT:
            self.right()

        elif char==UP:
            self.up()

        elif char==SHIELD:
            self.shield()

        elif char==BOOST:
            self.boost()

        elif char==SHOOT:
            self.bullets(screen,bullet)

        if config.start_col>self.get_x():
            self.update_x(config.start_col)

        if config.start_col+config.frame_width-5<self.get_y():
            self.update_y(config.start_col+config.frame_width-5)

        self.change()

    def restart_life(self):
        #Resets the hero co ordinates to the initial one
        self.update_y(config.height-5)
        self.update_x(config.start_col)
        self.change()

    def bullets(self,screen,bullet):
        #bullets come from y+1,x+6
        temp=bullet.get_cor()
        if self.get_x()+6 < config.width:
            temp=np.insert( temp,len(temp), [self.get_y()+1, self.get_x()+6],axis=0 )
            bullet.update_cor(temp)
            screen[self.get_y()+1][self.get_x()+6]='>'

    def magnet_effect(self, param, param1, param2):
        if param1<=self.get_x() and param2>=self.get_x() and param+4<=self.get_y():
            self.up()
            if param1<=self.get_x() and param2-40>=self.get_x():
                self.right()
            # else:
            #     self.left()
        else:
            pass

