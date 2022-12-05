import os
import sys

path = (sys.argv[1])

liste = (os.listdir(path))

for nb,i in enumerate(liste):
    print (f"{nb}. {i}")
print(liste)