import os
import sys
from .commands import Command
print 'something in the init'

script_name = os.path.basename(sys.argv[0])

if script_name != 'setup.py':
    from .samantha import Samantha
