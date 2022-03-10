from itertools import count
import sys
import subprocess
from os import path

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

dir = path.dirname(path.abspath(sys.argv[1]))
name = f"demangld_{path.basename(sys.argv[1])}"

counter = 1

with open(f"{dir}\\{name}", "w") as w:
    for line in lines:
        symbol = line.split("=")[0]
        address = line.split("=")[1]
        process = subprocess.run(f"java -jar CWD.jar \"{symbol}\"", capture_output=True, shell=True)
        if process.returncode == 0:
            symbol = process.stdout.decode("UTF-8")
            symbol = symbol.strip()
            w.write(f"{symbol}={address}")
            print(f"line {counter} demangled")
        print(f"line {counter} not demangled")
        counter += 1
