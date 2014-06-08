# SHORTCUTS
# By: Patrick Gabbidon
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


# Functions
def menu():
	print "MENU"
	print "Please choose one of the following mini tutorials options ( 1-5 or x to exit): "
	print "1 - GitHub Commands"
	print "2 - Common Linux Commands"
	print "x - exit"

def GitMenu():
	print "Please choose one of the following options (0-3): "
	print "   1 - How to Push to Github? "
	print "   2 - How to pull from Github? "
	print "   3 - General Help "
	print "   0 - Return to Main Menu"

def LinuxMenu():
	print "Please choose one othe following options (0-5): "
	print "   1 - How to view and change directories?"
	print "   2 - How to install Guest Additions or Parallel Tools?"
	print "   3 - How to use Vim and Nano?"
	print "   4 - to be added"
	print "   5 - to be added"
	print "   0 - Return to Main Menu"


# Main Loop
while choice != 'x':
	git_choice = ''
	menu()
	choice = raw_input().lower()
	if choice == '1':
		while git_choice != '0': 
			GitMenu()
			git_choice = raw_input()
			print
		
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
				print "  $ git pull"
				print
			
			elif git_choice == '3':
				print
				print "When first starting on a project make sure to clone directory first with: "
				print "  $ git clone 'url here' "
				print
				print "Also remember Github applications are for noobs, using the terminal is where its at"
				print 
			
			elif git_choice == '0':
				print
				break
				
			else:
				print "\n Not a valid choice"
				print
				
	elif choice == '2':
		while git_choice != '0': 
			LinuxMenu()
			git_choice = raw_input()
			print
		
			if git_choice == '1':
				print
				print "To view current directories use the command: "
				print "  $ ls"
				print "To change from the current directory use the 'cd' command: "
				print "  example -  $ cd Documents"
				print 
				
			elif git_choice == '2':
				print 
				print "To install Guest Additions for Virtual Box follow commands below: "
				print "  $ apt-get update && apt-get install -y linux-headers-$(uname -r) "
				print "  $ cp /media/cd-rom/VBoxLinuxAdditions.run /root/"
				print "  $ chmod 755 /root/VBoxLinuxAdditions.run"
				print "  $ cd /root"
				print "  $ ./VBoxLinuxAdditions.run"
				print "done. "
				print 
				print " To install Parallel Tools for Parallels follow commands below: "
				print "  $ apt-get update && apt-get install -y linux-headers-$(uname -r)"
				print "  $ cd /media/cdrom0"
				print "  $ cp -r install installer/ kmods/ tools/ version /tmp"
				print "  $ cd /tmp "
				print "  $ ./install"
				print "done."
				print
			
			elif git_choice == '3':
				print
				print "Using vim"
				print "   "
				print
				print "Using nano"
				print 
			
			elif git_choice == '0':
				print
				break
				
			else:
				print "\n Not a valid choice"
				print

	
	elif choice == 'x':
		sys.exit()
		
		
	else:
		print "\n Not a valid choice"
		print	
		
		
		
		