# CITS1401 Semester 1 2015, Project 2
# Student 1 Name:    Harrison Marley    Student no: 21522889
# Student 2 Name:    Matt Cooper          Student no:
# Twelve Men's Morris

from graphics import *
from random import *
from math import *


wSize = 600
allLocs = []

class Player:
	def __init__(self,Colour,Player_number):
		self.blocked = False
		self.Circles = [] # List of player's Total number of pieces.
		self.cColour = Colour
		self.Player_number = Player_number
		self.Occup = [] # list of locations of player's pieces.
		self.Number_of_mills = 0
		self.linesOccup = [] # Location of player's mills
		turn = 0



def main():
	# controls the flow of the program, allows the players to put their pieces and then move them,
	# alternately, if a mill is made, invites the player to remove opponents piece and decides which
	# player has won. Uses the random function for Player 2 (the computer)
	win = GraphWin('QAT',wSize,wSize)

	win.setBackground('green')
	win.setCoords(0,0,wSize,wSize)
	ptList = drawBoard(win)

	#Circle(ptList[0][0], 20).draw(win)

	#print statements to see lists
	print(len(ptList), len(ptList[0]))
	print('allLocs list: ', allLocs)
	print(len(allLocs))
	print('ptList: ', ptList)

	#unOccup is a list of locations and is deleted from/added to as locations become taken or available
	unOccup = list(allLocs)
	print(unOccup[0])

	Player_1 = Player("white",1)
	Player_2 = Player("black",2)

	#these index variables are used to increment through the Circles list after every turn so that a new circle will be drawn
	#or else a graphics error may be raised
	Player_1_index = 0
	Player_2_index = 0


	Player_turn = 1

	while True:
		if Player_turn == 1:
			movePiece(win, ptList, Player_1_index, Player_1.cColour, Player_1.Circles, Player_1, Player_2.Occup, unOccup)
			#if isLine(Player_1.Occup, linesOccup) == True:
				#removePiece(win, ptList, Player_2.Circles, Player_2.Occup, unOccup)
			Player_1_index += 1
			if Player_1_index > 11:
				Player_1_index = 11
			Player_turn -= 1

		else:
			movePiece(win, ptList, Player_2_index, Player_2.cColour, Player_2.Circles, Player_2, Player_1.Occup, unOccup)
			Player_2_index += 1
			if Player_2_index > 11:
				Player_2_index = 11
			Player_turn += 1


	win.mainloop()


def searchForMoves(points, unOccup):
# Written by Mathew Cooper 20933403 May 2015.
# This function imports the list of all the points adjacent to the points that currently hold game pieces, 'points'.
# This function also imports the list of all points that currently hold no game pieces, 'UnOccup'.
# Each iteration of the loop searches through the list of unoccupied spaces, 'UnOccup', for one of the points in 'points'.

# If a point is found to be in both 'points' and 'UnOccup', it means that the player has an available move.
# If such a point is found, the loop ends and the function returns the variable "result" that stores the value "False".
# This ultimately results in the "blocked" function concluding that the user is not blocked and the game can continue.

# If the function completes the loop iterations without finding an available opening,
# the function returns the variable "result" that stores the value "True", that signifies that the player is blocked.
# This ultimately results in the "blocked" function concluding that the user is blocked and the game ends.

	# Initialising loop variable.
	j = 0
	# Setting up the while loop that searched 'UnOccup' one point at a time.
	while j < len(points):
		# Testing if the point for this loop is in 'UnOccup'.
		trap = (points[j] in unOccup)

		# If the point is in 'UnOccup', end the function and return that the player is not blocked.
		if (trap == True):
				result = False
				return result
		# If the point is not in 'UnOccup', continue the loop iterations until you find a valid point, or the loop condition is met.
		# If no suitable point is found before the iterations end, return that the user is blocked.
		if(trap == False):
				result = True
				j = j+1
	return result

