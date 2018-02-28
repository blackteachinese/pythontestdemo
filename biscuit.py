#!/usr/bin/python
hasBiscuits = raw_input("Do you have any biscuits? yes or no. ")
if hasBiscuits == "yes" :
	print "They look delicious"
	willshare = raw_input("can i have one? ")
	if willshare == "yes":
		print "Thank you !"
	else :
		print "I guess computers don't eat biscuits anyway ..."
else :
	print "I don't believe you"