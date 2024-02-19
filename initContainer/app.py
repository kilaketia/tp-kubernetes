import os
import sys

MESSAGE = os.environ.get('MESSAGE')
with open('/message.txt','rw') as f:
    f.write(MESSAGE)