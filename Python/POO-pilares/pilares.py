#class A:
   # a = 1 # atributo publico
    #__b = 2 #Atributo privado a classe A


#class B(A):
  #  __c = 3 #Atributo privado a classe B

  #  def __init__(self):
   #     print(self.a)
    #    print(self.__c)

#class C(B):


#a = A()
#print(a.a) # imprime 1

#b = B()

#print(b.__b) # Erro, __b é privado a classe A.
#print(b.__c)# Erro, __C é um atributo privado, somente chamado pela classe.


'''
class Animal():
    def __init__(self):
        print("Animal criado")

    def oQueSou(self):
        print("Animal")
    
    def come(self):
        print("Comendo")

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cachorro criado")
    
    def oQueSou(self):
        print("Cachorro")
    
    def late(self):
        print("Auau!")

c = Cachorro()

c.oQueSou()

c.come()

c.late()

cachorrin = Cachorro()

c.late
c.come
'''

class AnimalSelvagem():
    def mover(self):
        print("estou correndo")

    def come(self):
        print("comendo")

class AnimalDomestico():
    def mover(self):
        print("Estou andando")
    def getDono(self):
        return self.dono

class Cachorro(AnimalSelvagem,AnimalDomestico):
    def __init__(self, dono):
        self.dono = dono

    def late(self):
        print("Auau!")


c = Cachorro("Luis")

print(c.getDono())
c.come()
c.late()
c.mover()