#!/bin/python3

import pprint,math

def findFreePosition(row, size, capacity):

  currentIndex = 0
  remainingSize = size
  for i in range(0, len(row)):
    if row[i] != 0:
      currentIndex = i+1
      remainingSize = size
    elif remainingSize == 1:
      row[currentIndex] = capacity
      for j in range(currentIndex + 1, currentIndex + size):
        row[j] = -1
      return currentIndex
    else:
      remainingSize -= 1

  return -1

def placeServers(servers, rows):

  # TODO better handling of non placed servers

  currentRow = 0
  for i in range(0, len(servers)):
    if currentRow == len(rows):
      currentRow = 0

    placed = findFreePosition(rows[currentRow], servers[i][0], servers[i][1])

    # Select the next row
    if placed >= 0:
      currentRow += 1

info = input().split(" ")
rows = int(info[0])
placementNb = int(info[1])
bannedPlacementNb = int(info[2])
groupNb = int(info[3])
serverNb = int(info[4])

bannedPlacement = list()
servers = list()

datacenter = [[]]

for i in range(rows):
  if i != rows - 1:
    datacenter.append([])
  for j in range(placementNb):
    datacenter[i].append(0)

for b in range(bannedPlacementNb):
  ban = input().split(" ")
  x = (int(ban[0]))
  y = (int(ban[1]))
  bannedPlacement.append((x,y))
  datacenter[x][y] = -1

for s in range(serverNb):
  serv = input().split(" ")
  # Create a tuple with size, capacity, and capacity/size
  servers.append((int(serv[0]), int(serv[1]), int(serv[1]) / int(serv[0])))

#Order by capacity/size dec
servers = sorted(servers, key=lambda servers: servers[2], reverse=True)

placeServers(servers, datacenter)

minRow = 111111111111
for i in range(len(datacenter)):
  sumRow = 0
  for j in range(len(datacenter[i])):
    if datacenter[i][j] > 0:
      sumRow += datacenter[i][j]

  minRow = min(sumRow, minRow)

print(minRow)



#Visualize datacenter
#pprint.pprint(datacenter)

#Log servers ordered
#for s in range(serverNb):
  #print(servers[s])
