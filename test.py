import os
import bullets
import game_state
import numpy as np
x= bullets.Bullet()
print(x.get_cor())

game_state.remove_bullet(x,-7,-6)
print(x.get_cor())
# import numpy as np

#
# x=np.arange(10).reshape(10,1)
# y=np.arange(-10,0).reshape(10,1)
# x=np.append(x,y,axis=1)
#
# print(x)
#
# c=list(filter(lambda row: row[0]>=4 and row[1]>=-6,x))
# print(c)
#
# print(len(c))
#
# print(c[0])
from random import seed, randint
from time import time, sleep

import numpy as np

# import config
#
# for i in range(13):
#     for j in range(40):
#         print(config.villain[i][j],sep='',end='')
#     print(i)

