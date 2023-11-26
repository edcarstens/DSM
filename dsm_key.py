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
    def nextChar(self, c):
        n = ord(c) ## ASCII a=97, z=122, 0=48, 9=57
        if (n==122):
            return '0'
        elif (n==57):
            return None
        else:
            return chr(n+1)
    def nextKey(self, k, idx=1):
        if (len(k) < idx):
            kk = 'a' + k
        else:
            kk = k
        x = self.nextChar(kk[-idx])
        if (x):
            rv = kk[:-idx] + x
            if (idx > 1):
                rv += kk[-idx+1:]
            return rv
        else:
            rv = kk[:-idx] + 'a'
            if (idx > 1):
                rv += kk[-idx+1:]
            return self.nextKey(kk, idx+1)
    def createUniqueKey(self, k=''):
        if (k and (k not in self.k2d)):
            kk = k
        else:
            kk = k + 'a'
        while (kk in self.k2d):
            kk = self.nextKey(kk)
        return kk
    def setUniqueKey(self):
        if (len(sys.argv) == 2):
            x = sys.argv[1]  ## use specified key (to create unique key if needed)
        elif (self.pwd in self.d2k):
            return self.d2k[self.pwd]  ## find existing key for this dir
        else:
            x = ''  ## create new unique key
        return self.createUniqueKey(x)

dsm_dirs = dsm_dirs_Class()
print(dsm_dirs.setUniqueKey())

