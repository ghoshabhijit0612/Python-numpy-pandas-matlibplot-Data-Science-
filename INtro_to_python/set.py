a={'1',2,3,4,5}
b = {99}
a.update(b)
b.update(a)
print('b->',b)
a.add(2)
print('a->',a)
type(a)