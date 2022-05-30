"""
This module was generated by Vizconnect.
Version: 1.03
Generated on: 2014-03-17 10:44:55.466000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()

	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: initialize a new display
	_name = 'main_display'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: set some parameters
			VFOV = 60
			aspect = viz.AUTO_COMPUTE
			stereo = viz.OFF
			
			#VC: create the raw object
			_window.fov(VFOV,aspect)
			_window.stereo(stereo)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Generic', model='Custom Window')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('head'))

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'head_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			positionSensitivity = 1.0
			rotationSensitivity = 0.09
			debug = False
			
			#VC: create the raw object
			from vizconnect.util.virtual_trackers import MouseAndKeyboardWalking
			rawTracker[_name] = MouseAndKeyboardWalking(positionSensitivity=positionSensitivity, rotationSensitivity=rotationSensitivity, debug=debug)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Mouse and Keyboard Walking')

	#VC: initialize a new tracker
	_name = 'r_hand_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			scaleVelocityWithDistance = True
			extensionAccel = 80
			debug = False
			
			#VC: create the raw object
			from vizconnect.util.virtual_trackers import ScrollWheel
			rawTracker[_name] = ScrollWheel(scaleVelocityWithDistance=scaleVelocityWithDistance, extensionAccel=extensionAccel, debug=debug)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Mouse Scroll Wheel')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: apply offsets
			_link.postTrans([0.1, -0.1, 0.4])

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'r_hand_input'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			rawInput[_name] = viz.mouse
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Mouse Buttons')

	#VC: initialize a new input
	_name = 'keyboard'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			d = viz.add('directinput.dle')
			device = d.getKeyboardDevices()[index]
			rawInput[_name] = d.addKeyboard(device)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Keyboard')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()

	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()

	#VC: initialize a new transport
	_name = 'main_transport'
	if vizconnect.isPendingInit('transport', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['head_tracker'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			orientationTracker = vizconnect.getTracker('head_tracker').getNode3d()
			debug = False
			acceleration = 4.0
			maxSpeed = 10.44
			rotationAcceleration = 90.0
			maxRotationSpeed = 120.0
			autoBreakingDragCoef = 0.1
			dragCoef = 0.0001
			rotationAutoBreakingDragCoef = 0.2
			rotationDragCoef = 0.0001
			usingPhysics = False
			parentedTracker = False
			transportationGroup = None
			
			#VC: create the raw object
			from transportation import wand_magic_carpet
			rawTransport[_name] = wand_magic_carpet.WandMagicCarpet(	orientationTracker=orientationTracker,
																					debug=debug,
																					acceleration=acceleration,
																					maxSpeed=maxSpeed,
																					rotationAcceleration=rotationAcceleration,
																					maxRotationSpeed=maxRotationSpeed,
																					autoBreakingDragCoef=autoBreakingDragCoef,
																					dragCoef=dragCoef,
																					rotationAutoBreakingDragCoef=rotationAutoBreakingDragCoef,
																					rotationDragCoef=rotationDragCoef,
																					usingPhysics=usingPhysics,
																					parentedTracker=parentedTracker,
																					node=transportationGroup)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(transport):
					if rawInput['keyboard'].isButtonDown(17):# make=Generic, model=Keyboard, name=keyboard, signal=Key W
						transport.moveForward(mag=1)
					if rawInput['keyboard'].isButtonDown(31):# make=Generic, model=Keyboard, name=keyboard, signal=Key S
						transport.moveBackward(mag=1)
					if rawInput['keyboard'].isButtonDown(30):# make=Generic, model=Keyboard, name=keyboard, signal=Key A
						transport.moveLeft(mag=1)
					if rawInput['keyboard'].isButtonDown(32):# make=Generic, model=Keyboard, name=keyboard, signal=Key D
						transport.moveRight(mag=1)
					if rawInput['keyboard'].isButtonDown(45):# make=Generic, model=Keyboard, name=keyboard, signal=Key X
						transport.moveUp(mag=1)
					if rawInput['keyboard'].isButtonDown(44):# make=Generic, model=Keyboard, name=keyboard, signal=Key Z
						transport.moveDown(mag=1)
					if rawInput['keyboard'].isButtonDown(16):# make=Generic, model=Keyboard, name=keyboard, signal=Key Q
						transport.turnLeft(mag=1)
					if rawInput['keyboard'].isButtonDown(18):# make=Generic, model=Keyboard, name=keyboard, signal=Key E
						transport.turnRight(mag=1)
				rawTransport[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTransport(rawTransport[_name], _name, make='Virtual', model='WandMagicCarpet')
	
		#VC: set the pivot of the node
		if initFlag&vizconnect.INIT_PIVOTS:
			vizconnect.getTransport(_name).setPivot(vizconnect.getAvatar('main_avatar').getAttachmentPoint('head').getNode3d())

	#VC: set the name of the default
	vizconnect.setDefault('transport', 'main_transport')

	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()

	#VC: initialize a new tool
	_name = 'proxy'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			from tools import proxy
			rawTool[_name] = proxy.Proxy()
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['r_hand_input'].getState()&viz.MOUSEBUTTON_LEFT:# make=Generic, model=Mouse Buttons, name=r_hand_input, signal=Left Mouse Button
						tool.action1()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Proxy')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('r_hand'))

	#VC: initialize a new tool
	_name = 'grabber'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.display.stencil',1)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = False
			highlightMode = tools.highlighter.MODE_OUTLINE
			placementMode = tools.placer.MODE_POINT_AND_PLACE
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['r_hand_input'].getState()&viz.MOUSEBUTTON_LEFT:# make=Generic, model=Mouse Buttons, name=r_hand_input, signal=Left Mouse Button
						tool.grabAndHold()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('r_hand'))

	#VC: initialize a new tool
	_name = 'grabber2'
	if vizconnect.isPendingInit('tool', _name, initFlag, initList):
		#VC: init which needs to happen before viz.go
		if initFlag&vizconnect.INIT_PREVIZGO:
			viz.setOption('viz.display.stencil',1)
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: initialization code needed by the parameters
			import tools
			from tools import grabber
			from tools import highlighter
			
			#VC: set some parameters
			usingPhysics = False
			highlightMode = tools.highlighter.MODE_OUTLINE
			placementMode = tools.placer.MODE_POINT_AND_PLACE
			
			#VC: create the raw object
			rawTool[_name] = grabber.Grabber(usingPhysics=usingPhysics, usingSprings=usingPhysics, highlightMode=highlightMode, placementMode=placementMode, updatePriority=vizconnect.PRIORITY_ANIMATOR+3)
	
		#VC: init the mappings for the raw object
		if initFlag&vizconnect.INIT_MAPPINGS:
			#VC: per frame mappings
			if initFlag&vizconnect.INIT_MAPPINGS_PER_FRAME:
				#VC: get the raw input dict so we have access to signals
				import vizact
				rawInput = vizconnect.getConfiguration().getRawDict('input')
				#VC: set the update function which checks for input signals
				def update(tool):
					if rawInput['r_hand_input'].getState()&viz.MOUSEBUTTON_LEFT:# make=Generic, model=Mouse Buttons, name=r_hand_input, signal=Left Mouse Button
						tool.grabAndHold()
				rawTool[_name].setUpdateFunction(update)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTool(rawTool[_name], _name, make='Virtual', model='Grabber')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getTool(_name).setParent(vizconnect.getAvatar('main_avatar').getAttachmentPoint('r_hand'))

	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()

	#VC: initialize a new avatar
	_name = 'main_avatar'
	if vizconnect.isPendingInit('avatar', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			head = False
			rightHand = True
			leftHand = False
			torso = False
			lowerBody = False
			rightArm = False
			leftArm = False
			
			#VC: create the raw object
			# base avatar
			import vizfx
			avatar = vizfx.addChild('mark.cfg')
			avatar._bodyPartDict = {}
			avatar._handModelDict = {}
			avatar.visible(head, r'mark_head.cmf')
			avatar.visible(rightHand, r'mark_hand_r.cmf')
			avatar.visible(leftHand, r'mark_hand_l.cmf')
			avatar.visible(torso, r'mark_torso.cmf')
			avatar.visible(lowerBody, r'mark_legs.cmf')
			avatar.visible(rightArm, r'mark_arm_r.cmf')
			avatar.visible(leftArm, r'mark_arm_l.cmf')
			rawAvatar[_name] = avatar
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addAvatar(rawAvatar[_name], _name, make='WorldViz', model='Mark')
	
		#VC: init the gestures
		if initFlag&vizconnect.INIT_GESTURES:
			#VC: need to get the raw input dict so we have access to signals
			import vizact
			rawInput = vizconnect.getConfiguration().getRawDict('input')
			
			#VC: gestures for the avatar's r_hand
			import hand
			def initHand():
				sensor = hand.InputSensor()
				rawAvatar[_name].handSensor = sensor
				sensor.createHandRenderer = lambda *args,**kw: hand._InputDeviceRenderer(*args,**kw)
				def appliedGetData():
					#VC: set the mappings for the gestures
					if rawInput['r_hand_input'].getState()&viz.MOUSEBUTTON_LEFT:# make=Generic, model=Mouse Buttons, name=r_hand_input, signal=Left Mouse Button
						return (hand.GESTURE_FIST, False, False)# GESTURE_FIST
					#VC: end gesture mappings
					return (hand.GESTURE_FLAT_HAND,False,False)
				sensor.getData = appliedGetData
				return hand.AvatarHandModel(rawAvatar[_name], left=False, type=hand.GLOVE_5DT, sensor=sensor)
			rightHand = initHand()
			rawAvatar[_name]._bodyPartDict[vizconnect.AVATAR_R_HAND] = rightHand
			rawAvatar[_name]._handModelDict[vizconnect.AVATAR_R_HAND] = rightHand
			
			#VC: gestures may change the raw avatar, so refresh the raw in the wrapper
			vizconnect.getAvatar(_name).setRaw(rawAvatar[_name])
	
		#VC: init the animator
		if initFlag&vizconnect.INIT_ANIMATOR:
			# need to get the raw tracker dict for animating the avatars
			from vizconnect.util.avatar import animator
			from vizconnect.util.avatar import skeleton
			
			# get the skeleton from the avatar
			_skeleton = skeleton.CompleteCharactersHD(rawAvatar[_name])
			
			#VC: set which trackers animate which body part
			# format is: bone: (tracker, parent, degrees of freedom used)
			_trackerAssignmentDict = {
				vizconnect.AVATAR_HEAD:(vizconnect.getTracker('head_tracker').getNode3d(), None, vizconnect.DOF_6DOF),
				vizconnect.AVATAR_R_HAND:(vizconnect.getTracker('r_hand_tracker').getNode3d(), vizconnect.AVATAR_HEAD, vizconnect.DOF_POS),
			}
			
			#VC: create the raw object
			_rawAnimator = animator.Direct(rawAvatar[_name], _skeleton, _trackerAssignmentDict)
			
			#VC: set animator in wrapper (DO NOT EDIT)
			vizconnect.getAvatar(_name).setAnimator(_rawAnimator, make='Virtual', model='Direct')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getAvatar(_name).setParent(vizconnect.getTransport('main_transport'))

	#VC: set the name of the default
	vizconnect.setDefault('avatar', 'main_avatar')

	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')
	
	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_ADVANCED)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')

