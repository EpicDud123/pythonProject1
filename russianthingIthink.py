import Levenshtein

str1 = "12345"
str2 = "abcd567"

distance = 1-Levenshtein.distance(str1, str2)/max(len(str1), len(str2))
print("The Levenshtein distance between the strings is:", distance)
