#!/usr/bin/python3

import csv
import random
import sys
from calcDistance2 import calcDistance2

#read the file and split the lines
file = open("/home/haileyw7/Classwork/python/coordinates.csv", "r")
lines = file.read().splitlines()

with open("/home/haileyw7/Classwork/python/coordinates.csv", newline='\n') as csvfile:
    linesList = list(csv.reader(csvfile))

#numbers of clusters wanted
print("Number of Clusters: ")
numCluster=int(input())

#assign each cluster a random point
clusters = []
for x in range (numCluster):
    clusters.append(random.choice(lines))

print(clusters)

sum = 0
clustersSum = []
clusterMap = []
#for each point, calculate distance from each cluster
for a in lines:
    for b in clusters:
        clustersSum.append((calcDistance2(a.split(","), b.split(",")))**2)
    #add smallest distance to the sum of distances squared
    minimum = min(clustersSum)
    sum += minimum
    print("Point " + a + " belongs in Cluster " + str(clustersSum.index(minimum)) + " with a Centroid of " + str(clusters[clustersSum.index(minimum)]))
    clusterMap.append(clustersSum.index(minimum))
    clustersSum.clear()

print(clusterMap)
print(sum)

#calculate the best point by taking the avg of each dimension
sumPoints = []
bestPoint = []
numPoints = len(linesList)
dimension = len(lines[0].split(","))

for a in range(dimension):
    sumPoints.append(0)
    for b in lines:
        c = b.split(",")
        sumPoints[a] += float(c[a])

for a in sumPoints:
    bestPoint.append(a/numPoints)

print(bestPoint)

#recalculate the distance to new centroid
betterSum = 0
betterClusterSum = []

for a in linesList:
    betterClusterSum.append((calcDistance2(a, bestPoint)**2))
    betterSum += (min(betterClusterSum))
    betterClusterSum.clear()

print(betterSum)
