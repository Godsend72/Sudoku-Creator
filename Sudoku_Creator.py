import Tkinter
import tkFileDialog
import tkFont
import random
import Image, ImageDraw
from datetime import datetime

import doctest



class vector2:  # class to hold x and y coordinates
	def __init__(self, x, y):
		"""This function initiates the x and y
		>>> test = vector2(5,5)
		>>> type(test)
		<type 'instance'>
		>>> test.x + test.y
		10
		"""
		self.x = x
		self.y = y


#functio that creates empty field Nx9
def clearfield(n):
	"""This function returns a list of n lists with 9 zeros
	>>> clearfield(1)
	[[0, 0, 0, 0, 0, 0, 0, 0, 0]]
	>>> type(clearfield(2))
	<type 'list'>
	>>> len(clearfield(3))
	3
	"""
	grid = []
	for i in range(n):
		grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
	return grid


def generatetop():
	"""This function randomly generates the 
	   middle and bottom left side 
		>>> type(generatetop())
		<type 'list'>
	   """
    # create grid with 3 rows and 9 cols
	grid = clearfield(3)
	for i in range(3):  # rows
		for j in range(9):  # column
			# reset the number list each iteration
			numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

			# remove numbers that already exist in the column
			for k in range(3):
				if grid[k][j] in numbers:
					numbers.remove(grid[k][j])

			# remove numbers that already exist in the row
			for l in range(9):
				if grid[i][l] in numbers:
					numbers.remove(grid[i][l])

			# remove numbers that already exist in the 3x3 grid
			for m in range(3):  # rows
				if j < 3:
					for n in range(3):  # cols
						if grid[m][n] in numbers:
							if grid[m][n] in numbers:
								numbers.remove(grid[m][n])
				elif j > 2 and j < 6:
					for n in range(3, 6):
						if grid[m][n] in numbers:
							if grid[m][n] in numbers:
								numbers.remove(grid[m][n])
				elif j > 5:
					for n in range(6, 9):
						if grid[m][n] in numbers:
							if grid[m][n] in numbers:
								numbers.remove(grid[m][n])

			# randomly select a number from available numbers
			if len(numbers) > 0:
				index = random.choice(numbers)
				grid[i][j] = index
			else:
				# if we ran out of numbers but still have empty field, return false
				return []
	# if successful return the grid
	return grid


def generateleft(grid):
	"""This function randomly generates the 
	   middle and bottom left side 
	   >>> type(generateleft(clearfield(9)))
	   <type 'list'>
	   """
	temp = clearfield(6)
	grid += temp
		
	for i in range(3,9):  # rows
		for j in range(3): # column
			# reset the number list each iteration
			numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			
			# remove numbers that already exist in the column
			for k in range(9):
				if grid[k][j] in numbers:
					numbers.remove(grid[k][j])

			# remove numbers that already exist in the row
			for l in range(3):
				if grid[i][l] in numbers:
					numbers.remove(grid[i][l])
					
			# remove numbers that already exist in the 3x3 grid	
			for m in range(3):
				if i > 2 and i < 6:
					for n in range(3, 6):
						if grid[n][m] in numbers:
							numbers.remove(grid[n][m])

				elif i > 5:
					for n in range(6, 9):
						if grid[n][m] in numbers:
							numbers.remove(grid[n][m])
							
			# randomly select a number from available numbers
			if len(numbers) > 0:
				index = random.choice(numbers)
				grid[i][j] = index
			else:
				# if we ran out of numbers but still have empty field, return false
				#return grid
				return []
	# if successful return the grid
	return grid





def generatebottom(grid):
	"""This function randomly generates the bottom side
		>>> type(generatebottom(clearfield(9)))
		<type 'list'>
		"""
		
	for i in range(6,9):  # rows
		for j in range(3,9): # column
			# reset the number list each iteration
			numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			
			# remove numbers that already exist in the column
			for k in range(9):
				if grid[k][j] in numbers:
					numbers.remove(grid[k][j])

			# remove numbers that already exist in the row
			for l in range(9):
				if grid[i][l] in numbers:
					numbers.remove(grid[i][l])
					
			# remove numbers that already exist in the 3x3 grid	
			for m in range(6,9):
				if j > 2 and j < 6:
					for n in range(3, 6):
						if grid[m][n] in numbers:
							numbers.remove(grid[m][n])

				elif j > 5:
					for n in range(6, 9):
						if grid[m][n] in numbers:
							numbers.remove(grid[m][n])
							
			# randomly select a number from available numbers
			if len(numbers) > 0:
				index = random.choice(numbers)
				grid[i][j] = index
			else:
				# if we ran out of numbers but still have empty field, return false
				#return grid
				return []
	# if successful return the grid
	return grid





def generateright(grid):
	"""This function randomly generates the right side 
		>>> type(generateright(clearfield(9)))
		<type 'list'>
		"""
	for i in range(3,6):  # rows
		for j in range(3,9): # column
			# reset the number list each iteration
			numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			
			# remove numbers that already exist in the column
			for k in range(9):
				if grid[k][j] in numbers:
					numbers.remove(grid[k][j])

			# remove numbers that already exist in the row
			for l in range(9):
				if grid[i][l] in numbers:
					numbers.remove(grid[i][l])
					
			# remove numbers that already exist in the 3x3 grid	
			for m in range(3,6):
				if j > 2 and j < 6:
					for n in range(3, 6):
						if grid[m][n] in numbers:
							numbers.remove(grid[m][n])

				elif j > 5:
					for n in range(6, 9):
						if grid[m][n] in numbers:
							numbers.remove(grid[m][n])
							
			# randomly select a number from available numbers
			if len(numbers) > 0:
				index = random.choice(numbers)
				grid[i][j] = index
			else:
				# if we ran out of numbers but still have empty field, return false
				return []
	# if successful return the grid
	return grid








