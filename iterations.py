from itertools import permutations
perms = [''.join(p) for p in permutations('data')]
for p in permutations('data'):
	print(p)
print(perms)	
