from __future__ import print_function
from sys import platform
from os import system
import WalabotAPI as wlbt



wlbt.Init()  # load the WalabotSDK to the Python wrapper
wlbt.SetSettingsFolder()  # set the path to the essetial database files
wlbt.ConnectAny()  # establishes communication with the Walabot

wlbt.SetProfile(wlbt.PROF_SENSOR_NARROW)  # set scan profile out of the possibilities
	# JC: replace PROF_SENSOR to PROF_SENSOR_NARROW
	# Sensor narrow: Lower-resolution images for a fast capture rate. Useful for tracking quick movement.
	# thus for heart rate
wlbt.SetDynamicImageFilter(wlbt.FILTER_TYPE_DERIVATIVE)  # specify filter to use
	#JC: replace FILTER_TYPE_MTI to FILTER_TYPE_DERIVATIVE
	#Moving Target Identification (MTI) filter, the Derivative filter is available for the specific frequencies typical of breathing.

## variables definition
## Walabot_SetArenaR - input parameters
minInCm = 30;
maxInCm = 150;
resICm = 1;
## Walabot_SetArenaTheta - input parameters
minIndegrees = -4;
maxIndegrees = 4;
resIndegrees = 2;
## Walabot_SetArenaPhi - input parameters
minPhiInDegrees = -4;
maxPhiInDegrees = 4;
resPhiInDegrees = 2;
##JC: here below modified from C++ breathing code, before use variables needs to be defined,  parameters accoarding to http://api.walabot.com/_features.html and http://api.walabot.com/_sample.html C++ breathing code
## Setup arena - specify it by Cartesian coordinates(ranges and resolution on the x, y, z axes); 
##  In Sensor mode there is need to specify Spherical coordinates(ranges and resolution along radial distance and Theta and Phi angles).
wlbt.SetArenaR(minInCm, maxInCm, resICm)
## Sets polar range and resolution of arena (parameters in degrees).
wlbt.SetArenaTheta(minIndegrees, maxIndegrees, resIndegrees)
## Sets azimuth range and resolution of arena.(parameters in degrees).
wlbt.SetArenaPhi(minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees)

wlbt.Start()  # starts Walabot in preparation for scanning
print ('hello')

while True:
	##JC: add calibrates based from C++ code
	##// calibrates scanning to ignore or reduce the signals
	wlbt.StartCalibration()
	while wlbt.GetStatus()[0] == wlbt.STATUS_CALIBRATING:
		wlbt.Trigger()
	Energy_current = wlbt.GetImageEnergy()
	#JC: replace GetSensorTargets to GetImageEnergy
	system('cls' if platform == 'win32' else 'clear')  # clear the terminal
	print('Energy_Current = ', Energy_current, '/n')



wlbt.Stop()  # stops Walabot when finished scanning
wlbt.Disconnect()  # stops communication with Walabot
