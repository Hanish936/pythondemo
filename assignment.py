#2 Write a Python program to count the number of characters (character frequency) in a string.
#Sample
#String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(frequency('google.com'))
var=2
print(type(var))

#1st
var1="this is a string"
print(len(var1))
#4rd question
def change(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change('restart'))
#5th
def charsmixup(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(charsmixup('abc', 'xyz'))
#6th
def add_string(str1):
  length = len(str1)
  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

#8th
def findlongestword(word):
  word_len = []
  for n in word:
    word_len.append((len(n), n))
  word_len.sort()
  return word_len[-1][0], word_len[-1][1]
result = findlongestword(["PHP", "Exercises", "Backend"])
print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])
#9th
def remove_char(str, n):
  first_part = str[:n]
  last_part = str[n + 1:]
  return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))
#10th
def change_sring(str1):
  return str1[-1:] + str1[1:-1] + str1[:1]
print(change_sring('abcd'))
print(change_sring('12345'))
