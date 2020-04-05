## IMPORTNG PYTHON MODULE

import pyttsx3 

print("\n\n*******************************TEXT TO SPEECH***************************\n")
print("*******READING TEXT FROM TERMINAL**********")

# USER INPUT
txt = str(input("Enter Your Text\n"))


res = pyttsx3.init()   # object creation


# say() function on the engine that passing input text to be spoken

res.say(txt) 

# runAndWait() function, it processes the voice commands. 

res.runAndWait() 


## if you want the text from the file

print("\n********READING TEXT FROM FILE***********")
print("\n****Now Listen your Text File******")

output = pyttsx3.init()

#READING FROM THE FILE

with open('textFile.txt') as f:
	lines = f.readlines()

 
output.say(lines)
output.runAndWait()	


