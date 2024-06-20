import numpy as np


name= input('what is your name?\n')
print('your name has ' + str(len(name)) + ' Characters in it')
randomNumber = np.random.randint(1,9)
print(randomNumber)
#ask for the users name
print('Hello, What is the name of the city you grew up in?')
cityName = input()
print('What is the name of your pet? Or a friends pet?')
petsName = input()
#return a response 
print('You could call your band ' + cityName + ' ' +petsName)

