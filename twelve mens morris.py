# CITS1401 Semester 1 2015, Project 2
# Student 1 Name:    Harrison Marley    Student no: 21522889
# Student 2 Name:    Matt Cooper        Student no: 20933403
# Twelve Men's Morris

from graphics import *
from random import *
from math import *


wSize = 600
allLocs = []

class Player:
	def __init__(self,Colour, Number):
		self.blocked = False
		self.Circles = [] # List of player's Total number of pieces.
		self.cColour = Colour
		self.Occup = [] # list of locations of player's pieces.
		self.Number_of_mills = 0
		self.Number = Number
		self.linesOccup = [] # Location of player's mills
		self.occupOld = []
		turn = 0

	#matches occupOld to Occup for use in detecting mills
	def matchOccup(self):
		self.occupOld = self.Occup




def main():
	# controls the flow of the program, allows the players to put their pieces and then move them,
	# alternately, if a mill is made, invites the player to remove opponents piece and decides which
	# player has won. Uses the random function for Player 2 (the computer)
	win = GraphWin('QAT',wSize,wSize)
	win.setBackground('green')
	win.setCoords(0,0,wSize,wSize)
	ptList = drawBoard(win)
	center = Point(300, 30)

	print(len(ptList), len(ptList[0]))
	print('allLocs list: ', allLocs)


	#unOccup is a list of locations and is deleted from/added to as locations become taken or available
	unOccup = list(allLocs)

	#initialising Player class with the
	Player_1 = Player("white", 1)
	Player_2 = Player("black", 2)
	#these index variables are used to increment through the Circles list after every turn so that a new circle will be drawn
	#or else a graphics error may be raised
	Player_1_index = 0
	Player_2_index = 0


	Player_turn = 1
	while True:
		if Player_turn == 1:
			turnLabel = Text(center, 'Player One Turn')
			turnLabel.draw(win)
			movePiece(win, ptList, Player_1_index, Player_1.cColour, Player_1.Circles, Player_1, Player_2.Occup, unOccup)
			if blocked(Player_2.Occup, unOccup) == True:
				print('Player 2 blocked. Game Over')
				break
			#increment index so circles list will not attempt to draw the same circle twice which will raise an error
			Player_1_index += 1
			turnLabel.undraw()

			if isLine(Player_1.Occup, Player_1.occupOld) == True:
				turnLabel = Text(center, 'you made a mill! Click to remove an enemy piece')
				turnLabel.draw(win)
				print('Mill detected')
				removePiece(win, ptList, Player_2.Circles, Player_2.Occup, unOccup,Player_2)
				Player_2.matchOccup()
				turnLabel.undraw()
			else:
				print('No mill')
			if Player_1_index > 11:
				Player_1_index = 11
			Player_turn -= 1

		else:
			turnLabel = Text(center, 'Player Two Turn')
			turnLabel.draw(win)
			print('This should be an AI move')
			movePiece(win, ptList, Player_2_index, Player_2.cColour, Player_2.Circles, Player_2, Player_1.Occup, unOccup)
			if blocked(Player_2.Occup, unOccup) == True:
				print('Player 2 blocked. Game Over')
				break
			#increment index so circles list will not attempt to draw the same circle twice which will raise an error
			Player_2_index += 1
			turnLabel.undraw()
			if isLine(Player_2.Occup, Player_2.occupOld) == True:
				turnLabel = Text(center, 'you made a mill! Click to remove an enemy piece')
				turnLabel.draw(win)
				print('Mill detected')
				removePiece(win, ptList, Player_1.Circles, Player_1.Occup, unOccup, Player_1)
				Player_1.matchOccup()
			else:
				print('No mill')
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
# If such a point is found, the loop ends and the function returns False.
# This ultimately results in the "blocked" function concluding that the user is not blocked and the game can continue.

# If the function completes the loop iterations without finding an available opening,
# the function returns the variable "result" that stores the value "True", that signifies that the player is blocked.
# This ultimately results in the "blocked" function concluding that the user is blocked and the game ends.

	# Setting up the while loop that searched 'UnOccup' one point at a time.

	for j in range(len(points)):
		# Testing if the point for this loop is in 'UnOccup'.
		moveAvailable = (points[j] in unOccup)
		print(points)
		print(points[j])
		print(moveAvailable)
		# If the point is in 'UnOccup', end the function and return that the player is not blocked.
		if (moveAvailable == True):
			return True
	return False

