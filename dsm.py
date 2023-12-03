## python3 code for DSM to support functions

import sys
import os

class dsm_dirs_Class:
    def __init__(self):
        self.maxStackSize = 10
        self.k2d = dict()
        self.d2k = dict()
        self.dlst = []
        self.pwd = os.environ['PWD']
        self.home = os.environ['HOME']
        if ('OLDPWD' in os.environ):
            self.oldpwd = os.environ['OLDPWD']
        else:
            self.oldpwd = self.home
        dirs = os.environ['DSM_DIRS'].split()
        for i in range(0, len(dirs), 2):
            self.k2d[dirs[i]] = dirs[i + 1]
            self.d2k[dirs[i + 1]] = dirs[i]
            self.dlst.append(dirs[i + 1])
        if (self.pwd in self.d2k):
            self.key = self.d2k[self.pwd]
        else:
            self.key = ''
        self.context = os.environ['DSM_CONTEXT']
        self.cc = os.environ['DSM_DESC']
        x = os.environ['DSM_STACK'].split()
        if x:
            self.stackIdx = int(x[0])
            self.stack = x[1:]
        else:
            self.stackIdx = -1
            self.stack = []  ## special case (at start)
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
    def setUniqueKey(self, k=''):
        if ((k and k==self.key) or (not k and self.key)):
            return '' ## no need to create new key
        else:
            oldKey = self.key
            self.key = self.createUniqueKey(k) ## create new unique key (from k)
            return oldKey
    def dsmStack(self):
        return '%s %s' % (self.stackIdx, ' '.join(self.stack))
    def dsmStackGo(self):
        rv = []
        idx = self.stackIdx
        d = self.stack[idx]
        if (d in self.d2k):
            self.key = self.d2k[d]
            rv.append('DSM_KEY=%s' % (self.key))
        else:
            rv.append('DSM_KEY=""')
        rv.append('cd %s' % (d))
        rv.append('DSM_STACK="%s"' % self.dsmStack())
        return rv
    def dsmStackPush(self, d, od):
        if (not self.stack):
            self.stack = [od, d]
            self.stackIdx = 1
        elif (self.stackIdx < len(self.stack)-1):
            self.stack = [od, d]
            self.stackIdx = 1
        else:
            self.stack.append(d)
            self.stackIdx += 1
            if (len(self.stack) > self.maxStackSize):
                self.stack = self.stack[1:]
                self.stackIdx -= 1
        return('DSM_STACK="%s"' % self.dsmStack())

    ## Begin DSM Commands
    def b(self):
        rv = []
        if (self.stack):
            if (self.stackIdx <= 0):
                rv.append('echo DSM:b: Error - Cannot go back any further')
            else:
                self.stackIdx -= 1
                rv = self.dsmStackGo()
        else:
            rv.append('echo DSM:b: Error - Directory history is empty')
        print(' && '.join(rv))
    def f(self):
        rv = []
        if (self.stack):
            if (self.stackIdx >= len(self.stack)-1):
                rv.append('echo DSM:f: Error - Cannot go forward any further')
            else:
                self.stackIdx += 1
                rv = self.dsmStackGo()
        else:
            rv.append('echo DSM:f: Error - Directory history is empty')
        print(' && '.join(rv))
    def g(self, k=''):
        rv = []
        if k:
            if (k in self.k2d):
                d = self.k2d[k]
                self.key = k
                rv.append('cd %s' % (d))
                rv.append('DSM_KEY=%s' % (self.key))
            else:
                print('echo DSM:g: Error - Key not found')
                return 1
        else:
            d = self.home
            rv.append('cd')
            if (d in self.d2k):
                self.key = self.d2k[d]
                rv.append('DSM_KEY=%s' % (self.key))
        rv.append(self.dsmStackPush(d, self.pwd))
        print(' && '.join(rv))
    
    ## Already cd'd to dir (PWD)
    def pd(self, k=''):
        rv = []
        # create unique key if needed
        oldKey = self.setUniqueKey(k)
        if (oldKey):
            rv.append('unset _' + oldKey)
        d = self.pwd
        if (d not in self.d2k):
            self.dlst.append(d)
        self.d2k[d] = self.key
        self.k2d[self.key] = d
        rv.append('export _' + self.key + '=' + d)
        dirs = []
        for d in self.dlst:
            dirs += [self.d2k[d],d]
        rv.append('DSM_DIRS="%s"' % (' '.join(dirs)))
        rv.append('DSM_KEY=%s' % (self.key))
        rv.append(self.dsmStackPush(self.pwd, self.oldpwd))
        print(' && '.join(rv))
    def d(self, k=''):
        if k:
            if (k in self.k2d):
                print(self.k2d[k])
            else:
                print('DSM:d: Error - key (' + k + ') not found')
        else:
            dsmKeys = self.k2d.keys()
            if dsmKeys:
                kMax = max([len(x) for x in dsmKeys])
                fmt = "%" + str(kMax) + "s  %s"
                for d in self.dlst:
                    print(fmt % (self.d2k[d], d))
    def k(self, d=''):
        if (not d):
            d = self.pwd
        if (d in self.d2k):
            print(self.d2k[d])
        else:
            print('DSM:k: Warning - dir (' + d + ') does not have a key')
    def c(self, fn=''):
        if (not fn):
            print('DSM:c: Error - No filename specified for loading context')
        else:
            self.context = fn
            dsmContexts = os.environ['DSM_CONTEXTS']
            fp = dsmContexts + '/' + fn ## full file path
            dirs = []
            cc = ''
            rv = []
            with open(fp) as file:
                for line in file:
                    first = line[0]
                    if (first != '#'):
                        k,d = line.strip().replace('  ', ' ').split()
                        dirs += [k,d]
                        rv.append('export _%s=%s' % (k,d))
                    elif (not cc):
                        cc = line ## first comment
            if (len(cc) < 2):
                cc = '# DSM context file, %s' % (fn)
            rv.append('DSM_CONTEXT="%s"' % (fn))
            rv.append('DSM_DESC="%s"' % (cc))
            rv.append('DSM_DIRS="%s"' % (' '.join(dirs)))
            d = self.pwd
            if (d in self.d2k):
                self.key = self.d2k[d]
                rv.append('DSM_KEY=%s' % (self.key))
            print(' && '.join(rv))
    def sc(self, fn=''):
        if (not fn):
            fn = self.context
            if (not fn):
                print('DSM:sc: Error - No filename specified for saving context')
                return 1
        dsmContexts = os.environ['DSM_CONTEXTS']
        fp = dsmContexts + '/' + fn ## full file path
        kMax = max([len(x) for x in self.k2d.keys()])
        fmt = "%" + str(kMax) + "s  %s"
        with open(fp,'w') as file:
            file.write(cc)
            for d in self.dlst:
                file.write(fmt % (self.d2k[d], d))
        return 0
    def rmk(self, k=''):
        rv = []
        if (not k):
            print('echo DSM:rmk: Error - No key specified to be removed')
        else:
            if (k in self.k2d):
                rv.append('unset _%s' % (k))
                d = self.k2d[k]
                del self.d2k[d]
                dirs = []
                for d in self.dlst:
                    if (d in self.d2k):
                        dirs += [self.d2k[d],d]
                rv.append('DSM_DIRS="%s"' % (' '.join(dirs)))
                if (k == self.key):
                    rv.append('DSM_KEY=""') ## remove current key
                print(' && '.join(rv))
            else:
                print('echo DSM:rmk: Error - Key not found')
    def ds(self):
        idx = 0
        for d in self.stack:
            if (self.stackIdx == idx):
                pre = '> '
            else:
                pre = '  '
            print("%s%s" % (pre,d))
            idx += 1

dsm_dirs = dsm_dirs_Class()
cmd = sys.argv[1]
arg1 = sys.argv[2] if (len(sys.argv) > 2) else ''
#arg2 = sys.argv[3] if (len(sys.argv) > 3) else ''
if cmd == 'g':
    dsm_dirs.g(arg1)
elif cmd == 'b':
    dsm_dirs.b()
elif cmd == 'f':
    dsm_dirs.f()
elif cmd == 'pd':
    dsm_dirs.pd(arg1)
elif cmd == 'd':
    dsm_dirs.d(arg1)
elif cmd == 'c':
    dsm_dirs.c(arg1)
elif cmd == 'sc':
    dsm_dirs.sc(arg1)
elif cmd == 'rmk':
    dsm_dirs.rmk(arg1)
elif cmd == 'k':
    dsm_dirs.k(arg1)
elif cmd == 'ds':
    dsm_dirs.ds()
