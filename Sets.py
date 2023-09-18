fSet = {'Kris', 'Roy', 'Arif', 'Dima', 'Arif'}
sSet = {'Kris', 'Roy', 'Arif'}
c = fSet.issubset(sSet)
s = sSet.issubset(fSet)
print(c, s)
def sets(fSet, sSet):
    a = fSet & sSet
    print(a)
sets(fSet, sSet)