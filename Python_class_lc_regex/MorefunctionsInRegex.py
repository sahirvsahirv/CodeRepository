import re

stripaddr = "182.168.1.2"

match = re.search('\d+\.\d+\.\d+\.\d+',stripaddr)

print(match)

print(re.match('\d+\.\d+\.\d+\.\d+',stripaddr))


prog = re.compile('(\d+)\.(\d+)\.(\d+)\.(\d+)')
#print("grouping...")
print(prog.match(stripaddr).group(0))
print(prog.match(stripaddr).group(1))
print(prog.match(stripaddr).group(2))
print(prog.match(stripaddr).group(3))
print(prog.match(stripaddr).group(4))
#print(prog.match(stripaddr).group(5)) ##Error
print("\n")

line = "cats are smarter than dogs"

#Match does only in the beginning of the string and
#search does anywhere
print("search dogs")
print(re.search(r'dogs', line, re.M | re.I).group(0))
#re.match for "dogs" will return None
print("Match dogs will return None")

print('match cats')
print(re.match(r'cats', line, re.M | re.I).group(0))

print("\n")
print("substitute")
print(re.search("cat", line, re.I))
print(re.sub("cat", "foxe", line))

print("\n")

print("Phone number example")
phonestr = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phonestr)
print( "Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phonestr)    
print( "Phone Num : ", num)
