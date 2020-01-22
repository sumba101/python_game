import numpy

class Coins:
    def __init__(self):
        self._coins_cor=numpy.arange(-7,-5).reshape(1,2)

    def get_corr(self):
        return self._coins_cor

    def update_corr(self,cor):
        self._coins_cor=cor
