import os

os.mkdir('mydir')
os.chdir('mydir')

open('file1.txt', 'w').close()
open('file2.txt', 'w').close()
open('file3.txt', 'w').close()

print(os.listdir())
