str_1 = 'python'
str_2 = 'newpython'

common_characters = set(str_1) & set(str_2)

for char in common_characters:
    print(f"'{char}' is a common character.")