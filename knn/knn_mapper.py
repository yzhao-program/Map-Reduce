#!/usr/bin/env python3

import sys
import csv

def readcsv(filename):
    X_t = []
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            x_test = list(map(float, line))
            X_t.append(x_test)
        return X_t

def knn_mapper():

    X_test = readcsv('test_n.csv')

    min_distance = [10000000,] * 15
    label = [-1,] * 15

    for line in sys.stdin:
        if line.strip() == "":
            continue
        features_target = line.strip().split(',')
        features = list(map(float, features_target[:-1]))
        target = int(float(features_target[-1]))

        idx = 0

        for x_test in X_test:
            distance_list = [(features[i] - x_test[i]) ** 2 for i in range(len(features))]
            distance_square = sum(distance_list)
            if distance_square < min_distance[idx]:
                min_distance[idx] = distance_square
                label[idx] = target
            idx = idx + 1
    
    for j in range(len(label)):
        print('\t'.join((str(j+1), str(label[j]), str(min_distance[j]))))

if __name__ == '__main__':
    knn_mapper()