def blocked(Occup, unOccup):
# Written by Mathew Cooper 20933403 May 2015.
	# Occup is a list of occupied points/locations by a Player and unOccup are free locations
	# returns True if all pieces of the Player are blocked otherwise Fals

	for i in range (len(Occup)):
			# Test each of the 3 possible co-ordinate points adjacent to a point in the outer square.
			if (Occup[i][0] == 0):
					# Establish point of interest.
					[a,b] = Occup[i]
					# Calculate adjacent points.
					points = [ [a,(b-1)%8], [a+1,b],[a,(b+1)%8] ] # Confirmed to correctly calculate adjacent points.
					#print([a,b])
					#print(points,"point0")
					# Search for points in unOccup to see if any moves are available.
					result = searchForMoves(points, unOccup)
					if result == False:
						return False


					i = 1 + 1
			# Test each of the 4 possible co-ordinate points adjacent to a point in the middle square.
			elif(Occup[i][0] == 1):
					# Establish point of interest.
					[x,y] = Occup[i]
					# Calculate adjacent points.
					points = [ [x+1,y], [x-1,y], [x,(y+1)%8],[x,(y-1)%8] ] # Confirmed to correctly calculate adjacent points.
					#print([x,y])
					#print(points,"point1")
					#print(points)
					# Search for points in unOccup to see if any moves are available.
					result = searchForMoves(points, unOccup)
					if result == False:
							return False


					#print("1",result)
					i = i+1
					#return result
			# Test each of the 3 possible co-ordinate points adjacent to a point in the inner square.
			elif(Occup[i][0] == 2):
					# Establish point of interest.
					[c,d] = Occup[i]
					# Calculate adjacent points.
					points = [[c,(d+1)%8],[c-1,d],[c,(d-1)%8]] # Confirmed to correctly calculate adjacent points.
					#print([c,d])
					#print(points,"point2")
					# Search for points in unOccup to see if any moves are available.
					result = searchForMoves(points, unOccup)
					if (result == False):
							return False

					#print("2",result)
					i = i+1
					#return result
	#print(i,"star")
	#print(result)

	return result


def movePiece(win, ptList, circle_index, cColor, Circles, Player, Occup, unOccup):#(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup):
	# this function performs a valid move for a Player (1 or 2) and updates the relevant lists
	# it uses the random function to make a valid move for Player 2 (the computer)
	# win is the GraphWin object, ptList is defined in drawBoard(), cColor is the color of pieces,
	# Occup is a list of occupied locations by the Player, linesOccup is a list of lines (mills)
	# of the Player, Circles is a list of the circles (pieces) and unOccup is a list of unOccup locations

	occupiedPoint = False

	print('movePiece() called')
	while True:
		pt = win.getMouse()
		nn, minDist, pt_index = findNN(pt, ptList)


		'''#test statements
		print('Clicked at: ', pt)
		print('Nearest point: ', nn)
		print('Distance: ', minDist)'''

		#if distance is too large, a circle will not be placed
		if minDist > 20:
			print('Distance too great. Did not place circle')
			continue


		#if all circles have not been placed (each player has 12), continue to allow user to draw circles for player
		elif len(Circles) < 12:

			#This loop is supposed to check the list unOccup (a list of unoccupied points) and if it
			#matches a spot, draw the circle
			for k in range(len(unOccup)):
					if unOccup[k] == pt_index:
						print('No object here')
						print(pt_index)

						circ = Circle(nn, 20)
						circ.setFill(cColor)
						Circles.append(circ)

						#print statements for test purposes
						print('circles list length: ', len(Circles))
						print('Circle Object: ', Circles[circle_index])
						print('circle_index: ', circle_index)
						Circles[circle_index].draw(win)

						#update Occup and unOccup
						Player.Occup.append(pt_index)
						try:
							unOccup.remove(pt_index)
							print('removed from unOcupp')
							return #returns nothing
						except:
							print('!!!could not remove from unOccup!!!')

					else:
						#print('grrr')
						continue

			continue

		#look for a click on the Player's own circle to attempt a move
		else:
			print('new wait for click called')
			pt = win.getMouse()
			nn, minDist, pt_index = findNN(pt, ptList)

			#index variable
			i = 0

			for k in range(len(Occup)):
				for j in Occup[k]:
					if (ptList[k][j].getX() == nn.x and ptList[k][j].getY() == nn.y):
						print('found another object at this location')

						for index in range(len(Circles)):
							a = Circles[i].getCenter()
							if (a.getX() == nn.x and a.getY() == nn.y):
								Circles[index].setOutline('red')







	#return [] # does not return anything



