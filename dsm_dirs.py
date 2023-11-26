## python3 code for DSM to support d function
import sys
if (len(sys.argv) > 1):
    kMax = max([len(y) for y in sys.argv[1::2]])
    fmt = "%" + str(kMax) + "s  %s"
    i = 0
    for arg in sys.argv[1:]:
        if (i % 2):
            d = arg
            print(fmt % (k,d))
        else:
            k = arg
        i += 1
