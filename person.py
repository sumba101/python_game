
class Person():
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def get_x(self ):
        return self._x

    def get_y(self ):
        return self._y

    def update_x(self,new_x):
        self._x=new_x

    def update_y(self,new_y):
        self._y=new_y


