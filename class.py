class Animal:
    def __init__(self,id, nome, idade,raca,porte,peso,nr_chip):
        self.id=id
        self.nome=nome
        self.idade=idade
        self.raca=raca
        self.porte=porte
        self.peso=peso
        self.nr_chip=nr_chip

    def InfoAnimal(self):
        print(f"Nome: {self.nome}")

class Consulta(Animal):
    def __init__(self,id,doencas,internamento):
        super().__init__(id)
        self.doencas=doencas
        self.internamento=internamento
    
class Dono(Animal):
    def __init__(self,id,nome1,contato,nif,morada):
        super().__init__(id)
        self.nome1=nome1
        self.contato=contato
        self.nif=nif
        self.morada=morada

    def Imprime(self):
        print(f"Nome do dono: {self.nome1}")

def main():
    cao=Animal(1,"Bobi",5,"Rafeiro","Medio",15,123)
    cao.InfoAnimal()

    pessoa=Dono(1,"Ana",987456321,123654987,"Rua Teste")
    pessoa.Imprime()
  
   
if __name__=="__main__": 
    main()