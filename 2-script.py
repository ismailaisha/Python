new_str = "СтРоКА дЛЯ проВЕрки СКрипта! Тут есть и чиСЛа 12830 и симВолы !@#$"

upper_str = 0
lower_str = 0
num_str = 0
sym_str = 0

for char in new_str:
    if char.isupper():
        upper_str += 1
    elif char.islower():
        lower_str += 1
    elif char.isdigit():
        num_str += 1
    else:
        sym_str += 1
print(f"В строке {upper_str} заглавных букв")  
print(f"В строке {lower_str} строчных букв")
print(f"В строке {num_str} чисел")
print(f"В строке {sym_str} символов")