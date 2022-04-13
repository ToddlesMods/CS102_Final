#!/usr/bin/env python3

def gSorter(game):
	return game.data['score']

class Game:
	def __init__(self, game):
		self.name = game
		self.data = {}
		
	def __repr__(self):
		return self.name

			
class GameList:
	def __init__(self,game):
		self.top_game = game
		self.high_score = game.data['score']
		self.bottom_game = game
		self.low_score = game.data['score']
		self.list = [game]

	#add a node to the GameList
	def addGame(self,game):
		self.list.append(game)
		self.list.sort(key=gSorter,reverse=True)
		self.top_game = self.list[0]
		self.high_score = self.list[0].data['score']
		self.bottom_game = self.list[-1]
		self.low_score = self.list[-1].data['score']

		
			
#tests:
		#test1 = Game('The Testing')
		#test1.data['score'] = 24
		#test2 = Game('Call of the Test')
		#test2.data['score'] = 21
		#test3 = Game('The Testing IV')
		#test3.data['score'] = 5
		#test4 = Game('Test Not')
		#test4.data['score'] = 48
		#test5 = Game('Who Done Tested it Now')
		#test5.data['score'] = 16

		#testList = GameList(test1)
		#print(testList.list)
		#testList.addGame(test2)
		#print(testList.list)
		#testList.addGame(test4)
		#print(testList.list)