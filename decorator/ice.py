from decorator.decoration import Decorator

class Ice(Decorator):
	def __init__(self,obj):
		self.__obj_hero = obj
		self.__damage = 3

	def displayPower(self):
		return self.__obj_hero.displayPower()+" Ice "

	def attack(self):
		return self.__obj_hero.attack()+self.__damage

	def setDamage(self,damage):
		self.__damage = damage
