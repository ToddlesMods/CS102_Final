#!/usr/bin/env python3

class Node:
	def __init__(self, game):
		self.name = game
		self.head = None
		self.tail = None
		self.data = {}
		
	def __repr__(self):
		return self.name
	
	def addTail(self,node):
		if self.tail:
			node.tail = self.tail
			self.tail.head = node
			node.head = self
			self.tail = node
		else:
			node.head = self
			self.tail = node
		
	def addHead(self,node):
		if self.head:
			self.head.tail = node
			node.head = self.head
			self.head = node
			node.tail = self
		else:
			self.head = node
			node.tail = self
			
class GameList:
	def __init__(self,game):
		self.top_game = game
		self.high_score = game.data['score']
		self.bottom_game = game
		self.low_score = game.data['score']
		
				
		
	
				