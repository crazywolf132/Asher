import os
import sys

script_name = os.path.basename(sys.argv[0])

if script_name != 'setup.py':
    from .samantha import Samantha

__version__ = '0.4.3'
__author__ = 'Gunther Cox'
__email__ = 'gunthercx@gmail.com'

