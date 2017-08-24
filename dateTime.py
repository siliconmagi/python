import os
from time import localtime, strftime
time = strftime("%Y-%m-%d %H:%M:%S", localtime())
cmd = 'echo ' + time
os.system(cmd)
