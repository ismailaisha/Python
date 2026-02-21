my_tuple = (32, 'name', 3.21, 'python', 45, 'name')

if len(my_tuple) == len(set(my_tuple)):
    print('All elements are unique in tuple:', my_tuple)
else:
    print('There are duplicate elements in tuple:', my_tuple)