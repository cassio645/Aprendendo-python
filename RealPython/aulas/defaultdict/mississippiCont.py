from collections import defaultdict
from collections import Counter


palavra = 'mississippi'
dicio = defaultdict(int)
for letra in palavra:
    dicio[letra] += 1

print(dicio)
# defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

cont = Counter('mississippi')
print(cont) # faz o mesmo