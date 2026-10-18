
import numpy as np

price = np.array([100,200,300,400])
print(price+100)
print(price-100)
print(price*2)
print(price**2)

print(price.min())
print(price.max())
print(price.mean())
print(price.sum())

print(price[price>150])
print((price>150).sum())    