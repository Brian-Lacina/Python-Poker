import random
import itertools

Rank = ["High Card", "Pair", "Two Pair", "Three of A Kind", "Strait", "Flush", "Full House" , "Quads", "Stait flush" , "ROYAL FLUSH!!!!"]
Rnum =["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
Rsuit=["c","d","h","s"]
def shuffle():
 SUITS = 'cdhs'
 RANKS = '23456789TJQKA'
 DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
 hand = random.sample(DECK, 5)
 return DECK
def bestHand(hand):
	w,h = 13, 4; 
	Matrix=[[0 for x in range(w)] for y in range(h)]
	for i in hand: 
		number = findNum(i[0])
		suit = findSuit(i[1])
		Matrix[suit][number]= 1
	high =  0
	if highCard(Matrix):
		high = 0
	if Pair(Matrix):
		high = 1
	if twoPair(Matrix):
		high = 2
	if trips(Matrix):
		high = 3
	if findStrait(Matrix):
		high = 4
	if fullHouse(Matrix):
		high = 6
	if Quads(Matrix):
		high = 7
	if findFlush(Matrix):
		high = 5
	if findStrait(Matrix)== True and findFlush(Matrix) == True:
		high =8

	return high

def  updateHigh(nums):
	if nums == 1: 
		return 	True
	return False
def  findNum(num):
	for i in range(len(Rnum)):
		if Rnum[i] == num:
			return i
	return 0 
def findSuit(suit):
	for i in range(len(Rsuit)):
		if Rsuit[i] == suit:
			return i 
	return 0



# needs to be able to find full house
def highCard(Matrix):
	High = 0
	
	for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
				High = i
	return True
def Pair(Matrix):
	  num = 0
	  numPair = 0
	  for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
                                num += 1
                                if num ==2:
					return True
                                        numPair+= 1
	  return False
def twoPair(Matrix):
	  numPair = 0
	  num =0
	  for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
                                num += 1
                                if num ==2:
                                        numPair+= 1
				if numPair == 2:
					return True
	  return False
def trips(Matrix):
	  numPair = 0
	  num = 0
	  for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
                                num += 1
                                if num ==3:
                                        return True
	  return False

def fullHouse(Matrix):
	numPair = 0
	num = 0
	numTrips = 0
        for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
                                num += 1
                                
		if num == 2:
			numPair +=1
		if num == 3:
			numTrips +=1

	if(numPair >= 1 and numTrips >= 1):
		return True
	return False
def Quads(Matrix):
	  numPair = 0
	  num = 0 
	  for i in range(len(Matrix[0])):
                num = 0
                for j in range(len(Matrix)):
                        if Matrix[j][i]== 1:
                                num += 1
                                if num ==4:
                                        return True
	  return False

#def findPair(Matrix):
#	high = 0
#	num = 0
#	highNum = 0
#	pair = 0
#	numPair= 0
#	numTrip = 0
#	highTrip = 0
#	fullHouse = 0	
#	highSec = 0
#	
#	for i in range(len(Matrix[0])):
#		num = 0
#		for j in range(len(Matrix)):
#			if Matrix[j][i]== 1:
#				num += 1
#				if num ==2:
#					numPair+= 1
#				if num == 3: 
#					numTrip += 1
#				if num == 4:	
#					numQuads = 1
#				if numTrip >=1 and numPair >= 1:
#					fullHouse += 1
#				if numTrip == 2:
#					fullHouse += 1
#				if  num >= highNum:
#					if( numPair >1):
#						highSec = high
	

def findStrait(Matrix):# works (i think)
	count = 0
	high = 0
	strait = 0
	temp = 0
	last = 0
	for i in range(len(Matrix[0])):
		temp = 0
                for j in range(len(Matrix)):
			if Matrix[j][i] == 1:
				if temp == 0:
					count += 1
					temp = 1
				if count >= 5 and last ==1:
					high = i
					strait = 1
		if(temp == 1):
			last = 1
		else:
			last = 0
			count = 0	
	if strait ==1:
		return True
	return False					
def findFlush(Matrix): # works (i think)
	num = 0
	flush =0
	high = 0
	for i in range(len(Matrix)):
                num = 0
                for j in range(len(Matrix[i])):
			if Matrix[i][j]:
				num+= 1
				if(num >= 5):
					flush = 1
					high = j
	if flush == 1:
		return True
	return False
#def findStraitFlush():
#def findRoyalFlush():

def main():
	pair = ["Ac", "3d", "2c", "Th", "Ad", "7s", "8d"] 
	twoPair = ["Ac", "2d", "2c", "Th", "Ad", "7s", "8d"]
	threePair = ["Ac", "2d", "2c", "Th", "Ad", "7s", "7d"]
	trips = ["Ac", "As", "2c", "Th", "Ad", "7s", "8d"]
	quads= ["Ah", "As", "Ac", "Th", "Ad", "7s", "8d"]
	fullHouse = ["Ac", "As", "2c", "2h", "Ad", "7s", "8d"]
	fuckFullHouse =  ["Ac", "As", "2c", "2h", "Ad", "Ks", "Kd"]
	strait = ["2c", "3c", "4d", "5c", "6h", "As" , "Td"]
	flush = ["2c", "4c" , "5c", "9d" , "2d", "7c" , "Jc"]
	deck= shuffle()
	hand =random.sample(deck, 7)
	print "Hand one " + str(hand)
	hand2= random.sample(deck,7)
	print "Hand two " + str(hand2)
	result = [0,0,0,0,0,0,0,0,0,0]
	numSim = 10000
	for i in range(numSim):
		deck = shuffle()
		hand = random.sample(deck,7)
		res = bestHand(hand)
		result[res] += 1
	for i in range(len(result)):
		print str(Rank[i]) + ": " + str((result[i]/float(numSim)) * 100) 	
if __name__ == "__main__": main()
