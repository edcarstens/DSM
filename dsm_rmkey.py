## python3 code for DSM to support rmk function
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
    def rmkey(self, k):
        if (k in self.k2d):
            d = self.k2d[k]
            del self.d2k[d]
    def __repr__(self):
        dirs = []
        for d in self.dlst:
            if (d in self.d2k):
                dirs += [self.d2k[d],d]
        return ' '.join(dirs)
    
dsm_dirs = dsm_dirs_Class()
dsm_dirs.rmkey(sys.argv[1])
print(dsm_dirs)


