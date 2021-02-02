import pandas as pd

toys = pd.DataFrame([
    {'nome': 'bola', 'shape': 'redondo'},
    {'nome': 'Cubo mágico', 'shape': 'cubo'}
])
print(toys['shape']) # redondo  cubo

print(toys.shape) # (2, 2)