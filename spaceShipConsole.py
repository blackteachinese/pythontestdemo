#!/usr/bin/python
import time
shipName = "Nastrama"
captain = "Wallace"
locaiton = "Earth"
password = "Buttercpus"
pAttempt = raw_input("Enter your password: ")
while pAttempt != password:
	print "Password incrorrect! "
	pAttempt = raw_input("Enter your password: ")
print "Password correct. welcome to the " + shipName
print " "
print "The spaceship " + shipName + " is currently visiting " + locaiton + " . "
choice = ""
while choice != "/exit":
	print "What wounld you like to do, " + captain + "?"
	print " "
	print "a. Travel to another planet"
	print "b. Fire cannons"
	print "c. Open the airlock"
	print "d. Self-destruct"
	print "/exit to exit"
	print " "
	choice = raw_input("Enter your choice : ")
	if  choice == "a":
		dest = raw_input("Where wounld you like to go? ")
		print "Leaving " + locaiton
		print "Travelling to " + dest
		time.sleep(5);
		print "Arrived at " + dest
		locaiton = dest
	elif choice == "b" :
		print "Fireing cannons"
		time.sleep(1)
		print "BAND!"
		time.sleep(1)
	elif choice == "c" :
		print "Opening airlock"
		time.sleep(3)
		print "Airlock open"
		time.sleep(1)
	elif choice == "d" :
		confirm = raw_input("Are you sure you want the ship to Self-destruct?(y/n)")
		if confirm == "y" :
			print "Ship will Self-destruct in"
			print "3"
			time.sleep(1)
			print "2"
			time.sleep(1)
			print "1"
			time.sleep(1)
			print "Goodbye"
			print "BOOM"
			choice = "/exit"
	elif choice == "/exit" :
		print "Goodbye"