def genGrid(win):
	"""This function creates a canvas
	   and draws lines to create a grid 
	   >>> win = Tkinter.Tk()
	   >>> type(genGrid(win))
	   <type 'instance'>
	   >>> win.destroy()
	   """
	# recreate the canvas
	canvas = Tkinter.Canvas(win, bg="white", height=500, width=500)

	# vertical data
	vStart = vector2(25, 25)
	vEnd = vector2(25, 475)

	# horizontal data
	hStart = vector2(25, 25)
	hEnd = vector2(475, 25)

	# grid creation
	for i in range(10):
		if i == 3 or i == 6:
			canvas.create_line(vStart.x, vStart.y, vEnd.x, vEnd.y, fill="red")
			canvas.create_line(hStart.x, hStart.y, hEnd.x, hEnd.y, fill="red")
		else:
			canvas.create_line(vStart.x, vStart.y, vEnd.x, vEnd.y)
			canvas.create_line(hStart.x, hStart.y, hEnd.x, hEnd.y)
		vStart.x += 50
		vEnd.x += 50
		hStart.y += 50
		hEnd.y += 50

	canvas.place(relx=0, rely=0)
	return  canvas



def genPuzzle():  # function that creates the puzzle
	"""This function calls other functions to create the puzzle
		>>> type(genPuzzle())
		<type 'list'>
		>>> len(genPuzzle())
		9
		"""
	# initiate every field to zero
	finish = False
	stageOne = True
	stageTwo = False
	stageThree = False

	while finish == False:
		while stageOne == True:
			top = []
			while len(top) == 0:
				top = generatetop()


			left = []
			counter = 0
			while len(left) == 0:
				left = generateleft(top)
				counter += 1
				if len(left) > 0:
					stageOne = False
					stageTwo = True
				if counter > 200: # if the function failes 200 times to find the left field break, and start over
					break


		bottom = []
		counter = 0
		while stageTwo == True:
			bottom = generatebottom(left)
			counter += 1
			if len(bottom) > 0:
				stageTwo = False
				stageThree = True
				#finish = True
			if counter > 200:  # if the function failes 200 times to find the left field break, and start over
				stageTwo = False
				stageOne = True
				break


		right = []
		counter = 0
		while stageThree == True:
			right = generateright(bottom)
			counter += 1
			if len(right) > 0:
				stageThree = False
				finish = True
			if counter > 200: # if the function failes 200 times to find the left field break, and start over
				stageThree = False
				stageOne = True
				break
	return  right





def removenumbers(puzzle):
	for i in range(len(puzzle)):
		for j in range(12):
			num = range(9)
			k = random.choice(num)
			puzzle[i][k] = 0
			del num[k]
	return puzzle






def drawPuzzle(puzzle, canvas):
	"""This function draws the numbers on te grid
	>>> win = Tkinter.Tk()
	>>> type(drawPuzzle([],genGrid(win)))
	<type 'NoneType'>
	
	>>> drawPuzzle([],genGrid(window))
	
	>>> win.destroy() # Here we do not expect anything
	
	
	 """
	# create the font size 20
	m_font = tkFont.Font(size=20)
	m_font.config(weight='bold')
	
	# draw the numbers on the grid
	rowPos = 50
	for i in range(len(puzzle)):
		colPos = 50
		for j in range(len(puzzle[i])):
			if puzzle[i][j] != 0:
				# draw the number to canvas
				canvas.create_text(colPos, rowPos, text=puzzle[i][j], font=m_font)
            # move to next column
			colPos += 50
		# move to next row
		rowPos += 50



def create(win):
	"""This function is called when the Gererate button is pressed
	>>> create(window)
	
	"""
	global puzzleField
	global canvas
	# generate a puzzle
	puzzleField = genPuzzle()
	finalPuzzle = removenumbers(puzzleField)
	# generate a canvas with the grid
	canvas = genGrid(win)
	# draw the puzzle
	drawPuzzle(finalPuzzle, canvas)
	return finalPuzzle


def save(puzzle): 
	""" This function saves the puzzle to txt file
	>>> save(genPuzzle())
	
	Nothing is expected as a return
	"""
	ftype = [("Image", "*.ps"), ("Text files", "*.txt")]
	fname = "sudoku"+str(datetime.now().strftime(' %Y-%m-%d %H:%M:%S'))
	filename = tkFileDialog.asksaveasfilename(filetypes=ftype, initialfile=fname)

	if filename.endswith(".txt"):
		text_file = open(filename, "w")
		for num in range(len(puzzle)):
			text_file.write(" %s " % puzzle[num] + "\n")
		text_file.close()

	elif filename.endswith(".ps"):
		canvas.postscript(file=fname, colormode='color')




# window creating
window = Tkinter.Tk()
window.title("Sudoku Creator")
window.geometry("500x550")
window.resizable(False, False)

# create whole puzzle
puzzleField = []
canvas = Tkinter.Canvas(window, bg="white", height=500, width=500)
create(window)


# doctest.testmod()

# create buttons
button_generate = Tkinter.Button(window, text="Generate", command=lambda: create(window), bg="white")
button_save = Tkinter.Button(window, text="Save", command=lambda: save(puzzleField), bg="white")


# place everything on the screen
button_generate.place(relx=0.2, rely=0.93)
button_save.place(relx=0.6, rely=0.93)
window.mainloop()
