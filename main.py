import math
from random import randint
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

xl_file = pd.ExcelFile("iris-data.xlsx")
dfs = pd.read_excel(xl_file)

print("############## Data Set ##############")
print(dfs)

k = 3


def initialize_clusters(dataset):
    clusters_list = [[] for i in range(k)]

    for i in range(len(dataset)):
        rnd = randint(0, k - 1)
        clusters_list[rnd].append(dataset.iloc[i])

    clusters_np_array = np.array(clusters_list)
    return clusters_np_array


def calculate_centroids(clusters):
    sums = [[clusters[i][0][j] for j in range(len(clusters[i][0]))] for i in range(len(clusters))]

    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            for k in range(len(clusters[i][j])):
                sums[i][k] += clusters[i][j][k]

    centroids_array = np.array(sums)
    for i in range(len(sums)):
        for j in range(len(sums[i])):
            centroids_array[i][j] /= len(clusters[i])
    return centroids_array


def euclidean_distance(a, b, length):
    sums = 0
    for i in range(length):
        sums += math.pow((a[i] - b[i]), 2)

    distance = math.sqrt(sums)
    return distance


def k_means(dataset):
    # uncomment to eliminate 0 length cluster problem
    # global k
    clusters = initialize_clusters(dataset)
    centroids = calculate_centroids(clusters)

    print("############## Cluster sizes ##############")
    for i in range(k):
        print(len(clusters[i]))
    print("############## Centroids #############")
    print(centroids)

    step_counter = 1
    optimal_condition = False
    while not optimal_condition:
        optimal_condition = True
        print("\n\n############## Step : " + str(step_counter) + " ##############")
        step_counter += 1
        temp_clusters_list = [[] for x in range(k)]
        for i in range(len(clusters)):
            for m in range(len(clusters[i])):
                min_distance = euclidean_distance(centroids[0], clusters[i][m], len(centroids[0]))
                nearest_cluster = 0
                for j in range(len(centroids)):
                    distance = euclidean_distance(centroids[j], clusters[i][m], len(centroids[j]))
                    if distance < min_distance:
                        min_distance = distance
                        nearest_cluster = j
                temp_clusters_list[nearest_cluster].append(clusters[i][m])
                if i != nearest_cluster:
                    optimal_condition = False

        # uncomment to eliminate 0 length cluster problem
        # for i in range(len(temp_clusters_list)):
        #     if len(temp_clusters_list[i]) == 0:
        #         del temp_clusters_list[i]
        #         k -= 1

        clusters = np.array(temp_clusters_list)
        centroids = calculate_centroids(clusters)

        print("############## Cluster sizes ##############")
        for i in range(k):
            print(len(clusters[i]))
        print("############## Centroids #############")
        print(centroids)
        if optimal_condition:
            pass


k_means(dfs)
