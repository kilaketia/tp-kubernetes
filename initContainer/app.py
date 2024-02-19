import os
import sys

MESSAGE = os.environ.get('MESSAGE')
with open('/volume/message.txt','w') as f:
    f.write(MESSAGE)