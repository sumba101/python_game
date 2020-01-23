from random import seed, randint
from time import time

import numpy as np

import config
from person import Person


class Villain(Person):
    def __init__(self, x, y):
        super().__init__( x, y )
        self._change()

    def _change(self):
        config.villain_x=self.get_x()
        config.villain_y=self.get_y()

    def shoot_ice(self,screen,ice):
        seed( time() )
        op = randint(1,16)
        if op%5==0:
            temp = ice.get_cor()
            temp = np.insert( temp, len( temp ), [self.get_y() + 7, self.get_x() - 1], axis=0 )
            ice.update_cor( temp )
            screen[self.get_y() + 7][self.get_x() -1] = '+'
        else:
            pass

    def update(self,y,ice,screen):
        if y+13<config.height and y!=0: #check if the height is within the height boundary of the dragon
            self.update_y(y)
        self._change()
        self.shoot_ice(screen,ice)

