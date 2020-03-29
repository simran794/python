import os
from datetime import datetime

# print("Hello World")
# this file will return a log file with list of files in path 'root (line 9)
# and at the end it will print current date and time

reader = open('log_{0}.txt'.format(datetime.now().strftime("%Y_%m_%d_%H_%M")),'w')
try:
    root='c:/'
    dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
    print dirlist
    for item in dirlist:
        reader.write("%s\n" % item)
finally:
    reader.close()
print datetime.now().strftime("%Y_%m_%d_%H_%M")
