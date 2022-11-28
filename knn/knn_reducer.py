#!/usr/bin/env python3

import sys
import math

def knn_reducer():

    min_distance = [math.inf,] * 15
    rowno_label = {}

    for line in sys.stdin:
        if line.strip() == "":
            continue
        row_target_distance = line.strip().split('\t')

        row_number = int(row_target_distance[0])
        target = row_target_distance[1]
        distance = float(row_target_distance[2])

        if distance < min_distance[row_number - 1]:
            min_distance[row_number - 1] = distance
            rowno_label[row_number] = target
    
    print('\t'.join(('Test data', 'Prediction')))
    for i in range(len(rowno_label)):
        print('\t'.join( (str(i + 1), rowno_label[i + 1]) ))

if __name__ == '__main__':
    knn_reducer()