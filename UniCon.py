from math import *

def mainMenu():
	print("(1) Temperature")
	print("(2) Light")
	print("(3) Volume")
	print("(4) Distance")
	print("(5) Exit")
	while True:
		try:
			selection=int(input("Enter choice: "))
			if selection==1:
				Temp()
				break
			elif selection==2:
				Ligh()
				break
			elif selection==3:
				Vol()
				break
			elif selection==4:
				Dist()
				break
			elif selection==5:
				exit()
				break
			
			else:
				print("Invalid selection. Enter 1-5")
				mainMenu()
		except ValueError:
			print("Invalid Selection")
	exit


def Temp():
	print("(1) Celcius to Farenheit?")
	print("(2) Farenheit to Celsius?")
	print("(3) Return to main menu.")
	while True:
		try:
			tselect=int(input("Enter choice: "))
			if tselect==1:
				celtofer()
				break
			elif tselect==2:
				fertocel()
				break
			elif tselect==3:
				mainMenu()
		except ValueError:
			print("Invalid Selection")
	exit

def Ligh():
	print("(1) Frequency to Wavelength?")
	print("(2) Wavelength to Farenheit?")
	while True:
		try:
			Lselect=int(input("Enter choice"))
			if Lselect==1:
				FtoW()
				break
			elif Lselect==2:
				WtoF()
				break
			elif Lselect==3:
				exit()
				break
		except ValueError:
			print("Invalid Selection.")
	exit
	
def celtofer():
	cel=float(input("Enter Celsius Value: "))
	print("\n Ferenheit Value:              " + str((cel * 1.8) + 32))
	print("\n The Celsius value of " + str(cel) + " is equal to " + str((cel * 1.8) + 32) + " degrees Celsius\n")
	if (cel <= 0): 
			print( "Below Freezing Point")
	else:
			print("Above Freezing Point")
	Temp()

def FtoW():
	freq=float(input("Enter Frequency: "))
	print("n\ Wavelength is 				" str((freq)))

# main routine
mainMenu()

