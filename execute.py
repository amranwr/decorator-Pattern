from decorator.spiderman import Spiderman
from decorator.fire import Fire
from decorator.ice import Ice
hero = Spiderman()
icePower = Ice(hero)
firePower = Fire(icePower)
firePower2 = Fire(firePower)

print("damage = {} points".format(firePower2.attack()))
print("sequence of power = {}".format(firePower2.displayPower()))
