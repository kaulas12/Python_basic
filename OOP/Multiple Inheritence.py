class User():
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print(f'Attack with power {self.power}')

class Archer(User):
  def __init__(self,name,arrows):
    self.name = name
    self.arrows = arrows
  def check_arrows(self):
    print(f'{self.arrows} remaining') 
  def run(self):
    print('Goblin, Wolf')

class HybridBorg(Wizard, Archer):
  def __init__(self,name,power,arrows):
    Archer.__init__(self,name,arrows)
    Wizard.__init__(self,name,power)


#instantiating multiple inheritence object
#
hb1 = HybridBorg('Hermoine',1000,900)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.run())
print(hb1.sign_in())