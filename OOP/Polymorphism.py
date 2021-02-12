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
  def __init__(self,name,num_arrows):
    self.name = name
    self.num_arrows = num_arrows
  def attack(self):
    print(f'attack with arrows {self.num_arrows}')

#polymorphism
wizard1 = Wizard('Harry Potter', 100)
archer1 = Archer('Weasley', 1900) 

def player_attack(char):
  char.attack()
#same name of method to be called
#different name of classes and parameters
player_attack(wizard1)
player_attack(archer1)  