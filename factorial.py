string = input()
splittedstring = string.split()

a = []
for numstr in splittedstring: 
    a.append(int(numstr))

print(a)

def mymax(*a):
    max = a[0]
    for i in range (1, len(a)):
        if max < i:
            max = i
    return max

print(mymax(a)) 



