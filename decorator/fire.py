from decorator.decoration import Decorator

class Fire(Decorator):
	def __init__(self,obj):
		self.__obj_hero = obj
		self.__damage = 3

	def displayPower(self):
		return self.__obj_hero.displayPower()+" Fire "

	def attack(self):
		return self.__obj_hero.attack()+self.__damage

	def setDamage(self,damage):
		self.__damage = damage
