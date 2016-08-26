import os, sys
print(sys.version)
print("Current script's path: %s" % os.path.dirname(os.path.abspath(__file__)))
print("Current working directory: %s" % os.getcwd())
print("Current directory contents: %s" % os.listdir("."))
