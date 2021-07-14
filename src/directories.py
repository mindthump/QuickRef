import os
import sys
from pathlib import Path

print(sys.version)
print("Current script's path: {}".format(Path(__file__).resolve()))
print("Current working directory: {}".format(os.getcwd()))
print("Current directory contents: {}".format(os.listdir(".")))
