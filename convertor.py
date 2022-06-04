import math
from tkinter import *
import random

class Binary_Convertor():

	def __init__(self, number, num_of_bits=1, lister=[], str=''):
		self.number = number
		self.num_of_bits = num_of_bits
		self.lister = lister
		self.str = str

	def decimal_to_num_of_binary_convertor(self):

		while self.num_of_bits >= 1:
			if (math.log(self.number, 2) < self.num_of_bits):
				break
			self.num_of_bits += 1

	def decimal_to_binary_convertor(self):
		self.num_of_bits -= 1
		while self.num_of_bits >= 0:
			if (self.number - pow(2, self.num_of_bits) < 0):
				self.lister.append(0)
				self.num_of_bits -= 1
				continue

			self.number -= pow(2, self.num_of_bits)
			self.lister.append(1)
			self.num_of_bits -= 1

		for m in self.lister:
			self.str += str(m)
		return self.str


class Decimal_Convertor():

	def __init__(self, binary, count=0, sum=0):
		self.binary = binary
		self.count = count
		self.sum = sum

	def binary_to_decimal_convertor(self):

		for num in self.binary[::-1]:
			if (num == "1" or num == "0"):
				if (num == "1"):
					self.sum += math.pow(2, self.count)
					self.count += 1
				else:
					self.count += 1
			else:
				print("Please enter a binary number. That was not a binary number.")
				return 0
		return self.sum


class Hexadecimal_Convertor():

	def __init__(self):
		pass

	def decimal_to_hex_convertor(self, number):

		hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
		list = []
		x = 0
		first_num = 0
		for num in range(1, number + 1):
			x += 1
			if (x == 16):
				first_num += 1
				x = 0
		list.append(hex[first_num])
		list.append(hex[x])
		string = ""
		for num in list:
			string += num
		return string


class Decimal_Convertor2():

	def init(self):
		pass

	def hex_to_decimal_convertor(self, hex):
		hex_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
		num_count = 0
		decimal_count = 0
		list = []
		for letter in hex:
			list.append(letter)

		first_num, second_num = list

		for letter in hex_board:
			if first_num == letter:
				num_count += (decimal_count * 16)
			if (second_num == letter):
				num_count += decimal_count
			decimal_count += 1

		return num_count

root = Tk()
root.title("CSP Project")


slide_num = 1
score = 0
restart = False
denom = 0

def destroy():
	root.destroy()
	return 0

def calcRandom(num):

	binary_convertor = Binary_Convertor(num)
	binary_convertor.decimal_to_num_of_binary_convertor()
	return binary_convertor.decimal_to_binary_convertor()

def calcRandom2(num):
	decimal_convertor = Hexadecimal_Convertor()
	return decimal_convertor.decimal_to_hex_convertor(num)


x = random.randint(1, 255)
binary = calcRandom(x)
hex = calcRandom2(x)


def display_game():

	global canvas1
	global button
	global intro_text

	if(restart):
		canvas5.destroy()
		intro_text5.destroy()

	canvas1 = Canvas(root, width=350, height=300)
	canvas1.pack()
	intro_text = Label(root, text="Hello. Welcome to Convertor Craziness!!")
	intro_text.pack()
	canvas1.create_window(175, 100, window=intro_text)
	button = Button(root, text="Play", command= next_screen)
	button.pack()

def next_screen():
	global canvas2
	global e2
	global intro_text2
	global button2
	global score_tracker1

	canvas1.destroy()
	button.destroy()

	score_tracker1 = Label(text = f"You have guessed {score} out of {denom} right.")
	score_tracker1.pack()
	canvas2 = Canvas(root, width=350, height=300)
	canvas2.pack()
	e2 = Entry(root, width=100)
	e2.pack()
	e2.insert(0, "Type Your Answer: ")
	intro_text2 = Label(root, text= f"Question 1: what is {x} in Binary?")
	intro_text2.pack()
	canvas2.create_window(175, 200, window=e2)
	canvas2.create_window(175, 100, window=intro_text2)
	button2 = Button(root, text="Next Question", command= lambda : next_click(e2.get()))
	button2.pack()


def next_screen2():
	global canvas3
	global enter3
	global intro_text3
	global button3
	global score_tracker2
	global hex

	score_tracker1.destroy()
	canvas2.destroy()
	e2.destroy()
	intro_text2.destroy()
	button2.destroy()

	score_tracker2 = Label(text = f"You have guessed {score} out of {denom} right.")
	score_tracker2.pack()
	canvas3 = Canvas(root, width=350, height=300)
	canvas3.pack()
	enter3 = Entry(root, width=100)
	enter3.pack()
	enter3.insert(0, "Type 2 numbers/characters in CAPS: ")
	intro_text3 = Label(root, text= f"Question 2:  what is {x} in hexadecimal?")
	intro_text3.pack()
	canvas3.create_window(175, 200, window=enter3)
	canvas3.create_window(175, 100, window=intro_text3)
	button3 = Button(root, text="Next", command= lambda : next_click(enter3.get()))
	button3.pack()


def final_winner():
	global canvas5
	global intro_text5
	global score_tracker4
	global score

	score_tracker2.destroy()
	canvas3.destroy()
	enter3.destroy()
	intro_text3.destroy()
	button3.destroy()

	score_tracker4 = Label(text = f"You have guessed {score} out of {denom} right.")
	score_tracker4.pack()
	canvas5 = Canvas(root, width=350, height=300)
	canvas5.pack()
	if(score == 0):
		intro_text5 = Label(root, text= "Be sure to play again to sharpen your skills in converting decimal numbers to hexadecimal and binary numbers!!!!", font = "Helvitica")
		intro_text5.pack()
	elif(score == 1):
		intro_text5 = Label(root, text="Nicely Done. Please play again.", font="Helvitica")
		intro_text5.pack()
	else:
		intro_text5 = Label(root, text="WOW!!! Your conversion ability is out of this world. I can tell you have been practicing.", font="Helvitica")
		intro_text5.pack()
	canvas5.create_window(175, 100, window=intro_text5)
	no_button = Button(root, text = "Exit", command = destroy, width = 20, height = 10)
	no_button.pack()
	canvas5.create_window(200, 250, window = no_button)


def next_click(answer):
	global slide_num
	global score
	global denom
	global real_answer

	real_answer = answer

	game = [next_screen, next_screen2, final_winner][slide_num]

	if(slide_num == 1 and binary == str(real_answer).split(" ")[-1]):
		score += 1

	if(slide_num == 2 and hex == str(str(real_answer).split(" ")[-1])):
		score += 1

	slide_num += 1
	denom += 1
	return game()

display_game()
mainloop()
