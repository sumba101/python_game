'''module to take input'''


class _getChUnix:
    '''class to take input'''

    def __call__(self):
        '''def to call function'''
        import sys
        import tty
        import termios
        old_settings = termios.tcgetattr( sys.stdin )
        try:
            tty.setcbreak( sys.stdin.fileno() )
            c = sys.stdin.read( 1 )

        finally:
            termios.tcsetattr( sys.stdin, termios.TCSADRAIN, old_settings )
        return c

