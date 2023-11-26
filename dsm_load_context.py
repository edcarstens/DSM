## python3 code for DSM to support c function
import sys
import os
home = os.environ['HOME']
dirs_ary = []
cc = ''
if (len(sys.argv) > 1):
    fn = home + "/DSM/contexts/" + sys.argv[1]
    #print('Loading from ' + fn + ' ..')
    with open(fn) as file:
        for line in file:
            first = line[0]
            if (first != '#'):
                k,d = line.strip().replace('  ', ' ').split()
                dirs_ary += [k,d]
                #os.environ["_" + k] = d
            elif (not cc):
                cc = line ## first comment
    if (len(sys.argv) == 2):
        print(' '.join(dirs_ary))
    elif (cc and (len(cc) > 2)):
        print(cc)
    else:
        print('# DSM context file, %s' % (sys.argv[1]))
#os.environ['DSM_DIRS'] = ' '.join(dirs_ary)
