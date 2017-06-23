import re

#match = re.search("pattern", "string")

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:                      
    print( 'found', match.group()) ## 'found word:cat'
else:
    print( 'did not find')

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') #=>  found, match.group() == "iii"
print(match.group())
match = re.search(r'igs', 'piiig') #=>  not found, match == None
print(match)
## . = any char but \n
match = re.search(r'..g', 'piiig') #=>  found, match.group() == "iig"
print(match.group())
## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') #=>  found, match.group() == "123"
print(match.group())
match = re.search(r'\w\w\w', '@@abcd!!')# =>  found, match.group() == "abc"
print(match.group())

##+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
##* -- 0 or more occurrences of the pattern to its left
##? -- match 0 or 1 occurrences of the pattern to its left
#+ and * are greedy
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')# =>  found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') #=>  found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')# =>  found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') #=>  found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') #=>  found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') #=>  not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') #=>  found, match.group() == "bar"
