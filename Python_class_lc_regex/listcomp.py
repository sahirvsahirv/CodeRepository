#list comprehensions

#concise
#twice as fast of writing the older way, the interpreter executes it as another command
#and hence one more machine cycle

list = []

for i in range(100):
    list.append(i)
#print(list)

#i*i = output
#i = the variable
#range(100) = input set
list = [ i*i for i in range(100)]    
#print(list)

squareslist = []
mylist = [1,2,3,4]

for i in mylist:
    squareslist.append(i*i)

#print(mylist)
#print(squareslist)

newsquares = [i*i for i in [1,2,3,4]]
#print(newsquares)

ifcondsquares = [i*i for i in range(10) if (i%2 == 0)]
#print(ifcondsquares)


nestedloop = []
nestedloop2 = []
loop1 = [1,2]
loop2 = ['a','b']

for i in loop1:
    for j in loop2:
        nestedloop.append([i,j])
        nestedloop2.append((i,j))

#print(nestedloop)
#print(nestedloop2)


cnestedloop = [[i,j] for i in loop1 for j in loop2]
cnestedloop2 = [(i,j) for i in loop1 for j in loop2]

print(cnestedloop)
print(cnestedloop2)

#Exercise
zippedlist = [i for i in zip([1, 2], ["a", "b"])]
print(zippedlist)














#Answer
zipped = [(loop1[i], loop2[i]) for i in range(len(loop2))]
print(zipped)







