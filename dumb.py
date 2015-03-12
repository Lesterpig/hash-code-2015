#!/bin/python3

import pprint,math

def findFreePosition(row, size, serverId):

  currentIndex = 0
  remainingSize = size
  for i in range(0, len(row)):
    if row[i] != -2:
      currentIndex = i+1
      remainingSize = size
    elif remainingSize == 1:
      row[currentIndex] = serverId
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

    placed = findFreePosition(rows[currentRow], servers[i][0], servers[i][4])

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
    datacenter[i].append(-2)

for b in range(bannedPlacementNb):
  ban = input().split(" ")
  x = (int(ban[0]))
  y = (int(ban[1]))
  bannedPlacement.append((x,y))
  datacenter[x][y] = -1

for s in range(serverNb):
  serv = input().split(" ")
  # Create a tuple with size, capacity, and capacity/size, group, originalId
  servers.append((int(serv[0]), int(serv[1]), int(serv[1]) / int(serv[0]), -1, s))

#Order by capacity/size dec
servers = sorted(servers, key=lambda servers: servers[2], reverse=True)

placeServers(servers, datacenter)

serversShow = sorted(servers, key=lambda servers: servers[4]) # THIS IS NOT LEGAL


for i in range(0,16): # for each row

  nbGroup = 6
  if i > 13:
    nbGroup = 3

  sumRow = 0
  for j in range(len(datacenter[i])):
    if datacenter[i][j] >= 0:
      sumRow += serversShow[datacenter[i][j]][1]

  idealC = sumRow / nbGroup

  indexFrom = int(i/2)*6
  indexTo   = (int(i/2)+1)*6

  if i > 13:
    indexFrom = 42
    indexTo   = 45

  for j in range(indexFrom, indexTo): # for each group
    sumCurGr = 0
    for k in range(len(datacenter[i])): # pour each slot
      if datacenter[i][k] >= 0:
        currentServer = serversShow[datacenter[i][k]]
        if currentServer[3] == -1 and (currentServer[1] + sumCurGr < idealC or j == indexTo-1): # todo optimize
          sumCurGr += currentServer[1]
          serversShow[datacenter[i][k]] = (currentServer[0], currentServer[1], currentServer[2], j, currentServer[4]) # THIS IS NOT LEGAL

#pprint.pprint(servers)

## LETS DO THE SHOW

def getPosition(serverId):
  for i in range(len(datacenter)):
    for j in range(len(datacenter[i])):
      if datacenter[i][j] == serverId:
        return (i, j)

  return (66666, -1)

for i in range(len(serversShow)):
  if serversShow[i][3] == -1:
    print("x")
  else:
    position = getPosition(serversShow[i][4])
    print(str(position[0]) + " " + str(position[1]) + " " + str(serversShow[i][3]))

