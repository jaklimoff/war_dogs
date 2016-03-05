import time
import sys

#def do_task():
#    time.sleep(0.5)

#def example(n):
#    for i in range(n):
#        do_task()
#        print '\b*',
#        sys.stdout.flush()
#    print ' Game loaded!'

#print 'Starting ',
#example(8)


import progressbar
import time

progress = progressbar.ProgressBar()
for i in progress(range(15), "Computing: ", 40):
    time.sleep(0.1)