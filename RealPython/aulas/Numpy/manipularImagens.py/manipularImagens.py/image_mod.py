import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread(r"C:\Users\CASSIO\Documents\Python\Aprendendo-python\RealPython\aulas\Numpy\manipularImagens.py\kitty.jpg")

'''output = img.copy()
output[:, :, :2] = 0 # vai criar uma outra imagem azul
mpimg.imsave('Blue.jpg', output) 
'''

'''averages = img.mean(axis=2) # pega a media do rgb
mpimg.imsave('bad-gray.jpg', averages, cmap='gray')'''

# Metodo de luminosidade
weights = np.array([0.3, 0.5, 0.11])
cinza = img @ weights
mpimg.imsave('good-gray.jpg', cinza, cmap='gray')


