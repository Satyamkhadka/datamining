import math
import numpy as np
import pandas as pd


# just for adding data to the csv
# data = np.random.randint(0, 1000, size=(100, 2))
# pd.DataFrame(data).to_csv("data.csv", header=('x', 'y'), index=None)

# getting data from csv
data = pd.read_csv('data.csv')

# logging
print(data.min().min())
print(data.max().max())

# converting panda datafram to  numpy array
data = pd.DataFrame.to_numpy(data)

# setting number of clusters to 10
k = 10
# setting nmber of iteration to 20
iteration = 20
# setting centers
centers = np.random.randint(data.min().min(), data.max().max(), size=(k, 2))


def get_nearest_mean(coord):
    nearest_coord = []
    nearest_distance = 0
    for item in centers:
        result.append({'coord': coord, 'distance': math.sqrt(
            (coord[0]-item[0])**2+(coord[1]-item[1])**2)})


# center = np.zeros((iteration,data.shape[0],2),dtype=object) #creating 3 dimensional array.
center = [[[[] for y in range(2)] for x in range(data.shape[0])]]

for it in range(1):
    for item in range(data.shape[0]):
        center[it][item][0] = data[item]
        center[it][item][1]
