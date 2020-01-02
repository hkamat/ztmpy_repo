class User():
	def sign_in(self):
		self.signed_in = True
		return 'logged in'

class Wizard(User):
	signed_in = False
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		if self.signed_in:
			print(f'Wizard {self.name} is attacking with {self.power}')
		else:
			print(f'Wizard {self.name} has not signed in so he cant attack. You are dead!!! Sorry...')


class Archer(User):
	signed_in = False
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		if self.signed_in:
			print(f'Archer {self.name} is attacking with {self.num_arrows}')
		else:
			print(f'Archer {self.name} has not signed in so he cant attack. You are dead!!! Sorry...')


archer1 = Archer('Robin', 100)
wizard1 = Wizard('Merlin', 'Shock')
wizard2 = Wizard('Gandalf', 'Strike')
wizard1.sign_in()
wizard1.attack()
Wizard.signed_in = True
wizard2.attack()