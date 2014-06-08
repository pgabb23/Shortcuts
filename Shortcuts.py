# SHORTCUTS
# By: Patrick Gabbidon & Jacob [insert last name here]
#
# This Python Script when executed brings up a menu of various mini tutorials for GitHub, Python..

#Importations
import sys, os

#Introduction
print "Welcome to Shortcuts v0.0"
print "Created June 7, 2014"
print

#Variable Declaration
choice = ''
git_choice = ''
# Functions
def menu():
	print "MENU"
	print "Please choose one of the following mini tutorials options ( 1-5 or x to exit): "
	print "1 - GitHub"
	print "x - exit"
#	choice = raw_input()
#	if choice == 'x':
#		sys.exit()

def GitMenu():
		print "Please choose one of the following options (0-3): "
		print "   1 - How to Push to Github? "
		print "   2 - How to pull from Github? "
		print "   3 - Help "
		print "   0 - return to main menu"
#		git_choice = raw_input()
#		if git_choice == '0':
			

# Main
while choice != 'x':
	menu()
	choice = raw_input().lower()
	if choice == '1':
		GitMenu()
		git_choice = raw_input()
		if git_choice == '1':
			print
			print "Commands are as follows:"
			print "  $ git add -A"
			print "  $ git commit -m \"insert message here\" "
			print "  $ git push"
			print 
			
		elif git_choice == '2':
			print 
			print "Commands are as follows: "
			print "  $ git push"
			print
				
		elif git_choice != '1' and git_choice != '0' :
			print "\n Not a valid choice"
	elif choice == 'x':
		sys.exit()
		
		
		
		
		
		
		