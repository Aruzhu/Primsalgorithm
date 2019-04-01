import numpy as np
import copy
#matrix = [[0,5,3,9],
#		[5,0,1,4],
#		[3,1,0,6],
#		[9,4,6,0]]
matrix = []
alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def initMatrix():
	matrixpart = []
	x = int(input("X: "))
	y = int(input("Y: "))
	userinput = ""
	for i in range(0, y):
		matrixpart = []
		while len(userinput) != y:
			print "y="+str(i)
			userinput = str(raw_input("enter entire y: "))
			print(len(userinput))
		for part in userinput:
			matrixpart.append(int(part))
		matrix.append(matrixpart)
		userinput = ""
def displayMatrix(list):
	for part in list:
		print part
def displayAlfa(list):
	for a in list:
		print alfa[a]
def primsAlgorithm():
	staX = int(raw_input("start x:"))
	stoX = int(raw_input("stop x:"))
	answer = []
	edited = []
	atX = staX
	lateX = 0
	going = True
	while going:
		answer.append(atX)
		xLine = []
		for part in matrix:
			xLine.append(part[atX])
		
		if atX == stoX:
			going = False
			break
		
		print "xline: "+ str(xLine) + "		lateX " + str(lateX)
		edited = copy.copy(xLine)
		del edited[lateX]
		lateX = atX
		
		while min(edited) == 0:
			del edited[edited.index(min(edited))]
		if edited == []:
			print "ikke sammenhengende"
			break
		print "edited = " + str(edited) + "	min edited: " + str(min(edited))
		atX = xLine.index(min(edited))
		print "atx = " + str(atX)
	print answer
	displayAlfa(answer)
def dijkstrasAlgorithm():
	staX = int(raw_input("start x:"))
	stoX = int(raw_input("stop x:"))
	answer = []
	edited = []
	editedHist = []
	atX = staX
	lateX = 0
	length = 0
	going = True
	while going:
		answer.append(atX)
		xLine = []
		for part in matrix:
			xLine.append(part[atX])
		
		if atX == stoX:
			going = False
			break
		
		print "xline: "+ str(xLine) + "		lateX " + str(lateX) + "	length: " + str(length)
		edited = copy.copy(xLine)
		del edited[lateX]
		lateX = atX
		
		while min(edited) == 0:
			del edited[edited.index(min(edited))]
		for a in range(0,len(edited)):
			edited[a] += length
		editedHist.append(list(edited))
		displayMatrix(editedHist)
		if edited == []:
			print "ikke sammenhengende"
			break
		print "edited = " + str(edited) + "	min edited: " + str(min(edited))
		atX = xLine.index(min(edited)-length)
		length += min(edited)
		print "atx = " + str(atX) + "	alfa: " + str(alfa[atX])
	print answer
	displayAlfa(answer)
def opphoyd():
	grad = int(raw_input("grad?:"))
	npmatrix = np.array(matrix)
	for i in range(0,grad-1):
		npmatrix = np.dot(npmatrix, npmatrix)
	print npmatrix
initMatrix()
displayMatrix(matrix)
#primsAlgorithm()
#dijkstrasAlgorithm()
opphoyd()


