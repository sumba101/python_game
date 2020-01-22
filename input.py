'''module to take input'''


class _getChUnix:
    '''class to take input'''

    def __call__(self):
        '''def to call function'''
        import sys
        import tty
        import termios
        # fedvar = sys.stdin.fileno()
        # old_settings = termios.tcgetattr(fedvar)
        # try:
        #     tty.setraw(sys.stdin.fileno())
        #     charvar = sys.stdin.read(1)
        # finally:
        #     termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        # return charvar
        old_settings = termios.tcgetattr( sys.stdin )
        try:
            tty.setcbreak( sys.stdin.fileno() )
            c = sys.stdin.read( 1 )

        finally:
            termios.tcsetattr( sys.stdin, termios.TCSADRAIN, old_settings )
        return c

# import os
# import sys
# import termios
# import fcntl
#
# def getch():
#   fd = sys.stdin.fileno()
#
#   oldterm = termios.tcgetattr(fd)
#   newattr = termios.tcgetattr(fd)
#   newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
#   termios.tcsetattr(fd, termios.TCSANOW, newattr)
#
#   oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
#   fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
#
#   try:
#     while 1:
#       try:
#         c = sys.stdin.read(1)
#         break
#       except IOError: pass
#   finally:
#     termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
#     fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
#   return c
