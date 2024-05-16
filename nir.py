import difflib

str1= "Hello World!"
str2= "Hello World"
matcher= difflib.SequenceMatcher(None,str1,str2)
print("similarity ratio is;",matcher.ratio())
