import numpy as np
import copy
matrix = np.fromfile("matrix.dta", sep="-").tolist()
alfa = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def initMatrix():
	global matrix
	matrix = []
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
	npmatrix = np.array(matrix)
	npmatrix.tofile("matrix.dta", "-")
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
		editedHist.append(edited)
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
	divide = int(raw_input("divide by length?(1=true):"))
	npmatrix = np.array(matrix)
	sum = np.dot(npmatrix, np.full(len(matrix[0]),1))
	if divide == 1:
		npmatrix = np.array(matrix)/np.hypot(sum,len(matrix[0]))
	for i in range(0,grad-1):
		npmatrix = np.dot(npmatrix, npmatrix)
	print npmatrix
	print "sum of original: "  + str(sum)
	sum = np.dot(npmatrix, np.full(len(matrix[0]),1))
	print "sum of potens: " + str(sum)
	sum = sum.tolist()
	print "highest priority: " + str(alfa[sum.index(max(sum))])
	
def meny():
	print "1. input matrix"
	print "2. display matrix"
	print "3. primsAlgorithm"
	print "4. djikstrasAlgorithm"
	print "5. dot operator"
def handlemeny():
	inp = int(raw_input("Command(1-5): "))
	if inp == 1:
		initMatrix()
	elif inp == 2:
		displayMatrix(matrix)
	elif inp == 3:
		primsAlgorithm()
	elif inp == 4:
		dijkstrasAlgorithm()
	elif inp == 5:
		opphoyd()
	meny()
	handlemeny()
meny()
handlemeny()


