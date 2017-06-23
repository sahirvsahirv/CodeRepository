import re

string = "my address is gowri.r@gmail.com"

emailwb3 = re.search(r'\w+\.\w+@\w+\.\w+[com]', string)
print("Using grouping with [\w]", emailwb3.group())

emailwb3 = re.search(r'[\w.]+@\w+\.\w+[com]', string)
print("Using grouping with [\w] - a shortcut", emailwb3.group())
print("\n")

