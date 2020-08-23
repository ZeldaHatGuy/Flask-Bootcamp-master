#class Dog():
#    species = 'mammal'
#    def __init__(self, breed, name ):
#        self.breed = breed
#        self.name = name



class Circle():
    pi = 3.14
    def __init__(self, radius=1):
      self.radius = radius


    def area(self):
        return self.radius * self.radius * self.pi
    
    def circumfrence(self):
        return 2 * self.pi * self.radius


class Animal():
    def __init__(self, fur):
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self,fur)
        print('Dog Created!')

    def report(self):
        print('I am a dog')



class book():
    def __init__(self,title,author,pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __repr__(self):

        #return f"Title: {self.title}, author: {self.author}"
        return "Title: {}, author: {}".format(self.title,self.author)
    def __len__(self):
        return self.pages

def tester(func):
    def help_func():
        print("do something")

        func()

        print("Help is on the way")

    return help_func

@tester
def need_help(name="Fred"):
    print("My name is {} and I need help".format(name))

need_help()