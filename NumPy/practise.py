import numpy as np

price=np.array([120,85,200,45,160,95,310])

print("Riel: ", price*1000)
print("After delivery costs: ",price-10)
print("After discount: ",price*0.8)
print("Total: ",price.sum())
print("Mean: ",price.mean())
print("Lowest: ",price.min())
print("Highest: ",price.max())
print("Above 100: ",price[price>100])
print("How many above 100: ",(price>100).sum())
print("How many below 100: ",(price<100).sum())