def blocked(Occup, unOccup):
	# Written by Mathew Cooper 20933403 May 2015.
    # Occup is a list of occupied points/locations by a Player and unOccup are free locations
    # returns True if all pieces of the Player are blocked otherwise Fals
	points = []

	if ((len(Occup)) <= 0) or (len(unOccup)) > 24:		# If you have no pieces on the board then you should have either already gotten a game over message, or the game has just started.
		return False

	else:
		for j in range (len(Occup)):

			if((Occup[j][0] == 0)):
				#print(Occup[j][0])
				# Test each of the 3 possible co-ordinate points adjacent to a point in the outer square.
				# Establish point of interest.
				[a,b] = Occup[j]
				#print([a,b])
				# Calculate adjacent points.
				points = [[a,(b-1)%8], [a+1,b],[a,(b+1)%8]] # Confirmed to correctly calculate adjacent points.
				result = searchForMoves(points, unOccup)
				if (result == True):
					return False

				# Test each of the 4 possible co-ordinate points adjacent to a point in the middle square.
			elif((Occup[j][0] == 1)):
				#print(Occup[j][0])
				# Test each of the 3 possible co-ordinate points adjacent to a point in the outer square.
				# Establish point of interest.
				[c,d] = Occup[j]
				# Calculate adjacent points.
				points = [ [c+1,d], [c-1,d], [c,(d+1)%8],[c,(d-1)%8] ] # Confirmed to correctly calculate adjacent points.
				result = searchForMoves(points, unOccup)
				if (result == True):
					return False

			elif((Occup[j][0] == 2)):
				# Establish point of interest.
				[e,f] = Occup[j]
				# Calculate adjacent points.
				points = [[e,(f+1)%8],[e-1,f],[e,(f-1)%8]] # Confirmed to correctly calculate adjacent points.
				result = searchForMoves(points, unOccup)
				if (result == True):
					return False

		return True

def movePiece(win, ptList, circle_index, cColor, Circles, Player, Occup, unOccup):
	# this function performs a valid move for a Player (1 or 2) and updates the relevant lists
	# it uses the random function to make a valid move for Player 2 (the computer)
	# win is the GraphWin object, ptList is defined in drawBoard(), cColor is the color of pieces,
	# Occup is a list of occupied locations by the Player, linesOccup is a list of lines (mills)
	# of the Player, Circles is a list of the circles (pieces) and unOccup is a list of unOccup locations


	#print statement used for testing
	print('movePiece() called')
	while True:


		#if all circles have not been placed (each player has 12), continue to allow Player to draw circles
		if len(Circles) <= 6:
			#drawCircle will return false if the click was on an Occupied space or too far from a node
			#when this occurs the program will just wait for a proper click
			if drawCircle(win, ptList, circle_index, cColor, Circles, Player, Occup, unOccup) == False:
				continue
			else:
				return

		#if a player has all pieces on the board, wait for a click ON the player's piece
		else:

			print('Select a token you would like to move')
			pt = win.getMouse()
			nn, minDist, pt_index = findNN(pt, ptList)

			#this make sure a circle is not place if the mouse is near a node but still quite far away
			if minDist > 20:
				print('Distance too great. Did not select a circle')
				continue

			#all pieces have been used, so wait for a click on the player's circle
			for k in range(len(unOccup)):
					if unOccup[k] == pt_index:
						continue
					else:
						print('colour change reached')
						#this iterates through the relevant Player_x.Circles[] and finds a matching circle for the click location
						#turns the Circle red so the user knows it has been selected and is ready to move
						for index in range(len(Circles)):
							a = Circles[index].getCenter()
							if (a.getX() == nn.x and a.getY() == nn.y):
								Circles[index].setFill('red')

								#When drawCircle returns False, the click was not valid or on a space, so await another click
								if drawCircle(win, ptList, circle_index, cColor, Circles, Player, Occup, unOccup) == False:
									continue
								else:

									Circles[index].undraw()
									Player.Occup.remove(pt_index)
									Player.occupOld.remove(pt_index)
									unOccup.append(pt_index)

									return



	#return [] # does not return anything

def drawCircle(win, ptList, circle_index, cColor, Circles, Player, Occup, unOccup):

	print('drawCircle has been called, motherfucker')

	pt = win.getMouse()
	nn, minDist, pt_index = findNN(pt, ptList)


	print('minDist: ', minDist)

	if minDist > 20:
			print('Distance too great. Did not place circle')
			return False

	for k in range(len(unOccup)):
			if unOccup[k] == pt_index:

				circ = Circle(nn, 20)
				circ.setFill(cColor)
				Circles.append(circ)

				Circles[circle_index].draw(win)

				#update Occup and unOccup
				Player.occupOld = Player.Occup.copy()
				Player.Occup.append(pt_index)
				try:
					unOccup.remove(pt_index)
					print('removed from unOccup')
					return nn, pt_index
				except:
					print('!!!could not remove from unOccup!!!')

	return False

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

