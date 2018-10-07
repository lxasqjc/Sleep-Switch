# Sleep-Switch
This is a personal hobbies project. I developed a Sleeping and Mood Switch, which utilize radio sensor (Walabot) to remotely detect human heart rate and automatically control smart devices based on analyses of the detected signal. It was built in host language of Python and corresponding SDK/API and utilized hardware including Raspberry Pi3, Walabot and relay (the project is published on Hackster platform

Link to project: https://www.hackster.io/user557511283/sleeping-and-mood-switch-691e96 

===Sleep_Switch_v1.0.0===
-initialize code based on hello walabot
-modify accoarding to image features (1) and code examples (2) of C++ for breathing detect
	(1) http://api.walabot.com/_features.html
	(2) http://api.walabot.com/_sample.html
-a modified breath detection code for python from C++, if can not debug could consider use C++ version
-when debuging checking comments start with "NOTE:" 

===Sleep_Switch_v1.0.1===
-debug calibration from given example .py codes
-use array to save each energy get from wlbt
-implement a timer to control circle
-note where to place calibration and need to put right before judging condition

===Sleep_Switch_v1.0.2===
-rewrite screen output to write to txt file, so could collect and analysis data

===Sleep_Switch_v1.0.3===
-fed analyzed sleeping criteria in: mean < 0.02, max <0.02, min <0.01, std <0.01

===Sleep_Switch_v1.0.3===
-raspberry pi version
-add light control after screen out
-adjust for test print every 5s and judge every 10s
