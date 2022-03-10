import sys
from cwfilt import *

if __name__ == "__main__":
    with open(sys.argv[1]) as fp:
        symbols = fp.read().splitlines()
    with open("demangled_"+sys.argv[1], "a") as newFile:
        for symbol in symbols:
            symbolp = symbol.split('=')
            try:
                newFile.write(demangle(symbolp[0]) + '=' + symbolp[1]+"\n")
            except:
                pass