def isLineReturn(Occup, occupOld):

	CornerList = [[[0, 1], [0, 2], [0, 3]], [[0, 3], [0, 4], [0, 5]], [[0, 5], [0, 6], [0, 7]],[[0, 7], [0, 0], [0, 1]],  # Outer square corners.
				  [[1, 1], [1, 2], [1, 3]], [[1, 3], [1, 4], [1, 5]], [[1, 5], [1, 6], [1, 7]],[[1, 7], [1, 0], [1, 1]],  # Center square corners.
				  [[2, 1], [2, 2], [2, 3]], [[2, 3], [2, 4], [2, 5]], [[2, 5], [2, 6], [2, 7]],[[2, 7], [2, 0], [2, 1]]]  # Inner square corners.

	# This loop searches the a player's Occup list for any and all mills, it creates a list of mills called "linesOccup".
	linesOccupNew = []  # The list of mills after a player makes their move. This will be filled in by this function.

	if (len(Occup) < 3):
		linesOccupNew = []
		return linesOccupNew

	else:
		# A mill is created when 1 of 2 conditions is met.
		# Mill case 1: Constant x, Changing y.
		for i in range(len(Occup)):
			[x, y] = Occup[i]  # The method I am using to refer to the first co-ordinate of each pair in Occup.
			a = ([x, (y + 1) % 8] in Occup)
			b = ([x, (y + 2) % 8] in Occup)

			# Testing whether of not the second point and the third point of a mill are owned by the player.
			if ((a == True) and (b == True)):
				mill = [[x, y], [x, (y + 1) % 8], [x, (y + 2) % 8]]
				if ((mill in CornerList) == False):  # Making sure that the calculated mill is not a corner.
					print("MILL")
					print(mill)
					print("Occup")
					print(Occup)
					for point in mill:
						if point not in occupOld:
							linesOccupNew.append(mill)  # If a mill is present, add it to the list "linesOccupNew".

		# Mill case 2: Changing x (here called "q"),  Constant y (here called "w").
		for j in range(len(Occup)):
			[q, w] = Occup[j]  # The method I am using to refer to the first co-ordinate of each pair in Occup.
			c = ([(q + 1), w] in Occup)
			d = ([(q + 2), w] in Occup)
			# Testing whether of not the second point and the third point of a mill are owned by the player.
			if ((c == True) and (d == True)):
				mill = [[q, w], [(q + 1), w], [(q + 2), w]]
				print("MILL")
				print(mill)
				print("Occup")
				print(Occup)
				for point in mill:
					if point not in occupOld:
						linesOccupNew.append(mill)  # If a mill is present, add it to the list "linesOccupNew".

		return linesOccupNew

def isLine(Occup, occupOld):
	#print("THIS IS ALL THAT IS OCCUPIED")
	#print(Occup)
	newMills = isLineReturn(Occup, occupOld)
	#print("HERE ARE ALL 'NEW' MILLS RETURNED FROM MATTTHEW")
	print(newMills)
	if len(newMills) > 0:
		print("FUCKING FUCK YES")
		for mill in newMills:
			print(mill)
			#Occup.append(mill)
		print(Occup)
		return True
	else:
		print("NO")
		return False


def removePiece(win,ptList, Circles, Occup, unOccup, Player):#Player,Occup,unOccup,linesOccup,Circles):
	# performs the removal of a piece as per the game rules
	# and updates Occup, unOccup and Circles lists

	print('removePiece() called')
	circleDeleted = False

	while not circleDeleted:
		click = win.getMouse()
		nn, minDist, pt_index = findNN(click, ptList)

		if minDist > 20:
			print('Distance too great. Did not place circle')
			continue

		i = 0

		#searches through Circles[] to find matching x,y value of a node
		#if it matches, remove that object
		for index in range(len(Circles)):
			a = Circles[i].getCenter()
			if (a.getX() == nn.x and a.getY() == nn.y):

				if isLine(Player.Occup, Player.occupOld) == True:
					print('Cannot remove a piece in a mill')
					continue
				else:
					print('Length of Circles BEFORE undraw: ', len(Circles))
					Circles[index].undraw()
					print('Length of Circles AFTER undraw: ', len(Circles))
					Occup.remove(pt_index)
					print('removed point from Occup. Updated Occup[]: ', Occup)
					unOccup.append(pt_index)
					print('Appended new open location to unOccup. Updated unOccup[]: ', unOccup)
					print('removePiece() breaks')
					circleDeleted = True
					break
			else:
				i += 1



	return [] # does not return anything


def AImove(win,ptList,cColor,Player,Occup,linesOccup,Circles,unOccup):
	# optional function for extra marks
	# replace the random function by this so that the computer (Player 2) performs an intelligent move



	return []




main()
