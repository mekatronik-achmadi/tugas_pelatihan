#!/usr/bin/python

"""
Identitas:
Nama: Achmadi S.T. M.T.
Email: mekatronik.achmadi@gmail.com
"""

# impor untuk numpy
import numpy as np

# impor library plot
from matplotlib import pyplot as plt

# data dasar
sudut = np.linspace(0, 2 * np.pi, 100)

# koordinat x
x = 16 * ( np.sin(sudut) ** 3 )

# koordinat y yang merupakan kombinasi 4 sinus beda frekuensi pada sudut sama
y = 13 * np.cos(sudut) - 5* np.cos(2*sudut) - 2 * np.cos(3*sudut) - np.cos(4*sudut)

# tampilkan
plt.plot(x, y)
plt.title('hhhhmmmmmmmmmmmmmmmmm')
plt.show()
