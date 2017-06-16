##Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
##
##Hints:
##Use list[index] notation to get a element from a list.
##
##Solution:




##Write a program to solve a classic ancient Chinese puzzle: 
##We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
##
##Hint:
##Use for loop to iterate all possible solutions.
##
##Solution:



























subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print( sentence)


def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print("chickens = {} and rabbits = {}".format(solutions[0], solutions[1]))
#beautiful solution
#mylist = [[c,r] for c in range(35) for r in range(35) if((c+r==35) and (2*c+4*r==94))]
mylist = [[c,r] for c in range(10) for r in range(35) if(((4*c-3*r)==12) and (r==(2*c-3)))]
print(mylist)
#http://mathforum.org/library/drmath/view/62209.html
#To solve them using numpy
