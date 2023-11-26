## python3 code for DSM to support pd function
import sys
import os
class dsm_dirs_Class:
    def __init__(self):
        self.k2d = dict()
        self.d2k = dict()
        self.dlst = []
        self.pwd = os.environ['PWD']
        dirs = os.environ['DSM_DIRS'].split()
        for i in range(0, len(dirs), 2):
            self.k2d[dirs[i]] = dirs[i + 1]
            self.d2k[dirs[i + 1]] = dirs[i]
            self.dlst.append(dirs[i + 1])
    def setUniqueKey(self):
        self.key = sys.argv[1]
        return self
    def addPair(self):
        d = self.pwd
        if (d not in self.d2k):
            self.dlst.append(d)
        self.d2k[d] = self.key
    def __repr__(self):
        dirs = []
        for d in self.dlst:
            dirs += [self.d2k[d],d]
        return ' '.join(dirs)
    
dsm_dirs = dsm_dirs_Class()
dsm_dirs.setUniqueKey().addPair()
print(dsm_dirs)
