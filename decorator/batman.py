from decorator.hero import Hero

class Batman(Hero):
	__amountOfDestruction = None
	def __init__(self):
		self.__amountOfDestruction = 4

	def displayPower(self):
		return "muscels "

	def attack(self):
		return self.__amountOfDestruction

	def setDamage(self,damage):
		self.__amountOfDestruction = damage
