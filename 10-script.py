list1 = [2, 'car', 24, 'cat', 244,4]
list2 = [1, 'house', 23, 'dog', 244, 5, 'car']
result = []

for item in list1:
    if item in list2 and item not in result:
        result.append(item)
print(result)