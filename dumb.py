#!/bin/python3

import pprint

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

#Visualize datacenter
#pprint.pprint(datacenter)

#Log servers ordered
#for s in range(serverNb):
  #print(servers[s])
