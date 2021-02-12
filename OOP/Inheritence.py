#inheritence
class User():
  def sign_in(self):
    print('Logged In')
class Wizard(User): #To access the user class
  pass
class Archer():
  pass
wiz=Wizard()
print(wiz.sign_in())        