import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

#from payment import payment_detail


def course():
    print("this is course file")

#payment_detail.payment()    