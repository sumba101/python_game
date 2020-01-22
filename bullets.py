import numpy

class Bullet:
    def __init__(self):
        self._bullet_cor=numpy.arange(-7,-5).reshape(1,2)

    def get_cor(self):
        return self._bullet_cor

    def update_cor(self,cor):
        self._bullet_cor=cor
