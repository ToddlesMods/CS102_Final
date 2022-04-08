#!/usr/bin/env python3
#Program to recommend video game

import csv
from Nodely import Node

#setting up game library class

#setting up background tree to help with searches
with open('metascrape.csv', newline='') as videogames:
	reader = csv.reader(videogames)
	#fields are 0 - 12, each row will create a node containing that game's information.
	index = 0
	for row in reader:
		#skip the first two rows as they don't contain game information
		if index < 2:
			index += 1
			continue
		newNode = Node(row[0])
		newNode.data['system'] = row[1]
		newNode.data['genre'] = row[7]
		newNode.data['score'] = row[9]
		newNode.data['description'] = row[6]
		#add new node to correct location in storage
		
