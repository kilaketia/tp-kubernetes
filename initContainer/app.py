import os
import sys

MESSAGE = os.environ.get('MESSAGE')
with open('/volume/message.txt','rw') as f:
    f.write(MESSAGE)