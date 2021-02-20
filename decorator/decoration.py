from decorator.hero import Hero
from abc import ABC, abstractmethod

class Decorator(Hero,ABC):
	__obj_hero = None
	__damage= None

	def __init__(self,heroo):
		pass

	@abstractmethod
	def displayPower(self):
		pass

	@abstractmethod
	def attack(self):
		pass

	@abstractmethod
	def setDamage(self,obj):
		pass