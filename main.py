import math
from random import randint
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

xl_file = pd.ExcelFile("Data_User_Modeling_Dataset.xls")
dfs = pd.read_excel(xl_file)

print(dfs)

k = 4


def initialize_clusters(dataset):
    clusters_list = [[] for i in range(4)]
    length = len(dataset)
    for i in range(length):
        rnd = randint(0, 3)
        if rnd == 0:
            clusters_list[0].append(dataset.iloc[i])

        elif rnd == 1:
            clusters_list[1].append(dataset.iloc[i])

        elif rnd == 2:
            clusters_list[2].append(dataset.iloc[i])

        elif rnd == 3:
            clusters_list[3].append(dataset.iloc[i])
    clusters_np_array = np.array(clusters_list)
    print("############## Clusters ##############")
    print(len(clusters_np_array[0]))
    print(len(clusters_np_array[1]))
    print(len(clusters_np_array[2]))
    print(len(clusters_np_array[3]))
    return clusters_np_array


def calculate_centroids(clusters):
    sums = [[clusters[i][0][j] for j in range(len(clusters[i][0]) - 1)] for i in range(len(clusters))]

    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            for k in range(len(clusters[i][j]) - 1):
                sums[i][k] += clusters[i][j][k]

    centroids_array = np.array(sums)
    for i in range(len(sums)):
        for j in range(len(sums[i])):
            centroids_array[i][j] /= len(clusters[i])
    print("############## Centroids #############")
    print(centroids_array)
    return centroids_array


def euclidean_distance(a, b, length):
    pass


def k_means():
    pass


clusters = initialize_clusters(dfs)
centroids = calculate_centroids(clusters)
