import re
# re.match() function to search pattern within the test_string.
# The method returns a match object if the search is successful.
# If not, it returns None


pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = "ma*n"
test_string = "man"
result = re.match(pattern, test_string)
# if result:
#     print("Matched")
# else:
#     print("No match")

# match
# "man",
# No match
# "mfididdn", "mafididdn", "mafn",

# pattern = "\A\(the\)"
# test_string = "(the) book" # match
# result = re.match(pattern, test_string)
# if result:
#     print("Matched")
# else:
#     print("No match")

# pattern = "^(the)"
# test_string = "tha book" # NOT match
# # "the book" matches
# result = re.match(pattern, test_string)
# if result:
#     print("Matched")
# else:
#     print("No match")

# re.findall(), if not found returns []
import re
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
# print(result)
# Output: ['12', '89', '34']

#
string = 'hE12C hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
# print(result)
# ['12', '89', '34']

# re.split()
import re
string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
# print(result)
# ['Twelve:', ' Eighty nine:', '.']

# If the pattern is not found, re.split() returns a list containing the original string.
string = 'Twelve:12 Eighty nine:89.'
pattern = '1000'

result = re.split(pattern, string)
# print(result)
# ['Twelve:12 Eighty nine:89.']

# re.sub
# re.sub(pattern, replace, string)
# The method returns a string where matched occurrences are replaced with the content of replace variable.
# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = '-'

new_string = re.sub(pattern, replace, string)
# print(new_string)
# abc-12de-23-f45-6

# re.search()
# The re.search() method takes two arguments: a pattern and a string.
# The method looks for the "first location" where the RegEx pattern produces a match with the string.
# If the search is successful, re.search() returns a match object; if not, it returns None.

# match = re.search(pattern, str)
string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

# if match:
#   print("pattern found inside the string")
# else:
#   print("pattern not found")

# Output: pattern found inside the string

# match.group() returns a string
# match.groups() returns  a tuple
string = '39801 356, 2102 1111'
# string = '2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
# The group() method returns the part of the string where there is a match
match = re.search(pattern, string)

# if match:
#   print(match.group()) # 801 35
#   # print(type(match.group())) # string
#   #print(type(match.groups()))  # <class 'tuple'>
#   #print(match.groups())   # ('801', '35')
# else:
#   print("pattern not found")

pattern = '(\d{3} \d{2})'
# match variable contains a Match object.
# The group() method returns the part of the string where there is a match
match = re.search(pattern, string)

if match:
  print(match.group()) # 801 35
  print(match.groups())   # ('801 35',)
else:
  print("pattern not found")