import numpy

class Obstacles:
    def __init__(self):
        self._vertical_ob_cor = numpy.arange( -7, -4 ).reshape( 1, 3 )
        self._diagnol_ob_cor = numpy.arange( -7, -4 ).reshape( 1, 3 )
        self._horizontal_ob_cor = numpy.arange( -7, -4 ).reshape( 1, 3 )

    def get_vcor(self):
        return self._vertical_ob_cor

    def get_hcor(self):
        return self._horizontal_ob_cor

    def get_dcor(self):
        return self._diagnol_ob_cor

    def update_vcor(self,cor):
        self._vertical_ob_cor=cor

    def update_hcor(self,cor):
        self._horizontal_ob_cor=cor

    def update_dcor(self,cor):
        self._diagnol_ob_cor=cor
