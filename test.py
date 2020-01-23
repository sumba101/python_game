import bullets
import numpy as np

import game_state

x=bullets.Bullet()
temp= x.get_cor()
temp = np.insert( temp, len( temp ), [-7, 5], axis=0 )
temp = np.insert( temp, len( temp ), [-7, 6], axis=0 )

print(temp)
x.update_cor(temp)
game_state.remove_bullet(x,-7,-6)
print(x.get_cor())
