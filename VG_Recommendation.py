#!/usr/bin/env python3
#Program to recommend video game

import csv
from Nodely import Game
from Nodely import GameList

#setting up game library class
GameDictionary = {}


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
		newNode = Game(row[0])
		newNode.data['system'] = row[1]
		newNode.data['genre'] = row[7]
		newNode.data['score'] = row[9]
		newNode.data['description'] = row[6]
		#add new node to correct location in storage
		#check to see if the system is already in place
		if newNode.data['system'] in GameDictionary:
			#check to see if the genre is already in place
			if newNode.data['genre'] in GameDictionary[newNode.data['system']]:
				#if the genre exists, a gamelist exists, so add the new game to the game list
				GameDictionary[newNode.data['system']][newNode.data['genre']].addGame(newNode)
			else:
				GameDictionary[newNode.data['system']][newNode.data['genre']] = GameList(newNode)
		else:
			GameDictionary[newNode.data['system']] = {}
			GameDictionary[newNode.data['system']][newNode.data['genre']] = GameList(newNode)
				
#begin the requesting part of the program

print("Hello! Welcome to the Game Library Assistant")
print("The systems we current support are:")
systemList = list(GameDictionary.keys())
keepRolling = True
while keepRolling:
	print(', '.join(systemList))

	userSys = ''
	while userSys not in systemList:
		userSys = input("Which system from above are you using?: ")
	print("Excellent!")

	genreList = list(GameDictionary[userSys].keys())
	print("These are the genre's we have for that system:")
	print(', '.join(genreList))
	userGenr = ''
	while userGenr not in genreList:
		userGenr = input("Which genre are you interested in?: ")
	
	print("Excellent!")
	print("Finally, would you like the top 10, bottom 10 or all games within that category?")
	userSelect = ''
	userOpt = ['TOP 10','BOTTOM 10','ALL']
	while userSelect not in userOpt:
		userSelect = input("Please type 'TOP 10', 'BOTTOM 10', or 'ALL': ").upper()

	#return the user's selection
	print()
	if userSelect == 'TOP 10':
		for i in range(10):
			focalGame = GameDictionary[userSys][userGenr].list[i]
			print(focalGame)
			print(focalGame.data['description'])
			print(focalGame.data['score'])
			print()
	elif userSelect == 'BOTTOM 10':
		for i in range(10):
			focalGame = GameDictionary[userSys][userGenr].list[-i]
			print(focalGame)
			print(focalGame.data['description'])
			print(focalGame.data['score'])
			print()
	else:
		for i in range(len(GameDictionary[userSys][userGenr])):
			focalGame = GameDictionary[userSys][userGenr].list[i]
			print(focalGame)
			print(focalGame.data['description'])
			print(focalGame.data['score'])
			print()
			
	#see if the user wants to look up other games
	continueQ = input("Would you like to search another group of games? Y or N: ").upper()
	if continueQ == 'N':
		keepRolling = False

