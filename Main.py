
#init matrix
matrix = []
matrixpart = []
x = int(input("X: "))
y = int(input("Y: "))
userinput = ""
for i in range(0, y+1):
	matrixpart = []
	while len(userinput) != y:
		print "x="+str(i)
		userinput = str(raw_input("enter entire x: "))
		print(len(userinput))
	print userinput
	for part in userinput:
		matrixpart.append(int(part))
	matrix.append(matrixpart)
	userinput = ""