def drawBoard(win):
	# draws the board and populates the gobal list allLocs[] which contains all valid locations in ptList
	# returns ptList which is a 3x8 list of lists containing Point objects. At the top level it contains
	# the 3 squares (biggest first). At the second level, it contains the 8 Points that define
	# each square e.g. ptList[2][1] is the inner most square's 2nd Point. For each square, the bottom
	# left is the first Point
	bk = wSize/8
	ptList = []
	for i in range(1,4):
		ptList.append([Point(bk*i,bk*i), Point(bk*i,4*bk), Point(bk*i,bk*(8-i)),Point(4*bk,bk*(8-i)),
					   Point(bk*(8-i),bk*(8-i)),Point(bk*(8-i), 4*bk), Point(bk*(8-i),bk*i),Point(4*bk,bk*i)])
		pp = Polygon(ptList[-1])
		pp.setWidth(5)
		pp.setOutline(color_rgb(255,255,0))
		pp.draw(win)
		for j in range(8):
			allLocs.append([i-1,j])
	for i in range(8):
		ll = Line(ptList[0][i],ptList[2][i])
		ll.setWidth(5)
		ll.setFill(color_rgb(255,255,0))
		ll.draw(win)
	print(ptList[0][0])

	return ptList

def square(x):
	return x * x


def findNN(pt, ptList):
	# finds the nearest location to a point pt in ptList so that the user is only required
	# to click near the location to place/select/move a piece and not exactly on top of it
	# returns the distance d and index location nn in ptList of the nearest point


	#Finding the nearest node to where the user clicked. 'pt' is a variable that is initialized
	#in movePiece()
	#currently this doesn't work because ptList[] stores more than 2 Point Objects at ptList[x][y]

	distCheck = 0
	minDist = -1
	nn = ptList[0][0]
	pt_index = [0, 0]
	for x in range(len(ptList)):
		for y in range(len(ptList[x])):
			dist = sqrt(square(ptList[x][y].getX() - pt.getX()) + square(ptList[x][y].getY() - pt.getY()))

			if minDist == -1:
				minDist = dist

			elif dist == 0:
				nn = ptList[x][y]
				pt_index = [x, y]
				return nn, minDist, pt_index

			elif dist < minDist:
				minDist = dist
				nn = ptList[x][y]
				pt_index = [x, y]



	return nn, minDist, pt_index


def isLine(Occup, linesOccup):
	# Occup is a list of occupied locations by a Player and linesOccup are the Player's mills
	# returns True if a line (mill) has been made with the last move and updates linesOccup (mills)
	# otherwise returns False
	return False


def removePiece(win,ptList, Circles, Occup, unOccup):#Player,Occup,unOccup,linesOccup,Circles):
	# performs the removal of a piece as per the game rules
	# and updates Occup, unOccup and Circles lists

	print('removePiece() called')

	click = win.getMouse()
	nn, minDist, pt_index = findNN(click, ptList)

	i = 0

	#searches through Circles[] to find matching x,y value of a node
	#if it matches, remove that object
	for index in range(len(Circles)):
		a = Circles[i].getCenter()
		if (a.getX() == nn.x and a.getY() == nn.y):
			Circles[index].undraw()
			Occup.remove(pt_index)
			print('removed point from Occup. Updated Occupp[]: ', Occup)
			unOccup.append(pt_index)
			print('Appended new open location to unOccup. Updated unOccup[]: ', unOccup)
			print('removePiece() breaks')
			break
		else:
			i += 1



	return [] # does not return anything


def AImove(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup):
	# optional function for extra marks
	# replace the random function by this so that the computer (Player 2) performs an intelligent move
	return []




main()
