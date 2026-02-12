files = ['1.txt', 'host.txt', 'new_file.txt', 'old_file.txt', 'test2.txt', 'test1.txt', 'host2.txt']

substring = 'host'

for file in files:
    if substring in file:
        print(file)

substring2 = 'test'

for file in files:
    if substring2 in file:
        print(file)
