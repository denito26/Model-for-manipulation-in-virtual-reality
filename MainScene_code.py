import viz

import vizfx

import vizconnect

import vizinput

viz.go()

#Enable physics
viz.phys.enable()


vizconnect.go('newconfig.py')

env = vizfx.addChild('All_Resources/MainProjects.osgb')


wineB=env.getChild('wine_bottle.gltf')

bearT=env.getChild('orange_bear.gltf')

dustBin=env.getChild('dustBin.gltf')

wineB.collideBox()

bearT.collideBox()

dustBin.collideBox()

dustBin.enable(viz.COLLIDE_NOTIFY)


wineB.disable(viz.DYNAMICS)
bearT.disable(viz.DYNAMICS)
dustBin.disable(viz.DYNAMICS)




def onCollideBegin(e):
	print(e)
	if e.obj1 == dustBin:
		e.obj2.remove()

viz.callback(viz.COLLIDE_BEGIN_EVENT,onCollideBegin)


grabbableObjects=[wineB,bearT]



grabber = vizconnect.getRawTool('grabber')

grabber.setItems(grabbableObjects)

grabber2 = vizconnect.getRawTool('grabber2')

grabber2.setItems(grabbableObjects)


# Here we will collect the unique info for each person who enters our Model



import re

import os

pattern = "^[0-9]+$"


while True:
	person = vizinput.input("(1)Please enter an ID number! \n(2)Characters are not allowed! \n(3) If instructions 1 and 2 are correct and you cannot proceed, \nplease try again to type another number, since other user may be using the number you are typing already!")
	# Regex check	
	check = re.search(pattern, person)
	
	# Using the OS module to check if a file with the given ID from the participant is already used and created to store data
	path= ('D:/3D_Models_For_Vizard/All_Resources/collect_data/collected_data%s.txt' % person)

	isFile = os.path.isfile(path)

	print (isFile)			
	
	if check and not isFile:
		break
		

# Starting a timer for the participant while is using the Model and will be used when clicking items

saved_time = viz.tick()

# Creating a file with the respective USER ID Number in the end of the file collected_data("")

collected_data = open('collect_data/collected_data' +str(person)+'.txt','a')


def onGrab(e):
	elapsed_time = viz.tick() - saved_time
	if e.grabbed == wineB:
		data = 'Person ' + str(person) + ' grabbed wineB.\t'
		print('The Wine bottle is grabbed.')

	if e.grabbed == bearT:
		data = 'Person ' + str(person) + ' grabbed bearT.\t'
		print("The orange bear is grabbed.")
	#add elapsed time to data
	data = data + 'Elapsed time was: ' + str(round(elapsed_time,2)) + ' seconds\n'
	collected_data.write(data)


# This tool GRAB_EVENT is used to catch our function and saves the data to our file
from tools import grabber
viz.callback(grabber.GRAB_EVENT, onGrab)	

	

#Save data for tracking
tracking_position = open('collect_data/tracking_'+str(person)+'.txt', 'a')
 
#Get the tracking data.
def getPositionData():
	position = viz.MainView.getPosition()
	print(position)
	#Make a string out of the data. Making the first column rounded to the second element after the comma and that is the same for the other two collumns
	data = str(round(position[0],2))+ '\t'+ str(round(position[1],2))+'\t'+str(round(position[2],2))+ '\n'
	#Write it to the tracking file.
	tracking_position.write(data)

# The below is used to enable the function for the tracking position, this function vizact.onupdate is using 2 arguments:
# - the first should be a number, which means a priority 
# - the second one is the function to be called and enabled.
vizact.onupdate(1, getPositionData)

