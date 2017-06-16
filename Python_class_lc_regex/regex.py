import re

##RULES
##a, X, 9, < : plain characters match themselves
##^$*+?{[]|() : meta-characters that have special meanings
##() : Define the scope and precedence of the operators
##: Boolean “or”, meaning either one or other of one	other
##^ : Start of a string
##$ : End of a string
##\ : inhibit the uniqueness of a character that is otherwise considered a meta-character (i.e., \ . for period; \ \ for slash; $ for a dollar sign)
##? : match zero or one occurrence of the pattern to the left (i.e., may or may not appear in pattern)
##- : if between two [], indicates a range of digits or alphabetic chars; will be interpreted as a literal if appearing first or last inside [].
##* : zero or more occurrences of a pattern to the left of
##+ : one or more occurrences of a pattern to the left of (q+, say, if you are expecting multiple q’s)
##. : periods match any character (except newline \n)
##{n} : matches number of times the preceding character/s appear (for example, a tel. # might be [0-9]{3}-[0-9]{3}-[0-9]{4})
##\w : matches a “word” character (such as a letter, number, or underbar)
##\W : matches any non-word character
##\d : decimal digit (ie, 0-9)
##\b : boundary between word and non-word and \B non-word boundary
##\s : matches any single whitespace character (such as space, newline, return, tab, form)
##\t : tab
##\n : newline
##\r : return
##\f : form
##\S : marches any non-whitespace character

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

  
textmatched = re.search("he is", "what a kind boy he is!")
textmatched = re.search(r"he is", "what a kind boy he is!")
print(textmatched.group())

#escaping with a back slash
textmatched = re.search("he\\s", "what a kind boy he\\s!")
textmatched = re.search(r"he\\s", "what a kind boy he\\s!")
print(textmatched.group())

#with group []
## inside a group - searched for one character amongst the group
## . , - are literal
## \ backslash for escaping is not allowed
## [^xyz] -all but xyz for exclusion

string = "my address is gowri.r@gmail.com"
#one or more characters
#then an '@'
#one or more characters
#escaping . - literal one
#one ore more of - c or o or m

email2 = re.search(r'.+@.+\.[com]', string)
#one or more words not having '@'
#then one '@'
#one or more words not having '@'
#literal . - escaping . (since '.' means any character)
#one or more words not having '@'
email21 = re.search(r'[^@]+@[^@]+\.[^@]+',string)

print("Email example 1: Using grouping\n", email2.group())
print("\n")
print("Email example 2: Using group and not starting with\n", email21.group())
print("\n")
#break the code - change it to ".ccom" and try ".gth"

#try with word boundaries now - [com] matches only a list
#\w = one or more words
#\. = escaping '.' - a literal '.'
#\w = one or more words
#@ = literal '@'
#\w+ = one or more words
#\. = a literal '.'
#\w+[com] = one or more words - with c/o/m
stringnet = "my address is gowri.r@gmail.net"
#will only search for .com
emailwb = re.search(r'\w+\.\w+@\w+\.\w+[com]', stringnet)
print("Email example 3: Using \w\n", emailwb)
#print(emailwb)


print("\n")
#try changing it by removing the [com] - any \w - word can be there not neccessarily .com
emailwb2 = re.search(r'\w+\.\w+@\w+\.\w+', stringnet)
print("Email example 4: Using \w - alternative for trying net\n", emailwb2.group())
print("\n")

#saving the pattern - pattern is simpler
#Group = word boundary and a literal '.'
#one or more wih a word boundary and a '.'
#@ = literal @
#\w+\. = one or more words and a literal '.'
#\w+[com] =  one or more words with c/o/m
emailwb3 = re.search(r'[\w.]+@\w+\.\w+[com]', string)
print("Email example 5: Using grouping with [\w]", emailwb3.group())
print("\n")

#Change the previous - \w+\. to a group
emailwb4 = re.search(r'[\w.]+@[\w.]+[\w]+[com]', string)
print("Email example 6: Using grouping with [\w] - the second group:  ", emailwb4.group())
#print(emailwb4)
print("\n")
#more with comrgnetdu
#Use a | in the group
stringnewnet = "my address is gowri.r@gmail.cgn"
emailwb5 = re.search(r'[\w.]+@[\w.]+[com|org|net|edu]', stringnewnet)
print("Email example 7: Using grouping with [\w] - add net/edu etc", emailwb5.group())
#print(emailwb5)
print("\n")


