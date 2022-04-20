def centimeters():
	x = int(input("Enter the number of centimeters you want to turn into bricks: "))
	y = x / 30
	z = round(y,1)
	print(str(z) + " is the amount of bricks.")

def meters():
	x = int(input("Enter the number of meters you want to turn into bricks: "))
	y = x / 0.3
	z = round(y,1)
	print(str(z) + " is the amount of bricks.")

def milimeters():
	x = int(input("Enter the number of milimeters you want to turn into bricks: "))
	y = x / 300
	z = round(y,1)
	print(str(z) + " is the amount of bricks.")

def feets():
	x = int(input("Enter the number of foot you want to turn into bricks: ")) * 0.3048
	y = x / 0.3
	z = round(y,1)
	print(str(z) + " is the amount of bricks.")

def inches():
	x = int(input("Enter the number of foot you want to turn into bricks: ")) * 2.54
	y = x / 30
	z = round(y,1)
	print(str(z) + " is the amount of bricks.")

w = int(input("If you want centimeters, write 0, meters, write 1, milimeters, write 2, feet, write 3 and inches, write 4. "))
if w == 0:
	centimeters()
elif w == 1:
	meters()
elif w == 2:
	milimeters()
elif w == 3:
	feets()
elif w == 4:
	inches()