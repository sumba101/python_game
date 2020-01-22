class Magnet():

    def init(self,x,y):
        self._startx=x-40
        self._endx=x+40
        self._y=y

    def get_start(self):
        return self._startx

    def get_end(self):
        return self._endx

    def get_y(self):
        return self._y