#there is .findall .sub for substitute, but the crux is learn how to create patterns
#.split


#Exercises

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
#Write a Python program that matches a word at the beginning of a string.
#Write a Python program that matches a word containing 'z'.
#Write a Python program that matches a word containing 'z', not start or end of the word.
#Write a Python program that matches a word at end of string, with optional punctuation.



















#solution 1:  patterns = 'a.*?b$'
#solution 2: ^\w+
#solution 3: \w*z.\w* or \w*z\w*
#solution 4: '\Bz\B'
#solution 5:  \w+\S*$ - \S is non-whitespace

#it can get very complex and the RFC compliant code is

##
#(?:(?:\r\n)?[ \t])*(?:(?:(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t]
##)+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:
##\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(
##?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ 
##\t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\0
##31]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\
##](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+
##(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:
##(?:\r\n)?[ \t])*))*|(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z
##|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)
##?[ \t])*)*\<(?:(?:\r\n)?[ \t])*(?:@(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\
##r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[
## \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)
##?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t]
##)*))*(?:,@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[
## \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*
##)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t]
##)+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*)
##*:(?:(?:\r\n)?[ \t])*)?(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+
##|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r
##\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:
##\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t
##]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031
##]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](
##?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?
##:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?
##:\r\n)?[ \t])*))*\>(?:(?:\r\n)?[ \t])*)|(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?
##:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?
##[ \t]))*"(?:(?:\r\n)?[ \t])*)*:(?:(?:\r\n)?[ \t])*(?:(?:(?:[^()<>@,;:\\".\[\] 
##\000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|
##\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>
##
##@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"
##(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t]
##)*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
##".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?
##:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[
##\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*|(?:[^()<>@,;:\\".\[\] \000-
##\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(
##?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)*\<(?:(?:\r\n)?[ \t])*(?:@(?:[^()<>@,;
##:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([
##^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\"
##.\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\
##]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*(?:,@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\
##[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\
##r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] 
##\000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]
##|\\.)*\](?:(?:\r\n)?[ \t])*))*)*:(?:(?:\r\n)?[ \t])*)?(?:[^()<>@,;:\\".\[\] \0
##00-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\
##.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,
##;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|"(?
##:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*))*@(?:(?:\r\n)?[ \t])*
##(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".
##\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t])*(?:[
##^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\]
##]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*\>(?:(?:\r\n)?[ \t])*)(?:,\s*(
##?:(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
##".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(
##?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[
##\["()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t
##])*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t
##])+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?
##:\.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|
##\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*|(?:
##[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".\[\
##]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)*\<(?:(?:\r\n)
##?[ \t])*(?:@(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["
##()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)
##?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>
##
##@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*(?:,@(?:(?:\r\n)?[
## \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,
##;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\.(?:(?:\r\n)?[ \t]
##)*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\
##".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*)*:(?:(?:\r\n)?[ \t])*)?
##(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\["()<>@,;:\\".
##\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])*)(?:\.(?:(?:
##\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z|(?=[\[
##"()<>@,;:\\".\[\]]))|"(?:[^\"\r\\]|\\.|(?:(?:\r\n)?[ \t]))*"(?:(?:\r\n)?[ \t])
##*))*@(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])
##+|\Z|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*)(?:\
##.(?:(?:\r\n)?[ \t])*(?:[^()<>@,;:\\".\[\] \000-\031]+(?:(?:(?:\r\n)?[ \t])+|\Z
##|(?=[\["()<>@,;:\\".\[\]]))|\[([^\[\]\r\\]|\\.)*\](?:(?:\r\n)?[ \t])*))*\>(?:(
##?:\r\n)?[ \t])*))*)?;\s*)
##################



#https://regex101.com/

#demilitor for the .
#emailwb6 = re.search(r'/.+@.+\..+/i', string)
#print("Email example 8: ", emailwb6)
#print(emailwb6)
#print("\n")






















