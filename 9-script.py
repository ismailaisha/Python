text = "Hello, Python! This is my string."
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char in vowels:
        result += "-"
    else:
        result += char

print(result)