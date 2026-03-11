import re
#1.Write a regex to check if a string contains only digits.

text = "Hi i am teja my num is 934"
result = re.findall("[0-9]", text)
print(result)

#2.Write a pattern to match a 10-digit mobile number.
text = "9346612345"
result = re.findall(r"^\d{10}$", text)
print(result)

#3.Find all lowercase letters in a string.
text = "Hello World! 123"
result = re.findall(r'[a-z]', text)
print(result)

#4.Extract all uppercase letters from a sentence.
text = "Hello World! 123"
result = re.findall(r'[A-Z]', text)
print(result)

#5.Match a string that starts with "Hello".
text = "Hello World!"
result = re.findall(r"^Hello",text)
print(result)

#6.Match a string that ends with "world".
text = "Hello World"
result = re.findall(r"World$",text)
print(result)

#7.Find all words separated by spaces.
text = "Hello World"
result = re.findall(r"\s",text)
print(result)

#8.Match exactly 5 characters.
text = "Hola World"
result = re.findall( r".{5}",text)
print(result)
# #Find all occurrences of the word "python" (case-sensitive).
#Replace all spaces in a string with underscores.

