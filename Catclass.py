#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
peanut = Cat('peanut', 15)
garfield = Cat('garfield', 6)
sparkling = Cat('sparkling', 5)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
	# print(type(*args))
	# print(type(args))
	# print(args[0])
	max_age = 0
	name = ''
	for arg in args:
		if arg.age > max_age:
			max_age = arg.age
			name = arg.name
	  	
	return name, max_age

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
name, age = get_oldest_cat(peanut, garfield, sparkling)
print(f'The oldest cat is {name} which is {age} years old')