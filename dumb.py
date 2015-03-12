#!/bin/python3

info = input().split(" ")
rows = int(info[0])
placementNb = int(info[1])
bannedPlacementNb = int(info[2])
groupNb = int(info[3])
serverNb = int(info[4])

bannedPlacement = list()
servers = list()

for b in range(bannedPlacementNb):
  ban = input().split(" ")
  bannedPlacement.append([int(ban[0]), int(ban[1])])

for s in range(serverNb):
  serv = input().split(" ")
  servers.append([int(serv[0]), int(serv[1])])


