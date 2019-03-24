#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''This file was created on 3/21/19 by damienrigden and programmed entilrely 
using pythonista on an iPhone 7plus.

This program calculates the quantities of ingredients needed for a meal in 
order to meet a desired calorie total and macronutrient percentages. The 
included example is a turkey and avocado sandwich.

The program ranks foods by their nutritional density, so it will make the 
perfect sandwich if you really like avocado, and dont really like tomatoes.'''

import copy

class Ingredient(list):
		'''Creates an ingredient object from a list, len(4) with carbs, fat, protein and weight in grams, defines each macro by gmacro/gtotal'''
		def __init__(self, input):
			self.input = input
			icarbs = self.input[0]
			ifat = self.input[1]
			iprotein = self.input[2]
			iweight = self.input[3]
			
			self.carbs = round(icarbs / iweight, 3)
			self.fat = round(ifat / iweight, 3)
			self.protein = round(iprotein / iweight, 3)
			self.calories = round(self.carbs * 4 + self.fat * 9 + self.protein * 4, 3)
			self.unitlist = [self.carbs, self.fat, self. protein, 1]
			
		def getcarbs(self):
			return self.carbs
			
		def getfat(self):
			return self.fat
		
		def getprotein(self):
			return self.protein
		
		def getcalories(self):
			return self.calories
			
		def __repr__(self):
			return 'ingredient(%r) [carb, fat, protein, weight]'  %self.input
			
		def __mul__(self, x):
			multiplied = []
			for item in self.unitlist:
				multiplied.append(round(item * x, 3))
			return multiplied
		
		def __str__(self):
			return 'ingredient(%r)' %self.unitlist
	

#Initializing my ingredients and a dictionary of them
avocado = Ingredient([12, 21, 2.9, 146])
bread = Ingredient([11.6, .9, 3.6, 28])
hummus = Ingredient([2.1, 1.4, 1.2, 15])
turkey = Ingredient([0, 2.1, 8, 28.4])
tomato = Ingredient([3.9, .2, .9, 100])
spinach = Ingredient([3.6, .4, 2.9, 100])
sandwich = {'avocado':avocado, 'bread':bread, 'hummus':hummus, 'turkey':turkey, 'tomato':tomato, 'spinach':spinach}

#input of meal requirements
print('')
totalcal = int(input('Enter desired calorie amount '))
percarb = int(input('Enter desired carb percentage '))
perprot = int(input('Enter desired protein percentage '))
perfat = (100 - (percarb + perprot))
print('Fat percentage ' + str(perfat))

permacros = [percarb, perfat, perprot]

#total grams of carbs fat protein based on total calories and desired percentage
totalcarb = (totalcal * (percarb * .01)) / 4
totalprot = (totalcal * (perprot * .01)) / 4
totalfat =  (totalcal * (perfat  * .01)) / 9


#find the ingredients with the most carbs fat and protein
fatweighted = []
carbweighted = []
proteinweighted = []

for item in sandwich.keys():
	fatweighted.append([sandwich[item].getfat(), sandwich[item], item])
	carbweighted.append([sandwich[item].getcarbs(), sandwich[item], item])
	proteinweighted.append([sandwich[item].getprotein(), sandwich[item], item])

#the follwing sort functions were sorting least to most by default. list items were a list of length 3, where the first element was the value to be sorted by
fatweighted.sort(reverse=True)
carbweighted.sort(reverse=True)
proteinweighted.sort(reverse=True)

mostfat = [fatweighted[0][1], fatweighted[0][2]]
mostcarb = [carbweighted[0][1], carbweighted[0][2]]
mostprotein = [proteinweighted[0][1], proteinweighted[0][2]]

maxmacrolist = [mostcarb, mostfat, mostprotein]

#this next part weights each ingredient by its macro rank
fatadjtot = 0
for a in range(len(fatweighted)):
	fatadjtot += fatweighted[a][0]
for x in range(len(fatweighted)):
	fatweighted[x].append(round((fatweighted[x][0])/fatadjtot,3))

caradjtot = 0
for b in range(len(carbweighted)):
	caradjtot += carbweighted[b][0]
for y in range(len(carbweighted)):
	carbweighted[y].append(round((carbweighted[y][0])/caradjtot,3))
	
proadjtot = 0
for c in range(len(proteinweighted)):
	proadjtot += proteinweighted[c][0]
for z in range(len(proteinweighted)):
	proteinweighted[z].append(round((proteinweighted[z][0])/proadjtot,3))

#next it calculates macro per gram of the weighted mixture of ingredients
fatpergram = 0
for item in fatweighted:
	fatpergram += (item[0] * item[3])

carpergram = 0
for item in carbweighted:
	carpergram += (item[0] * item[3])
	
propergram = 0
for item in proteinweighted:
	propergram += (item[0] * item[3])

#this part figures out the total number of grams of each macro mixture
fatingredients = totalfat/fatpergram
caringredients = totalcarb/carpergram
proingredients = totalprot/propergram

#this creates lists of the macro mixtures
fatmixture = []
for ing in fatweighted:
	fatmixture.append([ing[1], ing[2], round((fatingredients * ing[3]), 3)])

carmixture = []
for ing in carbweighted:
	carmixture.append([ing[1], ing[2], round((caringredients * ing[3]), 3)])

promixture = []
for ing in proteinweighted:
	promixture.append([ing[1], ing[2], round((proingredients * ing[3]), 3)])

fatmixture.sort()
carmixture.sort()
promixture.sort()

#adding up the total quantities
totmixture = copy.deepcopy(promixture)

for num in range(len(totmixture)):
	totmixture[num][2] += carmixture[num][2]
	totmixture[num][2] += fatmixture[num][2]
	totmixture[num][2] = round(totmixture[num][2], 3)
	
#figuring out calorie total of the guessed final mixture and adjusting to desired calorie amount
def calorieadj(totmixture, totalcal):
	guesscalories = 0
	for ing in totmixture:
		guesscalories += (ing[0].getcalories() * ing[2])
		guesscalories = round(guesscalories, 3)
	
	#find percentage that the calories were off of desired calories
	calorieratio = totalcal / guesscalories

	#adjust total mixture to meet new calorie amount
	for ing in totmixture:
		ing[2] *= calorieratio
		ing[2] = round(ing[2], 3)
	
	return totmixture

#next we figure out macro ratios of food list
def getnewmacros(totmixture):
	newcar = 0
	newfat = 0
	newpro = 0
	for item in totmixture:
		newcar += (item[0].getcarbs() * item[2])
		newfat += (item[0].getfat() * item[2])
		newpro += (item[0].getprotein() * item[2])
	
	newtotal = newcar + newfat + newpro
	newcarrat = round(((newcar / newtotal) * 100), 1)
	newfatrat = round(((newfat / newtotal) * 100) , 1)
	newprorat = round(((newpro / newtotal) * 100), 1)
	return [newcarrat, newfatrat, newprorat]

#gets adjustment ratios for macros
def macroadjrat(newmacrosL1, permacrosL2):
	madj= []
	for x in range(3):
		madj.append(round((newmacrosL1[x] / permacrosL2[x]), 3))
	
	return madj

#adjusts our food list based on macro adjustment ratios
def macroadjust(totmixture, maxmacrolist, macroadjrat):
	for item in totmixture:
		if item[1] == maxmacrolist[0][1]:
			item[2] /= macroadjrat[0]
			
		elif item[1] == maxmacrolist[1][1]:
			item[2] /= macroadjrat[1]
		
		elif item[1] == maxmacrolist[2][1]:
			item[2] /= macroadjrat[2]
			
		else:
			pass
	
	for item in totmixture:
		item[2] = round(item[2], 3)
		
	return totmixture

#this repeats the adjustment 20 times, edit to make it repeat the adjustment so it stops when newmacros and permacros are the same
for _ in range(20):
	totmixture = calorieadj(totmixture, totalcal)
	newmacros = getnewmacros(totmixture)
	macroadjusted = macroadjrat(newmacros, permacros)
	totmixture = macroadjust(totmixture, maxmacrolist, macroadjusted)

for item in totmixture:
	print(str(int(item[2])) + ' grams of ' + item[1])


''' Need to figure out how to get more tomato

Create a standard library of ingredients that you can select from to make a custom meal dictionary

If meal calculation is not possible shoot an error message that says to 'add an ingredient with more 'x'.'''

